from utils.card import Card
from typing import List
from random import choice, shuffle


class Player:

    def __init__(self):
        cards = Card()
        print(cards)
        print(List[Card])
        self.cards: List[Card] = []
        
        
        print(self.cards)
        self.turn_count = 0
        self.number_of_card = 0
        self.history: List[Card] = []

    def play(self):
        
        played_card = choice(self.cards)
        self.cards.remove(played_card)
        self.history.append(played_card)
        self.turn_count += 1
        self.number_of_card = len(self.cards)

        print(f"{self.name} turn {self.turn_count} played: {played_card.value} {played_card.icon} {played_card.color}")

        return played_card
    

    def __str__(self):

        return f"Player {self.name} with {self.number_of_cards} cards"
    
class Deck:
    def __init__(self):
        self.card = []

    def fill_deck(self):
        self.color = ["red", "black"]
        self.icon = ["♥", "♦", "♣", "♠"]
        self.card_color = []
        for i in range(len(self.color)):
            for j in range(len(self.icon)):
                if i == 0 and j <= 1:
                    self.card_color.append((self.color[i] + self.icon[j]))
                elif i == 1 and j > 1:
                    self.card_color.append((self.color[i] + self.icon[j]))
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.all_card = []
        for i in self.value:
            for j in self.card_color:
                self.all_card.append(i + j)
        return self.all_card
    
    def shuffle(self):

        shuffle(self.all_card)

        return self.all_card 
    

    def distribute(self):
        players = ["Me", "you", "he", "she"]
        self.card_distri = {}
        table = []
        self.number_of_card_player = len(self.all_card)// len(players)
  

        i = 0

        while len(self.all_card) > 0 and i < len(players):   
                table = self.all_card[:self.number_of_card_player]
                self.card_distri[players[i]] = table
                self.all_card = self.all_card[self.number_of_card_player:]
                i += 1

        return self.card_distri




test1 = Deck()
test1.fill_deck()
print(test1.distribute())

