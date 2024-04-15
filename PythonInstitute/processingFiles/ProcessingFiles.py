import errno
import sys
from os import strerror

sys.stderr.write("This is a modified error message in the sys module\n\n")

def first_example():
    try:
        s = open("c:/users/user/Desktop/file.txt", "rt")
        # Actual processing goes here.
        s.close()
    except Exception as exc:
        if exc.errno == errno.ENOENT:
            print("The file doesn't exist.")
        elif exc.errno == errno.EMFILE:
            print("You've opened too many files.")
        else:
            print("The error number is:", exc.errno)

def second_example():
    try:
        s = open("c:/users/user/Desktop/file.txt", "rt")
        # Actual processing goes here.
        s.close()
    except Exception as exc:
        print("The file could not be opened:", strerror(exc.errno))

def reading_file_fromDownloads():

    stream = open("/Users/antonioacostaflores/Downloads/tzop.txt", "rt", encoding="UTF-8")

    print("Content of the file: ->", stream.read(10), "<- End of the content of the file", sep="")

def reading_charByChar_fromTextFile():

    counter = 0
    try:
        s = open("/Users/antonioacostaflores/Downloads/text.txt", "rt", encoding="UTF-8")
        ch = s.read(1)

        while ch != '':
            print(ch, end="")
            counter += 1
            ch = s.read(1)

        s.close()
        print("\n\ntotal chars:", counter)

    except IOError as exp:
        print("I/O Error ocurred:", strerror(exp.errno))

def reading_wholeContent_fromTextFile():
    try:
        cnt = 0
        s = open('/Users/antonioacostaflores/Downloads/text.txt', "rt")
        content = s.read()
        for ch in content:
            print(ch, end='')
            cnt += 1
        s.close()
        print("\n\nCharacters in file:", cnt)

    except IOError as e:
        print("I/O error occurred: ", strerror(e.errno))

def reading_lineByLine_fromTextFile():
    try:
        counter_lines = counter_chars = 0
        s = open("/Users/antonioacostaflores/Downloads/text.txt", "rt", encoding="UTF-8")
        line = s.readline()

        while line != '':
            counter_lines += 1

            for ch in line:
                print(ch, end="")
                counter_chars += 1

            line = s.readline()

        s.close()

        print("\n\nTotal chars in the file", counter_chars)
        print("Total lines in the file", counter_lines)

    except IOError as exp:
        print("There is an IO Error", strerror(exp.errno))

def reading_allLines_fromTextFile():
    try:
        ccnt = lcnt = 0
        s = open('/Users/antonioacostaflores/Downloads/text.txt', 'rt')
        lines = s.readlines(20)
        while len(lines) != 0:
            for line in lines:
                lcnt += 1
                for ch in line:
                    print(ch, end='')
                    ccnt += 1
            lines = s.readlines(10)
        s.close()
        print("\n\nCharacters in file:", ccnt)
        print("Lines in file:     ", lcnt)
    except IOError as e:
        print("I/O error occurred:", strerror(e.errno))

def experiment_readlines_method():
    print("outer methods to check the file only readlines")
    s = open("/Users/antonioacostaflores/Downloads/text.txt", "rt", encoding="UTF-8")
    print(s.readlines(2))
    print(s.readlines(2))
    print(s.readlines(2))
    print(s.readlines())
    s.close()

def reading_lineAsIterator_fromTextFile():
    try:
        ccnt = lcnt = 0
        for line in open('/Users/antonioacostaflores/Downloads/text.txt', 'rt'):
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        print("\n\nCharacters in file:", ccnt)
        print("Lines in file:     ", lcnt)
    except IOError as e:
        print("I/O error occurred: ", strerror(e.errno))

def writing_charByChar():
    try:
        fo = open('newtext.txt', 'wt')  # A new file (newtext2.txt) is created.
        for i in range(10):
            s = "line #" + str(i + 1) + "\n"
            fo.write(s)
            for ch in s:
                fo.write(ch)
        fo.close()
    except IOError as e:
        print("I/O error occurred: ", strerror(e.errno))

def writing_wholeLine():
    try:
        fo = open('newtext_WholeLine.txt', 'wt')
        for i in range(10):
            fo.write("line #" + str(i + 1) + "\n")
        fo.close()
    except IOError as e:
        print("I/O error occurred: ", strerror(e.errno))

def check_binaryArray_For_Char():
    data_a = bytearray(ord('a'))
    data_b = bytearray(ord('b'))
    data_10 = bytearray(10)

    count_a = count_b = count_10 = 0

    print("Printing the a data", data_a, sep="\n")
    print()
    print("Printing the b data", data_b, sep="\n")
    print()
    print("Printing the 10 data", data_10, sep="\n")

    print("\nPrinting all elements from byteArray for 'a'")
    for i in data_a:
        print(i, end=" ")
        count_a += 1
        if count_a % 15 == 0:
            print()
    print()

    print("\nPrinting all elements from byteArray for 'b'")
    for i in data_b:
        print(i, end=" ")
        count_b += 1
        if count_b % 15 == 0:
            print()
    print()

    print("\nPrinting all elements from byteArray for '10'")
    for i in data_10:
        print(i, end=" ")
        count_10 += 1
        if count_10 % 15 == 0:
            print()
    print()

def convert_BiteArray_To_BinaryFile():
    data = bytearray(10)

    for i in range(len(data)):
        data[i] = 10 + i

    print("\nPrinting data elements:")
    count = 0
    for i in data:
        print(i, end=" ")
        count += 1
        if count % 15 == 0:
            print()
    print()

    try:
        binary_file = open('binary_file', 'wb')
        successful_written_bytes = binary_file.write(data)
        print("successful written bytes:", successful_written_bytes)
        binary_file.close()
    except IOError as ioE:
        print("There is a IOError", strerror(ioE.errno))

def readBytes_from_BinaryFile():

    data = bytearray(10)

    print("Printing the elements of data:")
    for i in data:
        print(i, end=" ")
    print()

    try:
        binary_file = open('binary_file', 'rb')
        success_Bytes_read = binary_file.readinto(data)
        print("Successful bytes read:", success_Bytes_read)
        binary_file.close()

        print("Hexadecimal values:")
        for i in data:
            print(hex(i), end=" ")
        print()

        print("Data values as they are:")
        for i in data:
            print(i, end=" ")
        print()

    except IOError as IoE:
        print("There is an IO Error:", strerror(IoE.errno))

def readBytes_from_WholeBinaryFile():

    try:
        binary_file = open('binary_file_copy', 'rb')
        data = bytearray(binary_file.read())
        binary_file.close()

        for i in data:
            print(i, end=" ")

    except IOError as ioE:
        print("There is an IO Error:", strerror(ioE.errno))

def readBytes_from_PartialBinaryFile():

    try:
        binary_file = open('binary_file_copy', 'rb')
        data = bytearray(binary_file.read(6))
        binary_file.close()

        for i in data:
            print(hex(i), end=" ")

        print()

        for i in data:
            print(i, end=" ")

    except IOError as ioE:
        print("There is a IO problem:", strerror(ioE.errno))

def copying_files():
    srcname = input("Enter the source file name: ")

    try:
        src = open(srcname, 'rb')
    except IOError as ioE:
        print("There is a problem reading the file:", strerror(ioE.errno))
        exit(ioE.errno)

    dstname = input("Enter the destination file name: ")

    try:
        dst = open(dstname, 'wb')
    except IOError as ioE:
        print("Cannot create the destination file:", strerror(ioE.errno))
        src.close()
        exit(ioE.errno)

    buffer = bytearray(65536)
    total = 0

    try:
        readin = src.readinto(buffer)
        while readin > 0:
            written = dst.write(buffer[:readin])
            total += written
            readin = src.readinto(buffer)
    except IOError as ioE:
        print("Cannot create the destination file:", strerror(ioE.errno))

    print("Total bytes written:", total)
    src.close()
    dst.close()



#first_example()
#second_example()
#reading_file_fromDownloads()
#reading_charByChar_fromTextFile()
#reading_wholeContent_fromTextFile()
#reading_lineByLine_fromTextFile()
#reading_allLines_fromTextFile()
#reading_lineAsIterator_fromTextFile()
#writing_charByChar()
#writing_wholeLine()
#check_binaryArray_For_Char()
#convert_BiteArray_To_BinaryFile()
#readBytes_from_BinaryFile()
#readBytes_from_WholeBinaryFile()
#readBytes_from_PartialBinaryFile()
copying_files()
