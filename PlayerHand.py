class PlayerHand:

    def __init__(self):
        self.hand = []

    def buildHand(self, drawCard):
        self.hand.append(drawCard)
#        print(self.hand)

    def splitHand(self, p1hand, deck, house):
        splithand = p1hand.hand.pop()
        while len(p1hand.hand) < 2:
            drawCard = deck.dealCard(house)
            p1hand.hand.append(drawCard)
            drawCard = deck.dealCard(house)
            splithand.append(drawCard)
        print(splithand)
