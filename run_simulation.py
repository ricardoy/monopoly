import random
import argparse
from monopoly import DecisionCoin, Dice
from monopoly import ImpulsivePlayer, DemandingPlayer, CautiousPlayer, RandomPlayer
from monopoly import Game
from monopoly import Property


PLAYERS_TYPE = {ImpulsivePlayer, DemandingPlayer, CautiousPlayer, RandomPlayer}
TOTAL_SIMULATIONS = 300


def generate_properties(n, min_sell, max_sell, min_rent, max_rent):
    board = []

    for _ in range(n):
        board.append(Property(sell_value=random.randint(min_sell, max_sell),
                              rent_value=random.randint(min_rent, max_rent)))

    return board


def build_game(min_sell, max_sell, min_rent, max_rent):
    players = [
        ImpulsivePlayer(),
        DemandingPlayer(50),
        CautiousPlayer(80),
        RandomPlayer(DecisionCoin(.5))
    ]
    random.shuffle(players)
    board = generate_properties(20, min_sell, max_sell, min_rent, max_rent)
    dice = Dice(6)
    return Game(players=players, board=board, dice=dice)


def run_simulation(min_sell, max_sell, min_rent, max_rent):
    assert(min_sell <= max_sell)
    assert(min_rent <= max_rent)
    assert(min_sell > 0)
    assert(max_sell > 0)
    assert(min_rent > 0)
    assert(max_rent > 0)

    time_out = 0
    turns_per_game = []
    wins_by_player = {player_type: 0 for player_type in PLAYERS_TYPE}

    for _ in range(TOTAL_SIMULATIONS):
        game = build_game(min_sell, max_sell, min_rent, max_rent)
        game.run_game()

        if game.total_remaining_players() != 1:
            time_out += 1

        turns_per_game.append(game.turns)

        winner = game.winner()
        wins_by_player[type(winner)] += 1

    print('Total de partidas que terminaram em time out: {}'.format(time_out))
    print('Média de turnos por partida: {:.2f}'.format(sum(turns_per_game) / TOTAL_SIMULATIONS))

    print('\nVitórias por tipo')
    for pt in PLAYERS_TYPE:
        print('{}: {:.2f}'.format(pt.label(), wins_by_player[pt] / TOTAL_SIMULATIONS * 100))

    max_number_of_wins = max(wins_by_player.values())
    most_wins_players = [player.label() for player, wins in wins_by_player.items() if wins == max_number_of_wins]
    print('\nComportamentos com mais vitórias: {}'.format(', '.join(most_wins_players)))



if __name__ == '__main__':
    parser = argparse.ArgumentParser('Monopoly Simulation')
    parser.add_argument('--min-sell', help='Minimum sell value', type=int, default=50)
    parser.add_argument('--max-sell', help='Maximum sell value', type=int, default=90)
    parser.add_argument('--min-rent', help='Minimum rent value', type=int, default=100)
    parser.add_argument('--max-rent', help='Maximum rent value', type=int, default=250)

    args = parser.parse_args()

    run_simulation(args.min_sell, args.max_sell, args.min_rent, args.max_rent)