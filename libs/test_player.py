import unittest
from libs.player import Player

class TestPlayer(unittest.TestCase):

    def test_deposit(self):
        player = Player(5000)
        player.deposit(100)
        self.assertEqual(player.balance, 5100)

        with self.assertRaises(ValueError):
            player.deposit(-100)

    def test_stake(self):
        player = Player(100)
        self.assertEqual(player.balance, 100)
        self.assertEqual(player.staked, 0)
        player.stake(50)
        self.assertEqual(player.balance, 50)
        self.assertEqual(player.staked, 50)

        with self.assertRaises(ValueError):
            player.stake(-1)

        with self.assertRaises(ValueError):
            player.stake(51)

    def test_insure(self):
        player = Player(100)
        self.assertEqual(player.balance, 100)
        self.assertEqual(player.staked, 0)
        player.stake(50)
        player.insure() # insure for 25
        self.assertEqual(player.balance, 25)
        self.assertEqual(player.staked, 50)
        self.assertEqual(player.insured, True)

        with self.assertRaises(ValueError):
            player.insure() # already insured

        player = Player(100)
        player.stake(100)
        with self.assertRaises(ValueError):
            player.insure() # insufficient funds to insure


