class Player:

    def __init__(self):
        self.name = None
        self.cash = 0

    def obtainName(self):
        nameInput = input("Please enter your name: ")
        self.name = nameInput

    def startingCash(self):
        self.cash = self.cash + 1000