import random
from Card import Card
class Deck:

    def __init__(self):
        self.currentDeck = []
        self.card = []

    def newDeck(self):
        self.currentDeck = []
        self.currentDeck.extend(range(1, 53))
        random.shuffle(self.currentDeck)
        print("Shuffling Deck")
        return self.currentDeck

    def dealCard(self, house):
        drawCard = house.pop()
        card = Card()
        card.determineCardType(drawCard)
        self.card = [card.face, card.suit, card.value]
        return self.card