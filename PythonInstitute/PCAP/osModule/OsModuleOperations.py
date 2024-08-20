import os
import platform as plat




def print_so_information():
    print("The uname object from os module (like command 'uname -a') :", os.uname(), sep="\n", end="\n\n")
    print("The uname object from platform module:", plat.uname(), sep="\n", end="\n\n")

    print("The name attribute:", os.name, end="\n\n")


def create_relative_path_directory(rel_directory_name):
    os.mkdir(rel_directory_name)


def create_explicit_current_directory(current_directory):
    os.mkdir(current_directory)


def create_directory_on_parent_directory(parent_directory):
    os.mkdir(parent_directory)


def create_directory_on_absolute_directory(absolute_directory):
    os.mkdir(absolute_directory)


def create_two_directories_recursively(recursive_directories_path):
    os.makedirs(recursive_directories_path)


def list_directories():
    print(os.listdir())


def change_directory(new_directory):
    os.chdir(new_directory)


def get_currentWorkingDirectoty():
    print("Current directory:", os.getcwd())


def delete_directory(directory):
    os.rmdir(directory)


def delete_directory_recursively(parentDirectoty):
    os.removedirs(parentDirectoty)


print_so_information()
list_directories()
try:
    create_relative_path_directory("relative_directory")
    create_explicit_current_directory("./explicit_relative_directory")
    create_directory_on_parent_directory("../parent_of_current_directory")
    create_directory_on_absolute_directory("/Users/antonioacostaflores/Documents/DevEnvironments/"
                                           "pythonInstitute/PythonInstitute/osModule/absolute_directory")
    create_two_directories_recursively("parent_directory/recursive_creation")
except FileExistsError as FEE:
    print("FileExistError:", os.strerror(FEE.errno))


list_directories()
change_directory("parent_directory") # Good
list_directories()
change_directory("recursive_creation")
list_directories()
change_directory("/Users/antonioacostaflores/Documents/DevEnvironments/pythonInstitute/PythonInstitute/osModule")
get_currentWorkingDirectoty()
delete_directory("absolute_directory")
delete_directory("explicit_relative_directory")
delete_directory_recursively("parent_directory/recursive_creation")

values = [os.system("mkdir directoryCreatedWithSystemFunc"),
          os.system("rmdir directoryCreatedWithSystemFunc"),
          os.system("mkdir newDirectoryToDelete"),
          os.system("cd newDirectoryToDelete"),
          os.system("pwd"),
          os.system("ls"),
          os.system("mkdir newDirectoryToDelete/newDirectoryToDeleteTwo"),
          os.system("rm -r newDirectoryToDelete"),
          os.system("rmdir relative_directory"),
          os.system("rmdir /Users/antonioacostaflores/Documents/DevEnvironments/"
                    "pythonInstitute/PythonInstitute/parent_of_current_directory"),
          os.system("ls")
          ]

for i in range(len(values)):
    print("Value in ", i, " -> ", values[i])
