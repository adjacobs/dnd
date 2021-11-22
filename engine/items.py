class Item:
    def __init__(self, name,  item_type, description):
        self.name = name
        self.item_type = item_type
        self.description = description
        self._count = 0
        self.weight = 0

    def __str__(self):
        """
        Returns name and item description
        @return:
        """
        return f'{self.name} is a {self.item_type} with a count of {self.count}'

    def __repr__(self):
        """
        Return class info
        @return:
        """
        return f'Item: {self.name}, type {self.item_type}..'

    @property
    def count(self):
        """
        Return the count of the item.
        @return:
        """
        return self._count

    @count.setter
    def count(self, value):
        """
        Add or subtract value from count.
        @param value: Int
        @return:
        """
        self.count += value


class WeaponBasic(Item):
    def __init__(self, name, item_type, description):
        super().__init__(self, name, item_type, description)
        self.name = name
        self.item_type = item_type
        self.description = description
        self.prof = False
        self.attack_type = ''
        self.reach = 0
        self.range = [0, 0]
        self.damage = 0
        self.charges = 0
