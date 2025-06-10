from player import Player, Deck
class Board:
    """
    This class choose the card played by each player at each turn
    """
    def __init__(self):
       self.players = ["Me", "you", "he", "she"]
       self.turn_count = 0
       self.active_cards = []
       self.history_cards = []

    def start_game(self):
       """
       This method launch the game 
       print all card played at each turn
       saved the history card and print the number of card in history card at each turn
       """
       
       print("game start !")

       deck = Deck()
       deck.fill_deck() 
       deck.shuffle()   
       distri = deck.distribute()
       
       while len(distri["Me"]) > 0:
          self.turn_count += 1
          print(f"--- Turn {self.turn_count} ---")             
          self.active_cards = []
          for player in self.players:
             card = distri[player].pop(0) 
             self.active_cards.append(card)
             self.history_cards.append(card)
             #print(f"In turn {self.turn_count}, player {player} played {self.active_cards}")
          print(f"active card = {self.active_cards}")
          print(f"Number of card in history card = {len(self.history_cards)}")
          #print(f"this is history card played after {self.turn_count} turn : {self.history_cards}")
       print("Game over !")
          
          

