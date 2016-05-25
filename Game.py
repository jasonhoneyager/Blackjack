from Player import Player
from Deck import Deck
from Scoreboard import Scoreboard
from PlayerHand import PlayerHand
from DealerHand import DealerHand
from Round import Round
from KeepPlaying import KeepPlaying

class Game:

    def __init__(self):
        self.player = None
        self.replayGame = None
        self.newGame = None

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
            p1hand = PlayerHand()
            dealerhand = DealerHand()
            while self.replayGame != False:
                if len(deck.currentDeck) <= 10:
                    house = deck.newDeck()
                round = Round()
                score = Scoreboard()
                wager = score.placeBet(self.player.cash)
                if wager == True:
                    self.newGame = True
                    break
                holeCard = round.startingHands(p1hand, dealerhand, deck, house)
                outcome = round.takeAction(p1hand, dealerhand, deck, house, holeCard, self.player.name)
                self.player.cash = score.updateCash(outcome, self.player.cash, wager)
                print(self.player.name, "has $", self.player.cash, "available")
                replay = KeepPlaying()
                replay.replayGame()
                self.replayGame = replay.playAgain
            if self.newGame == False:
                print("I don't need you.  I'll build my own casino.  With Blackjack... and hookers... Awww, forget it.")
            elif self.newGame == True:
                print("Come back when you have some money to lose.")