import json
import logics.settings as settings

class Inventory:
    def buyItem(self, item):
        selected_item_price = item["price"]
        if settings.config.character.po >= selected_item_price:
            settings.config.character.po -= selected_item_price
            settings.config.character.inventory.append(item)
            print(settings.config.colors.GREEN, end="") 
            print("Merci d'avoir acheté : ", end="")
            print(item["name"], end="")
            print(settings.config.colors.ENDC, end="\n")
            #settings.config.loadings.loadingCircle()

        else:
            print(f"{settings.config.colors.RED}Vous n'avez pas assez de pièces d'or, désolé !{settings.config.colors.ENDC}")

    def sellItem(self, item):
        selected_item_price = item["price"]
        settings.config.character.po += selected_item_price
        settings.config.character.inventory.remove(item)
        print(settings.config.colors.GREEN, end="") 
        print("Merci d'avoir vendu : ", end="")
        print(item["name"], end="")
        print(settings.config.colors.ENDC, end="\n")
        #settings.config.loadings.loadingCircle()