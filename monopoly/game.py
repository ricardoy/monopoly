from typing import List
from monopoly import AbstractPlayer, Property, Dice


TOTAL_TURNS = 1000


class Game:
    def __init__(self, players: List[AbstractPlayer], board: List[Property], dice: Dice):
        self.turns = 0
        self.current_player = 0
        self.players = players
        self.board = board
        self.player_position = {player: 0 for player in self.players}
        self.dice = dice

    def total_remaining_players(self):
        return len(self.players)

    def _update_current_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def process_turn(self) -> None:
        """

        :return:
        """
        player = self.players[self.current_player]
        current_position = self.player_position[player]
        new_position = (current_position + self.dice.roll()) % len(self.board)
        self.player_position[player] = new_position
        if new_position < current_position:
            player.add_to_balance(100)

        current_property = self.board[new_position]

        if current_property.has_owner():
            if current_property.owner != player:
                value_to_pay = player.pay_and_update_balance(current_property.rent_value)
                current_property.owner.add_to_balance(value_to_pay)
                if player.is_balance_negative():
                    for property in player.properties:
                        property.evict_owner()
                    self.players = [player for player in self.players if not player.is_balance_negative()]
        else:
            if player.should_buy(current_property.sell_value):
                player.add_property(current_property)
                current_property.owner = player

        self._update_current_player()

    def run_game(self) -> None:
        """
        Run the game
        :return: None
        """
        while True:
            self.turns += 1
            self.process_turn()

            if self.turns == TOTAL_TURNS or len(self.players) == 1:
                return

    def winner(self):
        """

        :return: the winner, if the game ended; otherwise, returns None.
        """
        if self.turns == TOTAL_TURNS:
            max_balance = max([p.balance for p in self.players])
            for p in self.players:
                if p.balance == max_balance:
                    return p
        elif len(self.players) == 1:
            return self.players[0]
        else:
            return None

    def time_out(self):
        return self.turns == TOTAL_TURNS and len(self.players) != 1

    def __str__(self):
        s1 = '---\n'
        for p in self.players:
            s1 += '{}: balance: {} board index: {}\n'.format(type(p).label(), p.balance, self.player_position[p])
        s1 += '\n'

        sell = ' '.join(['{: 4}'.format(property.sell_value) for property in self.board]) + '\n'
        rent = ' '.join(['{: 4}'.format(property.rent_value) for property in self.board]) + '\n'
        owner = ' '.join([str(property.owner)[:4] for property in self.board]) + '\n'

        return s1 + sell + rent + owner