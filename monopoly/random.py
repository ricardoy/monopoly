import random


class Dice:
    def __init__(self, n):
        self.possible_values = [x for x in range(1, n+1)]

    def roll(self):
        return random.choice(self.possible_values)


class DecisionCoin:
    def __init__(self, probability):
        self.probability = probability

    def should_do(self):
        return random.uniform(0, 1) <= self.probability
