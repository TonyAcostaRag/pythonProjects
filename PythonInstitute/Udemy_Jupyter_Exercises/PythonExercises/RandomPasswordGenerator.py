import random

message = '''
-- Password generator --
Choose option:
1: generate password
2: exit the program
Your choice: '''

alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digit_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
special_list = ['!', '@', '#', '$', '%', '&', '*', '^', '|', '(', ')', '_', '+']


def generate_pass():
    print('\nGenerate password function')
    password_length = int(input('Provide password length: '))
    uppercase_letters = input('Use uppercase letters? (y/n):')
    digits_letters = input('Use digits? (y/n):')
    special_char_letters = input('Use special characters? (y/n):')

    generated_password = ''

    i = 0
    while i < password_length:
        type_char = random.randint(1, 3)
        if type_char == 1:
            alpha = str(random.choice(alpha_list))
            type_alpha = random.randint(1, 2)
            if type_alpha == 1 and uppercase_letters.lower() == 'y':
                generated_password += alpha.upper()
                i += 1
            else:
                generated_password += alpha
                i += 1
        elif type_char == 2 and digits_letters.lower() == 'y':
            generated_password += str(random.choice(digit_list))
            i += 1
        elif type_char == 3 and special_char_letters.lower() == 'y':
            generated_password += str(random.choice(special_list))
            i += 1

    print('Generated password:', generated_password)


while True:

    try:
        option = int(input(message))

        if option == 1:
            generate_pass()
        elif option == 2:
            print('Bye!')
            break
        else:
            print('Please enter a correct value')

    except ValueError:
        print('Please enter a correct value')
