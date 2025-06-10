from utils.card import Card
from typing import List
from random import choice, shuffle


class Player:
    """
    This class create number of turn of the game,
    history of played card
    """

    def __init__(self):
        cards = Card()
        self.cards = []
        self.turn_count = 0
        self.number_of_card = 0
        self.history = []

    def play(self):
        """
        This method choose card to play by a player
        """
        
        played_card = choice(self.cards)
        self.cards.remove(played_card)
        self.history.append(played_card)
        self.turn_count += 1
        self.number_of_card = len(self.cards)

        print(f"{self.name} turn {self.turn_count} played: {played_card.value} {played_card.icon} {played_card.color}")

        return played_card
    

    def __str__(self):
        """
        This method return the name of player
        and the card he played
        """

        return f"Player {self.name} with {self.number_of_cards} cards"
    
class Deck:
    """
    This method fill randomly the deck"""
    def __init__(self):
        self.card = []

    def fill_deck(self):
        """
        This method create the set of 52 cards 
        with color, icon and number
        """
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

    def __str__(self):
        """
        This method return all the 52 created card
        """
        
        return str(self.all_card)
       
    
    def shuffle(self):
        """
        This method shuffle created cards
        """

        shuffle(self.all_card)

    
    def __str__(self):
        """
        This method return shuffled 52 created card
        """
        
        return str(self.all_card)

    

    def distribute(self):
        """
        This method distribute card to each player
        """
        players = ["Me", "you", "he", "she"] # list of players
        self.card_distri = {} # This will attribute a set of cards to each player
        table = []
        self.number_of_card_player = len(self.all_card)// len(players) #number of card per player
  

        i = 0

        while len(self.all_card) > 0 and i < len(players):   
                table = self.all_card[:self.number_of_card_player]
                self.card_distri[players[i]] = table
                self.all_card = self.all_card[self.number_of_card_player:]
                i += 1


    

        return self.card_distri





