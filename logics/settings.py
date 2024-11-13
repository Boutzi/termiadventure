from logics.maps import Maps
from logics.character import Character
from logics.weapons import Weapons
from logics.armors import Armors
from logics.consumables import Consumables
from logics.dialogs import Dialogs
from logics.utils import Utils
from logics.jobs import Jobs
from logics.menus import Menus
from logics.inventory import Inventory
from logics.loadings import Loadings
from logics.quests import Quests
from logics.colors import Colors

class Settings:
    def __init__(self):
        self.state = "intro"
        self.maps = Maps()
        self.inventory = Inventory()
        self.weapons = Weapons()
        self.armors = Armors()
        self.consumables = Consumables()
        self.dialogs = Dialogs()
        self.utils = Utils()
        self.loadings = Loadings()
        self.colors = Colors()
        self.menus = Menus()
        self.quests = Quests()
        self.jobs = Jobs()
        self.character = Character()

    def setEnvironnement(self, _menus, _job, _currentPlace):
        self.state = _menus
        self.character.job = _job
        self.character.setAttributes()
        self.maps.currentPlace = _currentPlace
        self.maps.getMap()
        self.character.addPlayerOnMap(self.maps.getCurrentMap(), 2, 2)
        self.quests.addQuests()
        
config = Settings()