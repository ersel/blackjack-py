import unittest
from libs.deck import Deck

class TestDeck(unittest.TestCase):

    def test_create_decks(self):
        # invalid deck
        with self.assertRaises(ValueError):
            invalid_deck = Deck(0)

        # single deck of 52 cards
        single_deck = Deck(1)
        self.assertEqual(len(single_deck.cards), 52)

        # Atlantic City: 8 decks
        atlantic_deck = Deck(8)
        self.assertEqual(len(atlantic_deck.cards), 8 * 52)

    def test_pick_cards(self):
        single_deck = Deck(1)
        single_deck.shuffle()
        for i in range(52):
            picked_card = single_deck.pick()

        # 52th try should return None
        last_try = single_deck.pick()
        self.assertEqual(last_try, None)

    def test_reset_deck(self):
        single_deck = Deck(1)
        for i in range(10):
            single_deck.pick()

        # picked 10 cards from a single deck
        # expecting to see 42 cards left
        self.assertEqual(len(single_deck.cards), 42)

        # reset deck we should see 52 cards again
        single_deck.reset()
        self.assertEqual(len(single_deck.cards), 52)
