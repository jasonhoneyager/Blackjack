from Player import Player
from Dealer import Dealer
from Deck import Deck
from Scoreboard import Scoreboard
from Round import Round
from Results import Results
from KeepPlaying import KeepPlaying

class Game:

    def __init__(self):
        self.player = None
        self.replayGame = None
        self.newGame = None
        self.outcome = 1

    def getPlayers(self):
        self.player = Player()
        self.player.obtainName()
        return self.player

    def getCash(self):
        self.player.getCash(self.player)

    def playGame(self):
        while self.newGame != False:
            self.newGame = False
            print("Welcome to Bender's Totally Legit and Not Rigged at All Blackjack Table.")
            print("You're not a cop, are you?  You have to tell me if you're a cop...")
            self.getPlayers()
            print("Welcome",self.player.name)
            self.player.startingCash()
            print(self.player.name, "has $",self.player.cash,"available")
            deck = Deck()
            dealer = Dealer()
            while self.replayGame != False:
                if len(deck.currentDeck) <= 10:
                    house = deck.newDeck()
                round = Round(self)
                results = Results(self)
                score = Scoreboard(self)
                wager = score.placeBet(self.player.cash)
                if self.newGame == True:
                    break
                round.startingHands(self.player, dealer, deck, house)
                round.takeAction(self.player, dealer, deck, house)
                if self.player.score <= 21 and self.player.score > 0:
                    round.checkDealerHand(self.player, dealer, deck, house)
                results.determineWinner(self.player, dealer)
                self.player.cash = score.updateCash(self.player.cash, wager)
                print(self.player.name, "has $", self.player.cash, "available")
                replay = KeepPlaying()
                replay.replayGame(self.player, dealer)
                self.replayGame = replay.playAgain
            if self.newGame == False:
                print("I don't need you.  I'll build my own casino.  With Blackjack... and hookers... Awww, forget it.")
            elif self.newGame == True:
                print("Oops, you're broke! ¯\_(ツ)_/¯")
                print("Come back when you have some money to lose. (\/)(;,,;)(\/)")