import unittest
from libs.card import Card
from libs.hand import Hand

class TestHand(unittest.TestCase):

    def test_dealt_card(self):
        new_hand = Hand()
        a_card = Card('Q')

        self.assertEqual(len(new_hand.cards), 0)
        new_hand.dealt_card(a_card)
        self.assertEqual(len(new_hand.cards), 1)

        with self.assertRaises(ValueError):
            new_hand.dealt_card('not a card')

    def test_calculate_soft(self):
        hand = Hand()
        multiple_aces = ['A', 'A', 'A', '1', '2', '3']
        for card in multiple_aces:
            hand.dealt_card(Card(card))

        self.assertEqual(hand.calculate_soft(), 19)

        single_ace = ['J', 'A']
        hand = Hand()
        for card in single_ace:
            hand.dealt_card(Card(card))
        self.assertEqual(hand.calculate_soft(), 21)

        no_aces = ['5', '6', '9']
        hand = Hand()
        for card in no_aces:
            hand.dealt_card(Card(card))
        self.assertEqual(hand.calculate_soft(), 20)

    def test_calculate_hard(self):
        hand = Hand()
        multiple_aces = ['A', 'A', 'A', '1', '2', '3']
        for card in multiple_aces:
            hand.dealt_card(Card(card))

        self.assertEqual(hand.calculate_hard(), 9)

        single_ace = ['J', 'A']
        hand = Hand()
        for card in single_ace:
            hand.dealt_card(Card(card))
        self.assertEqual(hand.calculate_hard(), 11)

        no_aces = ['5', '6', '9']
        hand = Hand()
        for card in no_aces:
            hand.dealt_card(Card(card))
        self.assertEqual(hand.calculate_hard(), 20)

    def test_is_finalized(self):
        hand = Hand()
        blackjack = ['A', 'Q']
        for card in blackjack:
            hand.dealt_card(Card(card))
        self.assertEqual(hand.is_finalized(), True)

        hand = Hand()
        soft_bust_hard_blackjack = ['A', 'A', 'Q', '9']
        for card in soft_bust_hard_blackjack:
            hand.dealt_card(Card(card))
        self.assertEqual(hand.is_finalized(), True)

        hand = Hand()
        soft_bust_hard_under_21 = ['A', 'A', 'Q', '8']
        for card in soft_bust_hard_under_21:
            hand.dealt_card(Card(card))
        self.assertEqual(hand.is_finalized(), False)

        hand = Hand()
        soft_bust_hard_bust = ['A', 'A', 'Q', 'Q']
        for card in soft_bust_hard_bust:
            hand.dealt_card(Card(card))
        self.assertEqual(hand.is_finalized(), True)

    def test_is_standing(self):
        hand = Hand()
        hand.stand()
        self.assertEqual(hand.is_finalized(), True)

    def test_split_hand(self):
        hand = Hand()
        splitable = ['A', 'A']
        for card in splitable:
            hand.dealt_card(Card(card))
        cards = hand.split()
        self.assertEqual(len(cards), 2)

        late_to_split = ['A', 'A', 'A']
        for card in late_to_split:
            hand.dealt_card(Card(card))
        cards = hand.split()
        self.assertEqual(len(cards), 0)

        non_splitable = ['A', 'Q']
        for card in non_splitable:
            hand.dealt_card(Card(card))
        cards = hand.split()
        self.assertEqual(len(cards), 0)

    def test_hand_options(self):
        hand = Hand()
        surrender = ['1', '2']
        for card in surrender:
            hand.dealt_card(Card(card))
        options = hand.get_options(Card('1'))
        self.assertListEqual(options, ['HIT', 'STAND', 'SURRENDER'])

        hand = Hand()
        splitable = ['1', '1']
        for card in splitable:
            hand.dealt_card(Card(card))
        options = hand.get_options(Card('1'))
        self.assertListEqual(options, ['HIT', 'STAND', 'SURRENDER', 'SPLIT'])

        hand = Hand()
        insurable = ['1', '2']
        for card in insurable:
            hand.dealt_card(Card(card))
        options = hand.get_options(Card('A'))
        self.assertListEqual(options, ['HIT', 'STAND', 'SURRENDER', 'INSURANCE'])

        hand = Hand(is_split=True)
        not_insurable = ['1', '2']
        for card in not_insurable:
            hand.dealt_card(Card(card))
        options = hand.get_options(Card('A'))
        self.assertListEqual(options, ['HIT', 'STAND', 'SURRENDER'])

        hand = Hand()
        not_initial_hand = ['1', '2', '3']
        for card in not_initial_hand:
            hand.dealt_card(Card(card))
        options = hand.get_options(Card('A'))
        self.assertListEqual(options, ['HIT', 'STAND'])

        hand = Hand(is_split=True)
        double = ['1', '2', '8']
        for card in double:
            hand.dealt_card(Card(card))
        options = hand.get_options(Card('A'))
        self.assertListEqual(options, ['HIT', 'STAND', 'DOUBLE'])
