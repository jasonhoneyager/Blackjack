class Card:

    def __init__(self):
        self.suit = None
        self.value = None
        self.face = None

    def determineCardType(self, drawCard):
        if drawCard <= 13:
            if drawCard == 1:
                 [self.face, self.value, self.suit] = ["A", 11, "Spades"]
            elif drawCard <= 10:
                  [self.face, self.value, self.suit] = [drawCard, drawCard, "Spades"]
            elif drawCard == 11:
                [self.face, self.value, self.suit] = ["J", 10, "Spades"]
            elif drawCard == 12:
                [self.face, self.value, self.suit] = ["Q", 10, "Spades"]
            elif drawCard == 13:
                [self.face, self.value, self.suit] = ["K", 10, "Spades"]
        elif drawCard >=14 and drawCard <= 26:
            if drawCard == 14:
                [self.face, self.value, self.suit] = ["A", 11, "Hearts"]
            elif drawCard <= 23:
                 [self.face, self.value, self.suit] = [drawCard - 13, drawCard - 13, "Hearts"]
            elif drawCard == 24:
                [self.face, self.value, self.suit] = ["J", 10, "Hearts"]
            elif drawCard == 25:
                [self.face, self.value, self.suit] = ["Q", 10, "Hearts"]
            elif drawCard == 26:
                [self.face, self.value, self.suit] = ["K", 10, "Hearts"]
        elif drawCard >= 27 and drawCard <= 39:
            if drawCard == 27:
                [self.face, self.value, self.suit] = ["A", 11, "Clubs"]
            elif drawCard <= 36:
                [self.face, self.value, self.suit] = [drawCard - 26, drawCard - 26, "Clubs"]
            elif drawCard == 37:
                [self.face, self.value, self.suit] = ["J", 10, "Clubs"]
            elif drawCard == 38:
                [self.face, self.value, self.suit] = ["Q", 10, "Clubs"]
            elif drawCard == 39:
                [self.face, self.value, self.suit] = ["K", 10, "Clubs"]
        elif drawCard >= 40 and drawCard <= 52:
            if drawCard == 40:
                [self.face, self.value, self.suit] = ["A", 11, "Diamonds"]
            elif drawCard <= 49:
                [self.face, self.value, self.suit] = [drawCard - 39, drawCard - 39, "Diamonds"]
            elif drawCard == 50:
                [self.face, self.value, self.suit] = ["J", 10, "Diamonds"]
            elif drawCard == 51:
                [self.face, self.value, self.suit] = ["Q", 10, "Diamonds"]
            elif drawCard == 52:
                [self.face, self.value, self.suit] = ["K", 10, "Diamonds"]