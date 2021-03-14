from unittest import TestCase
from monopoly import ImpulsivePlayer


class PlayerTest(TestCase):
    def setUp(self) -> None:
        self.player = ImpulsivePlayer()
        self.player.balance = 10

    def test_player_should_buy_if_balance_allow_it(self):
        self.assertTrue(self.player.should_buy(9))
        self.assertTrue(self.player.should_buy(10))

    def test_player_should_not_buy_if_price_greater_than_balance(self):
        self.assertFalse(self.player.should_buy(11))
