from utils.card2 import Card
from random import choice


class Player:

    def __init__(self):
        cards = Card()
        self.cards = cards
        print(len(cards))
        
        print(type(self.cards))
        self.turn_count = 0
        self.number_of_card = 0
        self.history = []

    def play(self):
        #player1 = choice(self.cards)
        #print(len(cards))
        self.card_color = []
        for i in range(len(self.color)):
            for j in range(len(self.icon)):
                if i == 0 and j <= 1:
                    self.card_color.append((self.color[i] + self.icon[j]))
                elif i == 1 and j > 1:
                    self.card_color.append((self.color[i] + self.icon[j]))
        return self.cards


test1 = Player()
print(test1.play())