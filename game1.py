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

    def card_value(self, card):
       """
       This method return the index of card value in value_order
       """
       value_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
       for val in sorted(value_order, key=len, reverse=True):
          if card.startswith(val):
             return value_order.index(val)
          

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
       # Initialization of score
       count_score = {player : 0 for player in distri} 
       
       
       while len(distri["Me"]) > 0:
          self.turn_count += 1
          print(f"--- Turn {self.turn_count} ---")             
          self.active_cards = []
          for player in self.players:
             print(f"{player} this is your cards : {distri[player]}")
             # the player must choose the index of the card he want to play
             card_choosed = int(input(f"{player} which card would you want to play (give index) = "))
             card = distri[player].pop(card_choosed -1) # delete of real position not python index
             self.active_cards.append(card)
             self.history_cards.append(card)
          print(f"active card of this turn = {self.active_cards}") # print of list of card played in a turn
          max_card = max(self.active_cards, key=self.card_value)
          print(f"max card of this turn = {max_card}")
          # related the max card to the player
          for i in range(len(self.active_cards)):
             if self.active_cards[i] == max_card:
                count_score[self.players[i]] = count_score.get(self.players[i], 0) + 1
                print(f"score = {count_score}")
          
       winner = max(count_score, key=count_score.get)
       print("Game over !")
       print(f"The Winner is : {winner} with a score of {count_score[winner]}")

       
          
          
