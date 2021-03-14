from unittest import TestCase
from monopoly import ImpulsivePlayer
from monopoly import Property
from monopoly import Game
from monopoly import Dice


class AlwaysRollOneDice(Dice):
    def __init__(self):
        super().__init__(6)

    def roll(self):
        return 1


class GameTest(TestCase):

    def test_single_player_game_should_finish_at_first_turn(self):
        p1 = ImpulsivePlayer()
        board = [Property(sell_value=1, rent_value=1), Property(sell_value=2, rent_value=2)]
        game = Game(players=[p1],
                         dice=AlwaysRollOneDice(),
                         board=board)

        self.assertEqual(game.winner(), p1)

    def test_game_should_time_out(self):
        p1 = ImpulsivePlayer()
        p2 = ImpulsivePlayer()
        board = [Property(sell_value=1, rent_value=1), Property(sell_value=2, rent_value=2)]
        game = Game(players=[p1, p2],
                         dice=AlwaysRollOneDice(),
                         board=board)

        game.run_game()

        self.assertTrue(game.time_out())

    def test_game_should_end(self):
        p1 = ImpulsivePlayer()
        p2 = ImpulsivePlayer()
        board = [Property(sell_value=300, rent_value=301)]
        game = Game(players=[p1, p2],
                    dice=AlwaysRollOneDice(),
                    board=board)

        game.run_game()

        self.assertEqual(p1, game.winner())

