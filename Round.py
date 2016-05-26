from Dealer import Dealer
from Results import Results
class Round:

    def __init__(self):
        self.play1 = 0

    def startingHands(self, player, dealer, deck, house):
        player.hand = []
        dealer.hand = []
        while len(player.hand) < 2:
            drawCard = deck.dealCard(house)
            player.buildHand(drawCard)
            drawCard = deck.dealCard(house)
            dealer.buildHand(drawCard)
        self.play1 = player.hand[0][2] + player.hand[1][2]
        print("Your Hand:",player.hand,"Total: ",self.play1)
        dealer.hideHoleCard()
        print("Dealer Hand:", dealer.hand,"Total: ",dealer.hand[0][2])

    def takeAction(self, player, dealer, deck, house):
        if self.play1 > 21:
            self.checkForAces(player, self.play1)
            print("Your Hand:", player.hand, "Total: ", self.play1)
            print("Dealer Hand:", dealer.hand, "Total: ", dealer.hand[0][2])
        while self.play1 <= 21:
            print("H-Hit, S-Stand, P-Split, D-Double, Q-Surrender")
            action = input("What would you like to do? ")
            if action.lower() == "h":
                self.hit(player, deck, house)
                if self.play1 > 21:
                    self.checkForAces(player, self.play1)
                    if self.play1 <= 21:
                        print("Your Hand:", player.hand, "Total: ", self.play1)
                        print("Dealer Hand:", dealer.hand, "Total: ", dealer.hand[0][2])
                        continue
                    results = Results()
                    outcome = results.playerBusts(player)
                    return outcome
            elif action.lower() == "s":
                outcome = self.stand(player, dealer, self.play1, deck, house)
                return outcome
            elif action.lower() == "p" and len(player.hand) == 2 and player.hand[0][2] == player.hand[1][2]:
                self.split(player, deck, house)
            elif action.lower() == "d":
                outcome = self.double(player, dealer, self.play1, deck, house)
                return outcome
            elif action.lower() == "q":
                outcome = self.surrender(player, dealer, deck, house)
                return outcome
            else:
                print("Please enter a valid action")

    def hit(self, player, deck, house):
        drawCard = deck.dealCard(house)
        player.buildHand(drawCard)
        self.play1 = self.play1 + drawCard[2]
        print("Your Hand:", player.hand, "Total: ", self.play1)

    def stand(self, player, dealer, handTotal, deck, house):
        dealerTotal = dealer.playDealerHand(player, dealer, handTotal, deck, house)
        results = Results()
        outcome = results.determineWinner(player, dealer, handTotal, dealerTotal)
        return outcome

    def split(self, player, deck, house):
        print("Not supported at this time")

    def double(self, player, dealer, handTotal, deck, house):
        drawCard = deck.dealCard(house)
        player.buildHand(drawCard)
        self.play1 = handTotal + drawCard[2]
        print("Your Hand:", player.hand, "Total: ", self.play1)
        if self.play1 > 21:
            results = Results()
            outcome = results.playerBusts(player)
            return outcome * 2
        dealerTotal = dealer.playDealerHand(player, dealer, self.play1, deck, house)
        results = Results()
        outcome = results.determineWinner(player, dealer, self.play1, dealerTotal)
        return outcome * 2

    def surrender(self, player, dealer, deck, house):
        results = Results()
        outcome = results.playerSurrender(player, dealer, deck, house)
        return outcome

    def checkForAces(self, player, handTotal):
        for cards in player.hand:
            if cards[2] == 11:
                cards[2] = 1
                self.play1 = self.play1 - 10
                return