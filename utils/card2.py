class Symbol:
    """
    This class create all the card
    """
    def __init__(self):
        self.color = ["red", "black"]
        self.icon = ["♥", "♦", "♣", "♠"]
        #self.color_type()
    

    def __str__(self):
        return str(self.color, self.icon)
    

class Card(Symbol):
    def __init__(self):
        super().__init__()
        self.set_of_card()
        
        

    def set_of_card(self):
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        

    def __str__(self):
        
        return str(self.value)
    



#test = Card(Symbol)
#test.color_type()
#print(test.__str__())
#print(test.set_of_card())
test = Card()
test