class DealerHand:

    def __init__(self):
        self.hand = []

    def buildHand(self, drawCard):
        self.hand.append(drawCard)

    def hideHoleCard(self):
        holeCard = self.hand[1]
        self.hand[1] = ["***************"]
        return holeCard

    def showHand(self, holeCard):
        self.hand[1] = holeCard