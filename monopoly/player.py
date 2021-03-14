from abc import ABC, abstractmethod


INITIAL_BALANCE = 300


class AbstractPlayer(ABC):
    def __init__(self):
        self.balance = INITIAL_BALANCE
        self.properties = set()

    def remove_property(self, property):
        self.properties.remove(property)

    def should_buy(self, property_value) -> bool:
        """

        :param property_value:
        :return: True if the player should buy the property
        """
        if self.balance < property_value:
            return False
        else:
            return self._should_buy(property_value)

    @abstractmethod
    def _should_buy(self, property_value):
        pass

    @staticmethod
    @abstractmethod
    def label() -> str:
        pass

    def add_property(self, property):
        self.properties.add(property)

    def pay_and_update_balance(self, value):
        """

        :param value:
        :return: the actual value to be payed
        """
        if self.balance < value:
            value_to_pay = self.balance
            self.balance -= value
            return value_to_pay
        else:
            self.balance -= value
            return value

    def is_balance_negative(self) -> bool:
        return self.balance < 0

    def add_to_balance(self, value):
        self.balance += value

    def __str__(self):
        return type(self).label()


class ImpulsivePlayer(AbstractPlayer):
    def __init__(self):
        super().__init__()

    def _should_buy(self, property_value):
        return True

    @staticmethod
    def label():
        return 'Impulsivo'


class DemandingPlayer(AbstractPlayer):
    def __init__(self, min_property_value):
        super().__init__()
        self.min_property_value = min_property_value

    def _should_buy(self, property_value):
        return property_value > self.min_property_value

    @staticmethod
    def label():
        return 'Exigente'


class CautiousPlayer(AbstractPlayer):
    def __init__(self, acceptable_balance):
        super().__init__()
        self.acceptable_balance = acceptable_balance

    def _should_buy(self, property_value):
        return self.balance - property_value > self.acceptable_balance

    @staticmethod
    def label():
        return 'Cauteloso'


class RandomPlayer(AbstractPlayer):
    def __init__(self, coin):
        super().__init__()
        self.coin = coin

    def _should_buy(self, property_value):
        return self.coin.should_do()

    @staticmethod
    def label():
        return 'Aleatório'