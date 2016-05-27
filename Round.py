class Round:

    def __init__(self, game):
        self.game = game

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
            elif action.lower() == "s":
                return
            elif action.lower() == "p" and len(player.hand) == 2 and player.hand[0][2] == player.hand[1][2]:
                self.split(player, deck, house)
            elif action.lower() == "d":
                self.double(player, deck, house)
                return
            elif action.lower() == "q":
                self.surrender(player)
                return
            else:
                print("Please enter a valid action")

    def hit(self, player, deck, house):
        drawCard = deck.dealCard(house)
        player.buildHand(drawCard)
        player.score = player.score + drawCard[2]
        print("Your Hand:", player.hand, "Total: ", player.score)

    def stand(self, player, dealer, deck, house):
        return

    def split(self, player, deck, house):
        print("Not supported at this time")

    def double(self, player, deck, house):
        drawCard = deck.dealCard(house)
        player.buildHand(drawCard)
        player.score = player.score + drawCard[2]
        print("Your Hand:", player.hand, "Total: ", player.score)
        if player.score > 21:
            self.checkForAces(player)
        self.game.outcome = 2

    def surrender(self, player):
        player.score = -1

    def checkForAces(self, player):
        for cards in player.hand:
            if cards[2] == 11:
                cards[2] = 1
                player.score = player.score - 10
                return

    def checkDealerHand(self, player, dealer, deck, house):
        dealer.playDealerHand(player, dealer, deck, house)