class Inventory:
    def __init__(self):
        self.copper = 0
        self.silver = 0
        self.gold = 0
        self.platinum = 0
        self.healthPotions = 0
        self.items = []
        self.weapons = []
        
    def getCopper(self):
        #Gets amount of copper in inventory
        return self.copper
    
    def addCopper(self, amount=0):
        #adds an "amount" of copper to inventory
        if isinstance(amount,int):
            self.copper+amount
            return True
        else:
            return False
    
    def removeCopper(self, amount=0):
        #Subtracts an "amount" of copper
        if isinstance(amount,int):
            self.copper-amount
            return True
        else:
            return False
    
    def getSilver(self):
        #Gets amount of silver in inventory
        return self.silver
    
    def addSilver(self, amount=0):
        #adds an "amount" of silver to inventory
        if isinstance(amount,int):
            self.silver+amount
            return True
        else:
            return False
    
    def removeSilver(self, amount=0):
        #Subtracts an "amount" of silver
        if isinstance(amount,int):
            self.silver-amount
            return True
        else:
            return False
    
    def getGold(self):
        #Gets amount of gold in inventory
        return self.gold
    
    def addGold(self, amount=0):
        #adds an "amount" of gold to inventory
        if isinstance(amount,int):
            self.gold+amount
            return True
        else:
            return False
    
    def removeGold(self, amount=0):
        #Subtracts an "amount" of gold
        if isinstance(amount,int):
            self.gold-amount
            return True
        else:
            return False
    
    def getPlatinum(self):
        #Gets amount of platinum in inventory
        return self.platinum
    
    def addPlatinum(self, amount=0):
        #adds an "amount" of platinum to inventory
        if isinstance(amount,int):
            self.platinum+amount
            return True
        else:
            return False
    
    def removePlatinum(self, amount=0):
        #Subtracts an "amount" of platinum
        if isinstance(amount,int):
            self.platinum-amount
            return True
        else:
            return False
    
    def getHealthPotion(self):
        #Gets amount of healthPotions in inventory
        return self.healthPotions
    
    def addHealthPotion(self, amount=0):
        #adds an "amount" of healthPotions to inventory
        if isinstance(amount,int):
            self.healthPotions+amount
            return True
        else:
            return False
    
    def removeHealthPotion(self, amount=0):
        #Subtracts an "amount" of healthPotion
        if isinstance(amount,int):
            self.healthPotions-amount
            return True
        else:
            return False
    
    def addWeapon(self, Weapon):
        self.weapons.append(Weapon)
        
    def removeWeapon(self, Weapon):
        if Weapon in self.weapons:
            self.weapons.remove(Weapon)
    
    def addItem(self, Item):
        self.items.append(Item)
        
    def removeItem(self, Item):
        if Item in self.items:
            self.items.remove(Item)


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
    