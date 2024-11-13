import os
import logics.settings as settings
import time
import json
import pyfiglet

class Utils:
    def __init__(self) -> None:
        pass

    def getInput(self, text):
        try:
            import msvcrt # Windows
            while msvcrt.kbhit():
                msvcrt.getch()
        except ImportError:
            import sys, termios # Linux/Mac
            #termios.tcflush(sys.stdin, termios.TCIOFLUSH)
        if text != "":
            inputUser = input(text)
        else:
            inputUser = input()
        return inputUser
    
    def clearInput(self):
        try:
            import msvcrt # Windows
            while msvcrt.kbhit():
                msvcrt.getch()
        except ImportError:
            import sys, termios # Linux/Mac
            #termios.tcflush(sys.stdin, termios.TCIOFLUSH)

    def clear(self):
        os.system("cls||clear")

    def title(self):
        os.system("cls")
        print(settings.config.colors.PURPLE)
        print(pyfiglet.figlet_format("TermiAdventure"))
        print(settings.config.colors.ENDC)

    def loadCharacter(self):
        with open("data/character.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        if data != []:
            settings.config.character.name = data[0][0]["name"]
            settings.config.character.po = data[0][1]["po"]
            settings.config.character.hp = data[0][2]["hp"]
            settings.config.character.mp = data[0][3]["mp"]
            settings.config.character.atk = data[0][4]["atk"]
            settings.config.character.deff = data[0][5]["deff"]
            settings.config.character.job = data[0][6]["job"]
            settings.config.character.inventory = data[0][7]["inventory"]
            settings.config.character.quest = data[0][8]["quest"]
            settings.config.state = "menus"
        return data

    def saveCharacter(self):
        self.clear()
        print("Sauvegarde en cours...")
        time.sleep(1.5)
        save = []
        save.append(settings.config.character.getCharacter())
        
        save = json.dumps(save, indent=4)
        with open("data/character.json", "w", encoding="utf-8") as f:
            f.write(save)


        self.clear()
        print("Sauvegarde terminée.")
        time.sleep(1.5)

    def resetCharacter(self):
        self.clear()
        print("Effacement de la sauvegarde en cours...")
        time.sleep(1.5)
        print(settings.config.colors.RED)
        settings.config.loadings.loadingBar(192058)
        print(settings.config.colors.ENDC)
        settings.config.dialogs.displayDialog("reset", 0, False, [], "RED", "", 0.040, 1)
        print("\n\n                                                 ", end="")
        settings.config.dialogs.displayDialog("reset", 1, False, [], "RED", "", 0.040, 2)
        print("\n\n", end="")
        settings.config.dialogs.displayDialog("reset", 2, False, [], "RED", "", 0.040, 2)
        print("\n\n                                                 ", end="")
        settings.config.dialogs.displayDialog("reset", 3, False, [], "RED", "", 0.040, 1)
        print("\n\n", end="")
        settings.config.dialogs.displayDialog("reset", 4, False, [], "RED", "", 0.040, 1.5)
        settings.config.dialogs.displayDialog("reset", 5, False, [], "RED", "", 0.040, 0.5)
        time.sleep(1)
        settings.config.character.name = None
        settings.config.character.po = 5000
        settings.config.character.hp = None
        settings.config.character.mp = None
        settings.config.character.atk = None
        settings.config.character.deff = None
        settings.config.character.job = None
        settings.config.character.inventory = []
        settings.config.character.quest = []
        settings.config.weapons.weapons = []
        settings.config.armors.armors = []
        settings.config.consumables.consumables = []
        settings.config.quests.quests = []
        settings.config.dialogs.displayDialog("enter", 0, False, [], "YELLOW", "", False, False)
        settings.config.utils.getInput("")