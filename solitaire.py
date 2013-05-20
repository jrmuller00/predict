class Card(object):
    """
    The Card class implements data nd functionality for a playing card

    The Card class has three data members
        
    string  Suit = ['clubs','hearts','diamonds','spades']   # specifies the suit of the card
    int     Value = [1,2,3,4,5,6,7,8,9,10,11,12,13]         # card value, note that 1 = Ace, 11 = Jack, 12 = Queen, 13 = King
    boolean Visible = True | False                          # determines if the card value is visible to the player

    """

    def __init__(self):
        """
        Initializes an empty card

        """
        self.Suit = ""
        self.Value = 0
        self.Visible = true

    def __init__(self, suit, value, visible):
        """
        intiialize the card with user specified values
        """
        self.Suit = suit
        self.Value = value
        self.Visible = visible

    def getCardValue(self):
        """
        This will return the card value

        int 1-13
        """
        return self.Value

    def setCardValue(self,value):
        """
        This will set the card value

        int 1-13
        """


    def getCardSuit(self):
        """
        This will get the card suit
        suit = ['clubs','hearts','diamonds','spades']
        """
        return self.Suit

    def setCardSuit(self, suit):
        """
        This will set the card suit which has to be:
        suit = ['clubs','hearts','diamonds','spades']
        """

    def getVisible(self):
        """
        This will determine if the card is face up or 
        face down to the user, ie if it shows the suit
        and value or whether it shows the back of the card
        """
        return self.Visible

    def setVisible(self, value):
        """
        This will set the visbility of the card
        to the user value = True | False
        """
        self.Visible = value

    def toggleVisible(self):
        """
        This will toggle the visbility between
        true | false
        """
        if self.Value == True:
            self.Visible = False
        else:
            self.Visible = True
    return


class CardPile(object):
    
    """
    The card pile object will be used to manage the various card piles
    used in the game including the main deck, the discard pile and the
    piles that cards in play are moved to and from 
    
    """
    
    def __init__(self):
        """
        Initialize an empty pile as a stack
        """
        self.pile=[]
        return
    
    
    def pushCard(card):
        """
        This will push the card onto the pile
        """
        
    def popCard():
        """
        This will pop the top card off the stack
        and remove it form the pile
        """
        return self.pile.pop()
        
    def shuffle():
        """
        shuffleDeck will shuffle the cards in the card pile.
        This will mainly be used to shuffle the cards in the main
        deck at the beginning of the game
        """ 
        
    def initializeDeck():
        """
        initializeDeck will create a full deck of cards
        """
        
    def  clearPile():
        """
        clearPile is used to empty the list of all its cards.
        This will be used a the end of the game to clear the 
        card piles and start again
        """
        
        
    def moveCard(targetPile):
        """
        moveCard will first check if the top card 
        from the source pile can be moved to the 
        targetPile.  If the move is valid, it will
        pop the card from the source pile and push it
        to the targetPile
        """
        
        
        
    
