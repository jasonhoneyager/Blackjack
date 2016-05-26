from Results import Results
class Round:

    def __init__(self):
        return

    def startingHands(self, player, dealer, deck, house):
        player.hand = []
        dealer.hand = []
        while len(player.hand) < 2:
            drawCard = deck.dealCard(house)
            player.buildHand(drawCard)
            drawCard = deck.dealCard(house)
            dealer.buildHand(drawCard)
        player.score = player.hand[0][2] + player.hand[1][2]
        print("Your Hand:",player.hand,"Total: ",player.score)
        dealer.hideHoleCard()
        print("Dealer Hand:", dealer.hand,"Total: ",dealer.hand[0][2])

    def takeAction(self, player, dealer, deck, house):
        if player.score > 21:
            self.checkForAces(player)
            print("Your Hand:", player.hand, "Total: ", player.score)
            print("Dealer Hand:", dealer.hand, "Total: ", dealer.hand[0][2])
        while player.score <= 21:
            print("H-Hit, S-Stand, P-Split, D-Double, Q-Surrender")
            action = input("What would you like to do? ")
            if action.lower() == "h":
                self.hit(player, deck, house)
                if player.score > 21:
                    self.checkForAces(player)
                    if player.score <= 21:
                        print("Your Hand:", player.hand, "Total: ", player.score)
                        print("Dealer Hand:", dealer.hand, "Total: ", dealer.hand[0][2])
                        continue
                    results = Results()
                    outcome = results.playerBusts(player)
                    return outcome
            elif action.lower() == "s":
                outcome = self.stand(player, dealer, deck, house)
                return outcome
            elif action.lower() == "p" and len(player.hand) == 2 and player.hand[0][2] == player.hand[1][2]:
                self.split(player, deck, house)
            elif action.lower() == "d":
                outcome = self.double(player, dealer, deck, house)
                return outcome
            elif action.lower() == "q":
                outcome = self.surrender(player, dealer, deck, house)
                return outcome
            else:
                print("Please enter a valid action")

    def hit(self, player, deck, house):
        drawCard = deck.dealCard(house)
        player.buildHand(drawCard)
        player.score = player.score + drawCard[2]
        print("Your Hand:", player.hand, "Total: ", player.score)

    def stand(self, player, dealer, deck, house):
        dealerTotal = dealer.playDealerHand(player, dealer, deck, house)
        results = Results()
        outcome = results.determineWinner(player, dealer)
        return outcome

    def split(self, player, deck, house):
        print("Not supported at this time")

    def double(self, player, dealer, deck, house):
        drawCard = deck.dealCard(house)
        player.buildHand(drawCard)
        player.score = player.score + drawCard[2]
        print("Your Hand:", player.hand, "Total: ", player.score)
        if player.score > 21:
            results = Results()
            outcome = results.playerBusts(player)
            return outcome * 2
        dealerTotal = dealer.playDealerHand(player, dealer, deck, house)
        results = Results()
        outcome = results.determineWinner(player, dealer)
        return outcome * 2

    def surrender(self, player, dealer, deck, house):
        results = Results()
        outcome = results.playerSurrender(player, dealer, deck, house)
        return outcome

    def checkForAces(self, player):
        for cards in player.hand:
            if cards[2] == 11:
                cards[2] = 1
                player.score = player.score - 10
                return