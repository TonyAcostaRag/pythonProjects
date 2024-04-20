import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def present(self):
        return self.value + ' of ' + self.suit


class Deck:

    def __init__(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) != 0:
            deal = self.cards[-1]
            del self.cards[-1]
            return deal
        else:
            return None

    def count_remaining(self):
        return len(self.cards)

    def get_remaining(self):
        return [i.present() for i in self.cards]


deck_one = Deck()

# showing the just created cards in Deck:
for i in deck_one.get_remaining():
    print(i)

deck_one.shuffle()

print('\nShowing the shuffled cards in Deck:')
for i in deck_one.get_remaining():
    print(i)
