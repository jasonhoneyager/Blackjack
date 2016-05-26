class Results:

    def __init__(self):
        return

    def determineWinner(self, player, dealer):
        if len(player.hand) == 2 and len(dealer.hand) == 2 and player.score == dealer.score:
            print("Push.  No Winner.")
            outcome = 0
            return outcome
        elif len(dealer.hand) == 2 and dealer.score == 21:
            outcome = self.dealerBlackjack()
            return outcome
        elif len(player.hand) == 2 and player.score == 21:
            outcome = self.playerBlackjack(player)
            return outcome
        elif dealer.score > 21:
            print("Dealer Busts.",player.name,"Wins!")
            outcome = 1
            return outcome
        elif player.score > dealer.score:
            print(player.name,"Wins!")
            outcome = 1
            return outcome
        elif dealer.score > player.score:
            print("House Wins!")
            outcome = -1
            return outcome
        elif player.score == dealer.score:
            print("Push.  No Winner.")
            outcome = 0
            return outcome

    def playerBlackjack(self, player):
        print("Blackjack!",player.name,"Wins!")
        outcome = 1.5
        return outcome

    def dealerBlackjack(self):
        print("Blackjack! House Wins!")
        outcome = -1
        return outcome

    def playerBusts(self, player):
        print(player.name, "Busts.  House Wins!")
        outcome = -1
        return outcome

    def playerSurrender(self, player, dealer, deck, house):
        print(player.name, "Surrenders Hand.")
        outcome = -0.5
        return outcome