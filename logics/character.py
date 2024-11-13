import keyboard
import sys
import logics.settings as settings

player_stats = ["Nom", "Pièces d'or", "HP", "Mana", "Attaque", "Défense", "Classe","Inventaire", "Quêtes"]
#player_stats_list = []
class Character:
    def __init__(self):
        self.name = None
        self.po = 5000
        self.hp = None
        self.mp = None
        self.atk = None
        self.deff = None
        self.job = None
        self.inventory = []
        self.quest = []

        self.row = 0
        self.col = 0
        self.canMove = True

    def getCharacter(self):
        character = []
        for attr_name, attr_value in vars(self).items():
            if attr_name != "row" and attr_name != "col" and attr_name != "canMove":
                character.append({attr_name : attr_value})
        return character
        
    def initializeCharacter(self):
       settings.config.character.createCharacter()
       settings.config.character.addPlayerOnMap(settings.config.maps.getCurrentMap(), 2, 2)

    def setAttributes(self):
        self.hp = settings.config.jobs.getJobAttributes(self.job, "hp")
        self.mp = settings.config.jobs.getJobAttributes(self.job, "mp")
        self.atk = settings.config.jobs.getJobAttributes(self.job, "atk")
        self.deff = settings.config.jobs.getJobAttributes(self.job, "deff")

    def getAttributes(self, character):
        while True:
            try:
                settings.config.utils.clear()
                print("Informations :\n")
                for attr_name, attr_value, attr_description in zip(vars(character).items(), vars(character).values(), player_stats):
                    if attr_name != "row" and attr_name != "col" and attr_name != "canMove":
                        if attr_name[0] == "inventory":
                            if len(attr_value) <= 0:
                                print(f"{settings.config.colors.YELLOW + attr_description + settings.config.colors.ENDC}: Vide")
                            else:
                                print(f"{settings.config.colors.YELLOW + attr_description + settings.config.colors.ENDC}: ", end="")
                                for i, item in enumerate(attr_value):
                                    print("[" + item["name"] + "] ", end="")
                                    if i == len(attr_value) - 1:
                                        print("")


                        elif attr_name[0] == "quest":
                            if len(attr_value) <= 0:
                                print(f"{settings.config.colors.YELLOW + attr_description + settings.config.colors.ENDC}: Vide")
                            else:
                                print(f"{settings.config.colors.YELLOW + attr_description + settings.config.colors.ENDC}:", end="")
                                for item in attr_value:
                                    print("[" + item["quest_name"] + "] ", end="")
                            
                        else:
                            print(f"{settings.config.colors.YELLOW + attr_description + settings.config.colors.ENDC} : {attr_value}")
                print("\n")
                settings.config.menus.main_menu_back()
            except ValueError:
                pass
            else:
                self.getAttributes(character)


    def addPlayerOnMap(self, place, row, col):
        place["map"][row][col] = "P"
        self.row = row
        self.col = col
    
    def movePlayerOnMap(self, place, row, col):
        place["map"][self.row][self.col] = " "
        place["map"][row][col] = "P"
        self.row = row
        self.col = col
    
    def handleInput(self):
        place = settings.config.maps.getCurrentMap()
        if place:
            if keyboard.is_pressed("up"):
                sys.stdin.flush()
                if place["map"][self.row - 1][self.col] != "#" and place["map"][self.row - 1][self.col] == " " and self.canMove == True:
                    self.movePlayerOnMap(place, self.row - 1, self.col)
                    self.canMove = False
                    settings.config.maps.getMapInformation()
            elif keyboard.is_pressed("down"):
                sys.stdin.flush()
                if place["map"][self.row + 1][self.col] != "#" and place["map"][self.row + 1][self.col] == " " and self.canMove == True:
                    self.movePlayerOnMap(place, self.row + 1, self.col)
                    self.canMove = False
                    settings.config.maps.getMapInformation()
            elif keyboard.is_pressed("left"):
                sys.stdin.flush()
                if place["map"][self.row][self.col - 1] != "#" and place["map"][self.row][self.col - 1] == " " and self.canMove == True:
                    self.movePlayerOnMap(place, self.row, self.col - 1)
                    self.canMove = False
                    settings.config.maps.getMapInformation()
            elif keyboard.is_pressed("right"):
                sys.stdin.flush()
                if place["map"][self.row][self.col + 1] != "#" and place["map"][self.row][self.col + 1] == " " and self.canMove == True:
                    self.movePlayerOnMap(place, self.row, self.col + 1)
                    self.canMove = False
                    settings.config.maps.getMapInformation()
            elif keyboard.is_pressed("escape"):
                settings.config.utils.clear()
                settings.config.state = "menus"
            else:
                self.canMove = True

    def createCharacter(self):
        settings.config.dialogs.displayDialog("enter", 0, False, [], "YELLOW", "", False, False)
        settings.config.utils.getInput("")
        settings.config.utils.clear()
        print("\n")
        print(settings.config.colors.LBLUE)
        settings.config.loadings.loadingBar(46018)
        print(settings.config.colors.ENDC)
        settings.config.utils.clear()

        settings.config.dialogs.displayDialog("intro_name", 0, True, [settings.config.dialogs.narrator], "LBLUE", "", 0.025, False)

        self.name = settings.config.utils.getInput("")

        settings.config.dialogs.displayDialog("intro_name", 1, True, [self.name], "LBLUE", "", 0.025, False)

        settings.config.dialogs.displayDialog("intro_name", 2, False, [], "LBLUE", "", 0.025, 0.2)
        
        settings.config.dialogs.displayDialog("intro_name", 3, False, [], "LBLUE", "", False, 0.3)

        settings.config.dialogs.displayDialog("loading", 0, False, [], "LBLUE", "", 0.3, False)

        settings.config.dialogs.displayDialog("intro_job", 0, True, [self.name], "LBLUE", "", 0.025, 0.2)

        settings.config.dialogs.displayDialog("intro_job", 1, True, [], "LBLUE", "", 0.025, False)

        settings.config.jobs.getJobs()

        jobIndex = settings.config.utils.getInput("\nQuelle voie emprunter : ")
        self.job = settings.config.jobs.getJobAttributesByIndex(int(jobIndex), "name")
        
        self.setAttributes()
        settings.config.utils.clear()

        settings.config.dialogs.printText(settings.config.jobs.getJobAttributes(self.job, "ascent"), True, 0.025, False, "LBLUE", "")

        settings.config.dialogs.displayDialog("intro_po", 0, False, [], "LBLUE", "", 0.025, False)

        settings.config.dialogs.displayDialog("loading", 0, False, [], "LBLUE", "", 0.3, False)

        settings.config.dialogs.displayDialog("intro_po", 1, False, [self.name, self.po], "LBLUE", "", 0.025, False)
        
        settings.config.dialogs.displayDialog("enter", 0, False, [], "YELLOW", "", False, False)
        settings.config.utils.getInput("")

        settings.config.state = "menus"