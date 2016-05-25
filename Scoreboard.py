class Scoreboard:

    def __init__(self):
        self.pot = 0

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
                self.pot = self.pot + wager
                print("Bet Accepted.  Funds $", cash - wager, "   Bet $", self.pot)
                return wager
        if cash <= 0:
            print("You are out of funds.")
            wager = True
            return wager

    def updateCash(self, outcome, cash, wager):
        int(cash)
        cash = cash + wager * outcome
        return cash