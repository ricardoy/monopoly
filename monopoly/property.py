class Property:
    def __init__(self, sell_value, rent_value):
        self.owner = None
        self.sell_value = sell_value
        self.rent_value = rent_value

    def has_owner(self):
        return self.owner is not None

    def evict_owner(self):
        self.owner = None