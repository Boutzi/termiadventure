import json

class Armors:
    def __init__(self):
        self.armors = []
        self.initializeArmors()

    def createWeapon(self, class_name, armor_name, price, bonus_deff):
        armor = {
            "class_name": class_name,
            "name" : armor_name,
            "price" : price,
            "bonus_deff": bonus_deff
        }   
        self.armors.append(armor)

    def getArmors(self, class_name):
        filtered = list(filter(lambda armor: armor["class_name"] == class_name, self.armors))
        if len(filtered) > 0:
            return filtered
        return {}
        
    def getWeapon(self, armor_name):
        filtered = list(filter(lambda armor: armor["armor_name"] == armor_name, self.armors))
        if len(filtered) > 0:
            return filtered[0]
        
    def getWeaponAttribute(self, armor_name, attribute):
        filtered = list(filter(lambda armor: armor["armor_name"] == armor_name, self.armors))
        if len(filtered) > 0:
            return filtered[0][attribute]

    def initializeArmors(self):
        with open('data/armors.json', 'r', encoding='utf-8') as f:
            armors = json.load(f)
        for armor in armors:
            self.createWeapon(armor["class_name"], armor["armor_name"], armor["price"], armor["bonus_deff"])