class Results:

    def __init__(self, game):
        self.game = game

    def determineWinner(self, player, dealer):
        if len(player.hand) == 2 and len(dealer.hand) == 2 and player.score == dealer.score:
            self.push()
        elif len(dealer.hand) == 2 and dealer.score == 21:
            self.dealerBlackjack()
        elif player.score == -1:
            self.playerSurrender(player)
        elif len(player.hand) == 2 and player.score == 21:
            self.playerBlackjack(player)
        elif player.score > 21:
            self.playerBusts(player)
        elif dealer.score > 21:
            self.dealerBusts(player)
        elif player.score > dealer.score:
            self.playerWin(player)
        elif dealer.score > player.score:
            self.dealerWin()
        elif player.score == dealer.score:
            self.push()
        elif player.score == -1:
            self.playerSurrender(player)

    def playerBlackjack(self, player):
        print("Blackjack!",player.name,"Wins!")
        self.game.outcome = self.game.outcome * 1.5

    def dealerBlackjack(self):
        print("Blackjack! House Wins!")
        self.game.outcome = self.game.outcome * -1

    def playerBusts(self, player):
        print(player.name, "Busts. House Wins!")
        self.game.outcome = self.game.outcome * -1

    def dealerBusts(self, player):
        print("Dealer Busts.",player.name,"Wins!")
        self.game.outcome = self.game.outcome * 1

    def playerSurrender(self, player):
        print(player.name, "Surrenders Hand.")
        self.game.outcome = self.game.outcome * -0.5

    def push(self):
        print("Push. No Winner.")
        self.game.outcome = self.game.outcome * 0

    def playerWin(self, player):
        print(player.name, "Wins!")
        self.game.outcome = self.game.outcome * 1

    def dealerWin(self):
        print("House Wins!")
        self.game.outcome = self.game.outcome * -1