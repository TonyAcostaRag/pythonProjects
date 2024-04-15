import errno
import sys
from os import strerror


class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    pass


class FileEmpty(StudentsDataException):
    pass


class StudentResults:

    def __init__(self, filename=input("Enter the file name to read: ")):
        self.student_dict = {}
        #self.filename = filename
        #self.filename = input("Enter the file name to read:")
        self.filename = 'samplefile.txt'
        # Test file for empty file
        # self.filename = 'emptyFile.txt'
        # Test non existence file
        # self.filename = 'nonExistenceFile.txt'
        # Test erroneous format
        # self.filename = 'erroneousFile.txt'

    def read_content(self):
        try:
            #filename = input("Enter the file name to read:")
            #filename = 'samplefile.txt'
            #filename = 'emptyFile.txt'
            #filename = 'nonExistenceFile.txt'
            #filename = 'erroneousFile.txt'
            file = open(self.filename, "rt", encoding="UTF-8")

            student_notes = {}
            line = file.readline()
            if line == '':
                raise FileEmpty

            while line != '':

                line_list = line.split("\t")
                if len(line_list) != 3:
                    raise BadLine

                if line_list[0] + " " + line_list[1] not in student_notes:
                    student_notes[line_list[0] + " " + line_list[1]] = float(line_list[2])
                else:
                    student_notes[line_list[0] + " " + line_list[1]] += float(line_list[2])

                line = file.readline()

            self.student_dict = dict(sorted(student_notes.items()))

            file.close()
        except FileEmpty as FE:
            print("Exception. The file is empty.")
        except BadLine as BL:
            print("The is a line in file not following the format.")
        except IOError as ioE:
            print("There is a IO Error:", strerror(ioE.errno))

    def display_report(self):
        for key, value in self.student_dict.items():
            print(key, value)


notes_one = StudentResults()

notes_one.read_content()
notes_one.display_report()
