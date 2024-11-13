import json

class Consumables:
    def __init__(self):
        self.consumables = []
        self.initializeConsumables()

    def createConsumable(self, name, description, price, hp, mana):
        consumable = {
            "name": name,
            "description" : description,
            "price" : price,
            "hp" : hp,
            "mana": mana
        }   
        self.consumables.append(consumable)

    def getConsumables(self):
        return self.consumables
        
    def getConsumable(self, name):
        filtered = list(filter(lambda consumable: consumable["name"] == name, self.consumables))
        if len(filtered) > 0:
            return filtered[0]
        
    def getConsumableAttribute(self, name, attribute):
        filtered = list(filter(lambda consumable: consumable["name"] == name, self.consumables))
        if len(filtered) > 0:
            return filtered[0][attribute]

    def initializeConsumables(self):
        with open('data/consumables.json', 'r', encoding='utf-8') as f:
            consumables = json.load(f)
        for consumable in consumables:
            self.createConsumable(consumable["name"], consumable["description"], consumable["price"], consumable["hp"], consumable["mana"])