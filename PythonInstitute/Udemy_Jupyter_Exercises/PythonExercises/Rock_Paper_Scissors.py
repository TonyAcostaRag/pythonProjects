import random


class Player:
    def __init__(self, score=0):
        self.__score = score

    def add_score(self):
        self.__score += 1

    def get_score(self):
        return self.__score


class Human(Player):
    def __ini__(self):
        super().__init__()

    def move(self):
        choice = input('\nRock, Paper or Scissors [r/p/s]? ')
        while choice.lower() not in ['r', 'p', 's']:
            choice = input('Rock, Paper or Scissors [r/p/s]? ')

        return choice


class Computer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        return random.choice(['r', 'p', 's'])


class Game:
    message = '''--- Rock Paper Scissors Game ---\nHow many rounds would you like to play? '''

    user = Human()
    computer = Computer()
    num_of_rounds = 0

    def take_choices(self, user, computer):
        user_choice = user.move()
        computer_choice = computer.move()
        print('You:', user_choice, '| Computer:', computer_choice)
        return (user_choice, computer_choice)

    def calculate_scores(self, round_choices, user, computer):

        result_dict = {
            ('r', 'r'): 'Tie',
            ('r', 'p'): 'computer win',
            ('p', 'r'): 'user win',
            ('p', 'p'): 'Tie',
            ('p', 's'): 'computer win',
            ('s', 'p'): 'user win',
            ('s', 's'): 'Tie',
            ('s', 'r'): 'computer win',
            ('r', 's'): 'user win',
        }

        result = result_dict.get(round_choices)

        if result == 'Tie':
            user.add_score()
            computer.add_score()
            print('This round is a tie')
        elif result == 'user win':
            user.add_score()
            print('You won this round!')
        elif result == 'computer win':
            computer.add_score()
            print('You lost this round!')

    def carrying_rounds(self):
        while True:
            try:
                num_of_rounds = int(input(self.message))

                for i in range(num_of_rounds):
                    round_choices = self.take_choices(self.user, self.computer)
                    self.calculate_scores(round_choices, self.user, self.computer)

                break

            except ValueError:
                print('Enter an integer input')

    def present_summary_game(self):
        user_points = self.user.get_score()
        computer_points = self.computer.get_score()
        message = '\n[Game Summary] Your points: ' + str(user_points) + ' | Computer points: ' + str(computer_points)

        if user_points > computer_points:
            message += '\nYou won.'
        elif user_points < computer_points:
            message += '\nComputer won.'
        else:
            message += '\nIt was a tie.'

        print(message)

    def play(self):
        self.carrying_rounds()
        self.present_summary_game()


game_one = Game()
game_one.play()
