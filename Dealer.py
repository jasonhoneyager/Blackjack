class Dealer:

    def __init__(self):
        self.hand = []
        self.hole = []
        self.score = 0

    def playDealerHand(self, player, dealer, deck, house):
        dealer.showHand()
        self.score = self.hand[0][2] + self.hand[1][2]
        print("Your Hand:", player.hand, "Total: ", player.score)
        print("Dealer Hand:", self.hand, "Total: ", self.score)
        if len(player.hand) == 2 and player.score == 21 and self.score != 21:
            dealerTotal = self.score
            return dealerTotal
        while self.score <= 16:
            drawCard = deck.dealCard(house)
            self.buildHand(drawCard)
            self.score = self.score + drawCard[2]
            print("Your Hand:", player.hand, "Total: ", player.score)
            print("Dealer Hand:", self.hand, "Total: ", self.score)
            if self.score > 21:
                self.checkForAces(player)
                continue
        dealerTotal = self.score
        return dealerTotal

    def checkForAces(self, player):
        for cards in self.hand:
            if cards[2] == 11:
                cards[2] = 1
                self.score = self.score - 10
                print("Your Hand:", player.hand, "Total: ", player.score)
                print("Dealer Hand:", self.hand, "Total: ", self.score)
                return

    def buildHand(self, drawCard):
        self.hand.append(drawCard)

    def hideHoleCard(self):
        self.hole = self.hand[1]
        self.hand[1] = ["***************"]

    def showHand(self):
        self.hand[1] = self.hole