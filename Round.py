from Dealer import Dealer
from Results import Results
class Round:

    def __init__(self):
        self.play1 = 0

    def startingHands(self, p1hand, dealerhand, deck, house):
        p1hand.hand = []
        dealerhand.hand = []
        while len(p1hand.hand) < 2:
            drawCard = deck.dealCard(house)
            p1hand.buildHand(drawCard)
            drawCard = deck.dealCard(house)
            dealerhand.buildHand(drawCard)
        self.play1 = p1hand.hand[0][2] + p1hand.hand[1][2]
        print("Your Hand:",p1hand.hand,"Total: ",self.play1)
        holeCard = dealerhand.hideHoleCard()
        print("Dealer Hand:", dealerhand.hand,"Total: ",dealerhand.hand[0][2])
        return holeCard

    def takeAction(self, p1hand, dealerhand, deck, house, holeCard, name):
        if self.play1 > 21:
            self.checkForAces(p1hand, self.play1)
            print("Your Hand:", p1hand.hand, "Total: ", self.play1)
            print("Dealer Hand:", dealerhand.hand, "Total: ", dealerhand.hand[0][2])
        while self.play1 <= 21:
            print("H-Hit, S-Stand, P-Split, D-Double, Q-Surrender")
            action = input("What would you like to do? ")
            if action.lower() == "h":
                self.hit(p1hand, deck, house)
                if self.play1 > 21:
                    self.checkForAces(p1hand, self.play1)
                    if self.play1 <= 21:
                        print("Your Hand:", p1hand.hand, "Total: ", self.play1)
                        print("Dealer Hand:", dealerhand.hand, "Total: ", dealerhand.hand[0][2])
                        continue
                    results = Results()
                    outcome = results.playerBusts(name)
                    return outcome
            elif action.lower() == "s":
                outcome = self.stand(p1hand, dealerhand, holeCard, self.play1, deck, house, name)
                return outcome
            elif action.lower() == "p" and len(p1hand.hand) == 2 and p1hand.hand[0][2] == p1hand.hand[1][2]:
                self.split(p1hand, deck, house)
            elif action.lower() == "d":
                outcome = self.double(p1hand, dealerhand, holeCard, self.play1, deck, house, name)
                return outcome
            elif action.lower() == "q":
                outcome = self.surrender(p1hand, dealerhand, deck, house, holeCard, name)
                return outcome
            else:
                print("Please enter a valid action")

    def hit(self, p1hand, deck, house):
        drawCard = deck.dealCard(house)
        p1hand.buildHand(drawCard)
        self.play1 = self.play1 + drawCard[2]
        print("Your Hand:", p1hand.hand, "Total: ", self.play1)

    def stand(self, p1hand, dealerhand, holeCard, handTotal, deck, house, name):
        dealer = Dealer()
        dealerTotal = dealer.playDealerHand(p1hand, dealerhand, holeCard, handTotal, deck, house)
        results = Results()
        outcome = results.determineWinner(p1hand, dealerhand, handTotal, dealerTotal, name)
        return outcome

    def split(self, p1hand, deck, house):
        print("Not supported at this time")

    def double(self, p1hand, dealerhand, holeCard, handTotal, deck, house, name):
        drawCard = deck.dealCard(house)
        p1hand.buildHand(drawCard)
        self.play1 = handTotal + drawCard[2]
        print("Your Hand:", p1hand.hand, "Total: ", self.play1)
        if self.play1 > 21:
            results = Results()
            outcome = results.playerBusts(name)
            return outcome * 2
        dealer = Dealer()
        dealerTotal = dealer.playDealerHand(p1hand, dealerhand, holeCard, self.play1, deck, house)
        results = Results()
        outcome = results.determineWinner(self.play1, dealerTotal, name)
        return outcome * 2

    def surrender(self, p1hand, dealerhand, deck, house, holeCard, name):
        results = Results()
        outcome = results.playerSurrender(p1hand, dealerhand, deck, house, holeCard, name)
        return outcome

    def checkForAces(self, p1hand, handTotal):
        for cards in p1hand.hand:
            if cards[2] == 11:
                cards[2] = 1
                self.play1 = self.play1 - 10
                return