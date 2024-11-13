import json

class Weapons:
    def __init__(self):
        self.weapons = []
        self.initializeWeapons()

    def createWeapon(self, class_name, weapon_name, price, bonus_atk):
        weapon = {
            "class_name": class_name,
            "name" : weapon_name,
            "price" : price,
            "bonus_atk": bonus_atk
        }   
        self.weapons.append(weapon)

    def getWeapons(self, class_name):
        filtered = list(filter(lambda weapon: weapon["class_name"] == class_name, self.weapons))
        if len(filtered) > 0:
            return filtered
        return {}
        
    def getWeapon(self, weapon_name):
        filtered = list(filter(lambda weapon: weapon["weapon_name"] == weapon_name, self.weapons))
        if len(filtered) > 0:
            return filtered[0]
        
    def getWeaponAttribute(self, weapon_name, attribute):
        filtered = list(filter(lambda weapon: weapon["weapon_name"] == weapon_name, self.weapons))
        if len(filtered) > 0:
            return filtered[0][attribute]

    def initializeWeapons(self):
        with open('data/weapons.json', 'r', encoding='utf-8') as f:
            weapons = json.load(f)
        for weapon in weapons:
            self.createWeapon(weapon["class_name"], weapon["weapon_name"], weapon["price"], weapon["bonus_atk"])