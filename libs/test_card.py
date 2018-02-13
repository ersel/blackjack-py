import unittest
from libs.card import Card

class TestCard(unittest.TestCase):
    numerics = list(range(1, 10))
    valid_cards = [str(i) for i in numerics] + ['K', 'Q', 'J', 'A']

    def test_create_valid_cards(self):
        for card in TestCard.valid_cards:
            new_card = Card(card)
            self.assertIsInstance(new_card, Card)

    def test_create_invalid_card(self):
        invalid_card = 'E'
        with self.assertRaises(ValueError):
            new_card = Card(invalid_card)

    def test_card_values(self):
        for index, card in enumerate(TestCard.valid_cards):
            new_card_value = Card(card).get_value()
            if(index < 9):
                self.assertEqual(new_card_value, [index + 1])
            elif(index < 12):
                # K, Q, J == 10
                self.assertEqual(new_card_value, [10])
            else:
                # A == 1 or 11
                self.assertEqual(new_card_value, [1, 11])

