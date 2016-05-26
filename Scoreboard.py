class Scoreboard:

    def __init__(self, game):
        self.game = game

    def placeBet(self, cash):
        int(cash)
        while cash > 0:
            try:
                wager = int(input("Please place your bet: "))
            except ValueError:
                print("Please enter a valid amount:")
                continue
            if wager > cash:
                print("Bet cannot exceed available funds.")
            if wager <= cash:
                print("Bet Accepted.  Funds $", cash - wager, "   Bet $", wager)
                return wager
        if cash <= 0:
            print("You are out of funds.")
            self.game.newGame = True

    def updateCash(self, outcome, cash, wager):
        int(cash)
        cash = cash + wager * outcome
        return cash