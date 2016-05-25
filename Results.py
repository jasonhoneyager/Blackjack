class Results:

    def __init__(self):
        return

    def determineWinner(self, p1hand, dealerhand, handTotal, dealerTotal, name):
        if len(p1hand.hand) == 2 and len(dealerhand.hand) == 2 and handTotal == dealerTotal:
            print("Push.  No Winner.")
            outcome = 0
            return outcome
        elif len(dealerhand.hand) == 2 and dealerTotal == 21:
            outcome = self.dealerBlackjack()
            return outcome
        elif len(p1hand.hand) == 2 and handTotal == 21:
            outcome = self.playerBlackjack(name)
            return outcome
        elif dealerTotal > 21:
            print("Dealer Busts.",name,"Wins!")
            outcome = 1
            return outcome
        elif handTotal > dealerTotal:
            print(name,"Wins!")
            outcome = 1
            return outcome
        elif dealerTotal > handTotal:
            print("House Wins!")
            outcome = -1
            return outcome
        elif handTotal == dealerTotal:
            print("Push.  No Winner.")
            outcome = 0
            return outcome

    def playerBlackjack(self, name):
        print("Blackjack!",name,"Wins!")
        outcome = 1.5
        return outcome

    def dealerBlackjack(self):
        print("Blackjack! House Wins!")
        outcome = -1
        return outcome

    def playerBusts(self, name):
        print(name, "Busts.  House Wins!")
        outcome = -1
        return outcome

    def playerSurrender(self, p1hand, dealerhand, deck, house, holeCard, name):
        print(name, "Surrenders Hand.")
        outcome = -0.5
        return outcome