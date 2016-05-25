class Dealer:

    def __init__(self):
        self.deal = 0

    def playDealerHand(self, p1hand, dealerhand, holeCard, handTotal, deck, house):
        dealerhand.showHand(holeCard)
        self.deal = dealerhand.hand[0][2] + dealerhand.hand[1][2]
        print("Your Hand:", p1hand.hand, "Total: ", handTotal)
        print("Dealer Hand:", dealerhand.hand, "Total: ", self.deal)
        while self.deal <= 16:
            drawCard = deck.dealCard(house)
            dealerhand.buildHand(drawCard)
            self.deal = self.deal + drawCard[2]
            print("Your Hand:", p1hand.hand, "Total: ", handTotal)
            print("Dealer Hand:", dealerhand.hand, "Total: ", self.deal)
            if self.deal > 21:
                self.checkForAces(dealerhand, self.deal)
                print("Your Hand:", p1hand.hand, "Total: ", handTotal)
                print("Dealer Hand:", dealerhand.hand, "Total: ", self.deal)
                continue
        dealerTotal = self.deal
        return dealerTotal

    def checkForAces(self, dealerhand, dealTotal):
        for cards in dealerhand.hand:
            if cards[2] == 11:
                cards[2] = 1
                self.deal = self.deal - 10
                return