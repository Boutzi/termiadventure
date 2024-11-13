import time
import os
import logics.settings as settings
from logics.colors import Colors

class Menus:
    def __init__(self):
        self.main = ["Aventure", "Boutique", "Quêtes", "Profil", "Options"]
        self.main_back = "Retour"
        self.shop = ["Armes", "Armures", "Consommables", "Vendre"]
        self.options = ["Sauvegarder", "Supprimer le personnage"]
        self.confirm = ["Oui", "Non"]
        self.weapons = []
    
    def main_menu(self):
        while True:
            try:
                settings.config.utils.title()
                print("\n", end="")
                for i, title in enumerate(self.main):
                    print(str(i + 1) + ". " + Colors.WHITE + title + "  " + Colors.ENDC, end="")
                print(f"{len(self.main) + 1}. " + Colors.WHITE + "Quitter" + Colors.ENDC)
                print("\n")
                settings.config.utils.clearInput()
                menu_choice_int = int(settings.config.utils.getInput(""))
                if menu_choice_int == 1:
                    settings.config.maps.getMapInformation()
                    settings.config.state = "moving"
                elif menu_choice_int == 2:
                    self.shop_menu()
                elif menu_choice_int == 3:
                    settings.config.quests.displayMyQuests()
                elif menu_choice_int == 4:
                    settings.config.character.getAttributes(settings.config.character)
                elif menu_choice_int == 5:
                    self.menuOptions()
                elif menu_choice_int == len(self.main) + 1:
                    os.system("cls||clear")
                    settings.config.state = "exit"
                else:
                    settings.config.state = "menus"
            except ValueError:
                pass
            else:
                break

    def main_menu_back(self):
        print("1. " + settings.config.colors.GREEN + settings.config.menus.main_back + settings.config.colors.ENDC)
        settings.config.utils.clearInput()
        menu_choice_int = int(input())
        if menu_choice_int == 1:
            self.main_menu()

    def shop_menu(self):
        while True:
            try:
                settings.config.utils.clear()
                print("\n", end="")
                for i, name in enumerate(self.shop):
                    print(str(i + 1) + ". " + Colors.YELLOW + name + "  " + Colors.ENDC, end="")
                print(f"{len(self.shop) + 1}. " + Colors.GREEN + "Retour" + Colors.ENDC)
                print("\n")
                menu_choice_int = int(settings.config.utils.getInput(""))
                if menu_choice_int == 1: #Weapons
                    self.shop_menu_list(settings.config.weapons.getWeapons(settings.config.character.job), "weapons")
                elif menu_choice_int == 2: #Armors
                    self.shop_menu_list(settings.config.armors.getArmors(settings.config.character.job), "armors")
                elif menu_choice_int == 3: #Consumables
                    self.shop_menu_list(settings.config.consumables.getConsumables(), "consumables")
                elif menu_choice_int == 4: #Sell
                    self.shop_menu_sell()
                elif menu_choice_int == 5: #GoBack
                    self.main_menu()
            except ValueError:
                pass
            else:
                self.shop_menu()

    def shop_menu_list(self, list_items, type):
        while True:
            try:
                settings.config.utils.clear()
                print (f"Solde : {settings.config.character.po}")
                filtered_inventory = [item['name'] for item in settings.config.character.inventory if 'name' in item]
                owned_weapons = []
            
                for i, item in enumerate(list_items):
                    match type:
                        case "weapons":
                            if item["name"] in filtered_inventory:
                                owned_weapons.append(item)
                                print(str(i + 1) + ". " + Colors.RED + item["name"] + Colors.ENDC + Colors.GREEN + " (possédé)" + Colors.ENDC)
                            else:
                                print(str(i + 1) + ". " + Colors.LBLUE + item["name"] + Colors.ENDC + Colors.YELLOW +  " (" + str(item["price"]) + " pièces d'or, +" + str(item["bonus_atk"]) + " d'attaque)" + Colors.ENDC)
                        case "armors":
                            if item["name"] in filtered_inventory:
                                owned_weapons.append(item)
                                print(str(i + 1) + ". " + Colors.RED + item["name"] + Colors.ENDC + Colors.GREEN + " (possédé)" + Colors.ENDC)
                            else:
                                print(str(i + 1) + ". " + Colors.LBLUE + item["name"] + Colors.ENDC + Colors.YELLOW +  " (" + str(item["price"]) + " pièces d'or, +" + str(item["bonus_deff"]) + " de défense)" + Colors.ENDC)
                        case "consumables":
                            print(str(i + 1) + ". " + Colors.LBLUE + item["name"] + Colors.ENDC + Colors.YELLOW +  " (" + str(item["price"]) + " pièces d'or)" + Colors.ENDC + " - " + Colors.LBLUE + str(item["description"]) + Colors.ENDC)
                print(f"{len(list_items) + 1}. " + Colors.GREEN + "Retour" + Colors.ENDC)
                settings.config.utils.clearInput()
                menu_choice_int = int(settings.config.utils.getInput(""))
                if menu_choice_int == len(list_items) + 1:
                    self.shop_menu()
                elif menu_choice_int - 1 <= len(list_items):
                    if list_items[menu_choice_int - 1] in owned_weapons:
                        print("Vous possédez déjà cet objet")
                        time.sleep(1)
                        self.shop_menu_list(list_items, type)
                    else:
                        settings.config.inventory.buyItem(list_items[menu_choice_int - 1])
                        time.sleep(1)
                        self.shop_menu_list(list_items, type)
            except ValueError:
                pass
            else:
                self.shop_menu_list(list_items, type)

    def shop_menu_sell(self):
        while True:
            try:
                os.system("cls")
                available_items = settings.config.character.inventory
                print (f"Solde : {settings.config.character.po}")
                for i, item in enumerate(available_items):
                    print(str(i + 1) + ". " + Colors.PURPLE, end="")
                    print(item["name"], end="")
                    print(Colors.ENDC)
                print(f"{len(available_items) + 1}. " + Colors.GREEN + "Retour" + Colors.ENDC)
                settings.config.utils.clearInput()
                menu_choice_int = int(settings.config.utils.getInput(""))
                if menu_choice_int == len(available_items) + 1:
                    self.shop_menu()
                elif menu_choice_int - 1 <= len(available_items):
                    settings.config.inventory.sellItem(available_items[menu_choice_int - 1])
                    time.sleep(1)
                    self.shop_menu_sell()
            except ValueError:
                pass
            else:
                self.shop_menu_sell()

    def menuOptions(self):
        os.system("cls")
        for i, option in enumerate(self.options):
            print(str(i + 1) + ". " + Colors.YELLOW + option + "  " + Colors.ENDC, end="")
        print(f"{len(self.options) + 1}. " + Colors.GREEN + "Retour" + Colors.ENDC)
        menu_choice_int = int(settings.config.utils.getInput(""))
        if menu_choice_int == len(self.options) + 1:
            self.main_menu()
        elif menu_choice_int <= len(self.options):
            if menu_choice_int == 1:
                settings.config.utils.saveCharacter()
            elif menu_choice_int == 2:
                settings.config.utils.clear()
                settings.config.dialogs.displayDialog("reset", 6, True, [], "RED", "", 0.025, False)
                print("\n")
                for i, confirmation in enumerate(self.confirm):
                    print(str(i + 1) + ". " + Colors.YELLOW + confirmation + "  " + Colors.ENDC, end="")
                print("\n")
                confirm_reset = int(settings.config.utils.getInput(""))
                if confirm_reset == 1:
                    settings.config.utils.resetCharacter()
                    settings.config.utils.clear()
                    time.sleep(0.5)
                    settings.config.state = "intro"
                elif confirm_reset == 2:
                    self.menuOptions()
                else:
                    self.menuOptions()

