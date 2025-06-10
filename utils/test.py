from utils.card import Card
from random import choice


class Player:

    def __init__(self):
        cards = Card()
        self.cards = list(cards)
        print(len(cards))
        
        #print(self.cards)
        self.turn_count = 0
        self.number_of_card = 0
        self.history = []

    def play(self):
        player1 = choice(self.cards)
        #print(len(cards))
        return self.cards


test1 = Player()
print(test1.play())


from utils.card import Card

class Player:
    def __init__(self):
        self.cards = Card()  # Initializes the Card object
        print("Player's cards initialized:")
        print(self.cards)  # __str__ method of Card is called here
        self.turn_count = 0
        self.number_of_card = 0
        self.history = []

    def play(self):
        return self.cards

# Create an instance of Player
test1 = Player()

# Access the card set directly
print("All cards in the player's hand:")
print(test1.cards.all_card)  # Access the list of cards


