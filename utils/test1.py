class Symbol:
    """
    This class creates all the card symbols (with colors).
    """
    def __init__(self):
        self.color = ["red", "black"]
        self.icon = ["♥", "♦", "♣", "♠"]
        self.card_color = []  # Initialize here
        self.color_type()

    def color_type(self):
        for i in range(len(self.color)):
            for j in range(len(self.icon)):
                if i == 0 and j <= 1:
                    self.card_color.append(self.color[i] + self.icon[j])
                elif i == 1 and j > 1:
                    self.card_color.append(self.color[i] + self.icon[j])

    def __str__(self):
        return str(self.card_color)


class Card(Symbol):
    def __init__(self):
        super().__init__()
        self.set_of_card()

    def set_of_card(self):
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.all_card = []
        for val in self.value:
            for sym in self.card_color:
                self.all_card.append(val + sym)

    def __str__(self):
        return str(self.all_card)


# Test the code
test = Card()
print(test)
