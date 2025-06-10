from player import Player, Deck
class Board:
    def __init__(self):
       players = players = ["Me", "you", "he", "she"]
       turn_count = 0
       active_cards = []
       history_cards = []

    def start_game(self):
       
       print("game start")

       deck = Deck()
       distri = deck.distribute()
       print(distri)

"""
- A method `start_game()` that will:
  - Start the game,
  - Fill a `Deck`,
  - Distribute the cards of the `Deck` to the players.
  - Make each `Player` `play()` a `Card`, where each player should only play 1 card per turn, and all players have to play at each turn until they have no cards left.
  - At the end of each turn, print:
    - The turn count.
    - The list of active cards.
    - The number of cards in the `history_cards`.

"""

test = Board()
print(test.start_game())