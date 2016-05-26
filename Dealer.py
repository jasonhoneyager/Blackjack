class Dealer:

    def __init__(self):
        self.deal = 0
        self.hand = []
        self.hole = []

    def playDealerHand(self, player, dealer, handTotal, deck, house):
        dealer.showHand()
        self.deal = self.hand[0][2] + self.hand[1][2]
        print("Your Hand:", player.hand, "Total: ", handTotal)
        print("Dealer Hand:", self.hand, "Total: ", self.deal)
        while self.deal <= 16:
            drawCard = deck.dealCard(house)
            self.buildHand(drawCard)
            self.deal = self.deal + drawCard[2]
            print("Your Hand:", player.hand, "Total: ", handTotal)
            print("Dealer Hand:", self.hand, "Total: ", self.deal)
            if self.deal > 21:
                self.checkForAces(player, self.hand, self.deal, handTotal)
                continue
        dealerTotal = self.deal
        return dealerTotal

    def checkForAces(self, player, dealer, dealTotal, handTotal):
        for cards in self.hand:
            if cards[2] == 11:
                cards[2] = 1
                self.deal = self.deal - 10
                print("Your Hand:", player.hand, "Total: ", handTotal)
                print("Dealer Hand:", self.hand, "Total: ", self.deal)
                return

    def buildHand(self, drawCard):
        self.hand.append(drawCard)

    def hideHoleCard(self):
        self.hole = self.hand[1]
        self.hand[1] = ["***************"]

    def showHand(self):
        self.hand[1] = self.hole