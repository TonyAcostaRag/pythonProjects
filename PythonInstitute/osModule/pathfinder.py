import os


"""
 -- Prerequisites and cleaning of the folders needed.

#path_configuration()
#tear_down_path_config()
#list_directories()
"""
def path_configuration():
    os.system("mkdir -p tree/c/other_courses/cpp")
    os.system("mkdir tree/c/other_courses/python")

    os.system("mkdir -p tree/cpp/other_courses/c")
    os.system("mkdir tree/cpp/other_courses/python")

    os.system("mkdir -p tree/python/other_courses/c")
    os.system("mkdir tree/python/other_courses/cpp")


def tear_down_path_config():
    os.chdir("/Users/antonioacostaflores/Documents/DevEnvironments/pythonInstitute/PythonInstitute/osModule")
    os.system("rm -r tree")


def list_directories():
    print("Current working directory: ", os.listdir())


"""
find() function.

Arguments: 
    path: Relative or absolute path; 2 positive test cases.
    dir: Name of the directory that you want to find; 1 positive test case. 
"""
def find(path, dir):
    os.chdir(path)
    workingDirectory = os.getcwd()
    if len(os.listdir()) > 0:
        for i in os.listdir():
            os.chdir(workingDirectory)
            try:
                if i == dir:
                    print("Desired directory found:", os.getcwd() + "/" + dir)
                    continue
                else:
                    find(i, dir)
                    continue
            except NotADirectoryError:
                print("Not a directory '" + i + "', pass")
                continue


"""
approach:
    Recursive directory search.

program output:
    Display the absolute paths if the directory were found with the given name.
"""
#path_configuration()
find("./tree", "python")
#tear_down_path_config()
