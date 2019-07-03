class Inventory:
    def __init__(self):
        self.copper = 0
        self.silver = 0
        self.gold = 0
        self.platinum = 0
        self.items = []
        self.weapons = []


class Weapon:

    def __init__(self):
        self.name = ''
        self.prof = False
        self.attack_type = ''
        self.reach = 0
        self.range = [0, 0]
        self.damage = 0
        self.damage_type = None
        self.weight = 0
        self.properties = []
        self.spells = []
        self.charges = 0


class Item:
    def __init__(self):
        self.name = ''
        self.count = 0
        self.description = ''
    
    def add(self, amount=0):
        # Adds an "amount" of healthPotions to inventory
        if isinstance(amount, int):
            self.count+amount
            return True
        else:
            return False
    
    def remove(self, amount=0):
        # Subtracts an "amount" of healthPotion
        if isinstance(amount, int):
            self.count-amount
            return True
        else:
            return False
