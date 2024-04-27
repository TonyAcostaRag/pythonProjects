import os
import uuid


os.chdir('todo_list')


class TodoList:
    __counter = 0
    __name_list_format = 'todo_list'

    def __init__(self):
        TodoList.__counter += 1
        self.__list_name = self.__name_list_format + str(TodoList.__counter) + '.txt'
        self.task_dict = {}
        try:
            stream = open(self.__list_name, 'w')
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
                self.browse_task()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.remove_task()
            elif choice == '4':
                print('Quiting from program...')
            choice

    def add_task(self):
        task = input('[ADD TASK]\nWhat is the task? ')
        deadline = input('What is the deadline? ')
        id = str(uuid.uuid4())

        try:
            stream = open(self.__list_name, 'a')
            stream.write('\n' + str(id) + ' | ' + task + ' | ' + deadline)
            self.task_dict[id] = task + ' | ' + deadline
            stream.close()
        except Exception as e:
            print('An Error occurred when opening the list for ',
                  self.__list_name, e)

    def browse_task(self):
        print()
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

    def remove_task(self):
        print('\n[COMPLETE TASK]')

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
                if task_to_complete in self.task_dict.keys():
                    print('\nCompleted task: ', self.task_dict.pop(task_to_complete))
                else:
                    print('\nNo valid id entered!')

            stream.close()
        except Exception as e:
            print('An Error occurred when reading the file:', e)

        try:
            stream = open(self.__list_name, 'w')
            for key, value in self.task_dict.items():
                stream.write(key + ' | ' + value)
            stream.close()
        except Exception as e:
            print('An Error occurred when re-writting the file:', e)


list_one = TodoList()
list_one.check_list()
