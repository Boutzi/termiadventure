import json
import time
import logics.settings as settings
class Dialogs:
    def __init__(self):
        self.narrator = "SNAKE"
        self.dialogs = []
        self.initializeDialogs()

    def createDialog(self, scene, texts):
        dialog = {
            "scene": scene,
            "texts": texts
        }
        self.dialogs.append(dialog)

    def initializeDialogs(self):
        with open('data/dialogs.json', encoding='utf-8') as f:
            dialogs = json.load(f)
        for dialog in dialogs:
            self.createDialog(dialog["scene"], dialog["texts"])

    def getDialog(self, scene, number):
        filtered = list(filter(lambda dialog: dialog["scene"] == scene, self.dialogs))
        if filtered:
            return filtered[0]["texts"][number]
        
    def printText(self, text, narrator, timer, pause, colorIn, colorOut):
        if narrator:
            text = settings.config.colors.getColors(colorIn) + self.narrator + " : " + text + settings.config.colors.getColors(colorOut)
        else:
            text = settings.config.colors.getColors(colorIn) + text + settings.config.colors.getColors(colorOut)

        if pause:
            time.sleep(pause)

        if timer:
            for letter in text:
                print(letter, end="", flush=True)
                time.sleep(timer)
        else:
            print(text)
    
    def displayDialog(self, scene, number, narrator, args, colorIn, colorOut, timer, pause):
        dialog = self.getDialog(scene, number)
        if dialog:
            dialog = dialog.format(*args)
            if narrator:
                dialog = settings.config.colors.getColors(colorIn) + self.narrator + " : " + dialog + settings.config.colors.getColors(colorOut)
            else:
                dialog = settings.config.colors.getColors(colorIn) + dialog + settings.config.colors.getColors(colorOut)

            if pause:
                time.sleep(pause)

            if timer:
                for letter in dialog:
                    print(letter, end="", flush=True)
                    time.sleep(timer)
            else:
                print(dialog)