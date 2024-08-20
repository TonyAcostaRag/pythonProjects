import os
import uuid


if os.getcwd()[-9:] != 'todo_list':
    os.chdir('todo_list')


class TodoList:
    __counter = 0
    __name_list_format = 'todo_list'

    def __init__(self):
        if len([i for i in os.listdir() if i.split('.')[1] == 'txt']) > 0:
            print('Available lists:\n')
            for file in sorted(os.listdir()):
                fileSplit = file.split('.')
                #if fileSplit[0] == TodoList.__name_list_format and fileSplit[1] == 'py':
                #    continue
                #elif fileSplit[0][:-1] == TodoList.__name_list_format and fileSplit[1] == 'txt':
                if fileSplit[0][:-1] == TodoList.__name_list_format and fileSplit[1] == 'txt':
                    print('->', file)
                    TodoList.__counter += 1

            choice = input('\n[1] To create a new list.\n[-> name list] Enter the list you want to update.\nChoice: ')
            while choice != '1' and choice not in os.listdir():
                choice = input('Enter a valid choice: ')
        else:
            choice = '1'

        self.__task_dict = {}
        open_mode = ''

        if choice == '1':
            TodoList.__counter += 1
            self.__list_name = self.__name_list_format + str(TodoList.__counter) + '.txt'
            open_mode = 'w'
        elif choice in os.listdir():
            self.__list_name = choice
            open_mode = 'r'

        try:
            stream = open(self.__list_name, open_mode)

            if choice != '1':
                for line in stream:
                    if line.split(' | ')[0] not in self.__task_dict:
                        self.__task_dict[line.split(' | ')[0]] = line.split(' | ')[1] + ' | ' + line.split(' | ')[2]

            stream.close()
        except Exception as e:
            print('An Error occurred when creating the todo list file:', e)

    def check_list(self):

        message = '''\n== TODO LIST ==
        [1] show tasks
        [2] add task
        [3] complete task
        [4] exit
        Your choice: '''

        choice = ''
        while choice != '4':
            choice = input(message)
            if choice == '1':
                self.__browse_task()
            elif choice == '2':
                self.__add_task()
            elif choice == '3':
                self.__remove_task()
            elif choice == '4':
                print('Quiting from program...')

    def __add_task(self):
        task = input('[ADD TASK]\nWhat is the task? ')
        deadline = input('What is the deadline? ')
        id = str(uuid.uuid4())

        try:
            stream = open(self.__list_name, 'a')
            stream.write(str(id) + ' | ' + task + ' | ' + deadline + '\n')
            self.__task_dict[id] = task + ' | ' + deadline
            stream.close()
        except Exception as e:
            print('An Error occurred when opening the list for ',
                  self.__list_name, e)

    def __browse_task(self):
        try:
            stream = open(self.__list_name, 'r')
            line = stream.readline()
            if line == '':
                print('\n[YOUR TASKS]\nEmpty list')
            else:
                print('\n[YOUR TASKS]')
                while line != '':
                    print(line)
                    line = stream.readline()

            stream.close()
        except Exception as e:
            print('An Error occurred when reading the file:', e)

    def __remove_task(self):
        print('\n[COMPLETE TASK]')
        task_to_complete = ''
        try:
            stream = open(self.__list_name, 'r')
            line = stream.readline()
            if line == '':
                print('\n[YOUR TASKS]\nEmpty list\n\nNo tasks to complete')
            else:
                print('\n[YOUR TASKS]')
                while line != '':
                    print(line)
                    line = stream.readline()

                task_to_complete = input('\nEnter id to complete: ')

            stream.close()
        except Exception as e:
            print('An Error occurred when reading the file:', e)

        if len(self.__task_dict) > 0:
            if task_to_complete in self.__task_dict.keys():
                print('\nCompleted task: ', self.__task_dict.pop(task_to_complete))

                try:
                    stream = open(self.__list_name, 'w')
                    for key, value in self.__task_dict.items():
                        stream.write(key + ' | ' + value + '\n')
                    stream.close()
                except Exception as e:
                    print('An Error occurred when re-writting the file:', e)

            else:
                print('\nNo valid id entered!')


if __name__ == '__main__':
    list_one = TodoList()
    list_one.check_list()
