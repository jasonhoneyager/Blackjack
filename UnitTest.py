import unittest
import sys
import mock

from Player import Player
from Dealer import Dealer
from Card import Card
from Deck import Deck
from Scoreboard import Scoreboard
from DealCard import DealCard
from Results import Results
from KeepPlaying import KeepPlaying

class UnitTest(unittest.TestCase):

#Player Tests#####################

#Dealer Tests#####################

#Card Tests#######################
    def test_determine_card_type(self):
        card = Card()
        drawCard = 1
        card.determineCardType(drawCard)
        self.assertEqual([card.face, card.value, card.suit], ["A", 11, "Spades"])

#Deck Tests#######################

#Scoreboard Tests#################
    def test_wager_input_valid(self):
        return

    def test_wager_input_invalid(self):
        return
#PlayerHand Tests#################

#DealCard Tests###################

#Results Tests####################
    def test_determine_winner_win(self):
        results = Results()
        player =
        dealer =
        results.determineWinner(player, dealer)
        self.assertEqual(outcome, 1)

    def test_determine_winner_lose(self):
        results = Results()
        player =
        dealer =
        results.determineWinner(player, dealer)
        self.assertEqual(outcome, -1)

    def test_determine_winner_push(self):
        results = Results()
        player =
        dealer =
        results.determineWinner(player, dealer)
        self.assertEqual(outcome, 0)

    def test_determine_winner_blackjack_win(self):
        results = Results()
        player =
        dealer =
        results.determineWinner(player, dealer)
        self.assertEqual(outcome, 1.5)

    def test_determine_winner_blackjack_lose(self):
        results = Results()
        player =
        dealer =
        results.determineWinner(player, dealer)
        self.assertEqual(outcome, -1)

    def test_determine_winner_blackjack_push(self):
        results = Results()
        player =
        dealer =
        results.determineWinner(player, dealer)
        self.assertEqual(outcome, 0)

    def test_determine_winner_dealer_bust(self):
        results = Results()
        player =
        dealer =
        results.determineWinner(player, dealer)
        self.assertEqual(outcome, 1)
#KeepPlaying Tests################

    def main():
        unittest.main()

if __name__ == "__main__":
    main()