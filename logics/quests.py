import json
import logics.settings as settings

class Quests:
    def __init__(self) -> None:
        self.quests = []
        self.initializeQuests()

    def createQuest(self, quest_name, quest_description, quest_type, quest_reward, quest_location, quest_status):
        quest = {
            "quest_name": quest_name,
            "quest_description": quest_description,
            "quest_type": quest_type,
            "quest_reward": quest_reward,
            "quest_location": quest_location,
            "quest_status": quest_status
        }   
        self.quests.append(quest)
    
    def initializeQuests(self):
        with open('data/quests.json', 'r', encoding='utf-8') as f:
            quests = json.load(f)
        for quest in quests:
            self.createQuest(quest["quest_name"], quest["quest_description"], quest["quest_type"], quest["quest_reward"], quest["quest_location"], quest["quest_status"])    

    def getQuest(self, quest_name):
        filtered = list(filter(lambda quest: quest["quest_name"] == quest_name, self.quests))
        if len(filtered) > 0:
            return filtered[0]

    def getQuests(self):
        return self.quests
    
    def getQuestsByStatus(self, quest_status):
        filtered = list(filter(lambda quest: quest["quest_status"] == quest_status, self.quests))
        if len(filtered) > 0:
            return filtered[0]
    
    def addQuests(self):
        for quest in self.quests:
            if quest["quest_status"] == "in_progress":
                settings.config.character.quest.append(quest)
        for quest in self.quests:
            if quest["quest_status"] == "completed":
                settings.config.character.quest.append(quest)

    def displayMyQuests(self):
        while True:
            try:
                settings.config.utils.clear()
                for quest_in_progress in settings.config.character.quest:
                    if quest_in_progress["quest_status"] == "in_progress":
                        print("Quête(s) en cours : " + quest_in_progress["quest_name"])
                        #print("Description : " + quest_in_progress["quest_description"])
                        print("Type : " + quest_in_progress["quest_type"])
                        #print("Récompense : " + str(quest_in_progress["quest_reward"]) + " po")
                        #print("Zone : " + quest_in_progress["quest_location"])
                        print("")
                for quest_done in settings.config.character.quest:
                    if quest_done["quest_status"] == "completed":
                        print("Quête(s) Terminée(s) : " + quest_done["quest_name"])
                        #print("Description : " + quest_done["quest_description"])
                        print("Type : " + quest_done["quest_type"])
                        #print("Récompense : " + str(quest_done["quest_reward"]) + " po")
                        #print("Zone : " + quest_done["quest_location"])
                        print("")
                print("\n")
                settings.config.menus.main_menu_back()
            except ValueError:
                pass
            else:
                self.displayMyQuests()