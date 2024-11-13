import os
import sys
import logics.settings as settings

if __name__ == "__main__":
    os.system("cls")
    settings.config.utils.loadCharacter()
    if len(sys.argv) > 1:
        settings.config.setEnvironnement(sys.argv[1], sys.argv[2], sys.argv[3])
    while settings.config.state != "exit":
        match settings.config.state:
            case "intro":
                settings.config.utils.title()
                settings.config.character.initializeCharacter()
            case "menus":
                settings.config.jobs.initializeJobs()
                settings.config.menus.main_menu()
            case "moving":
                settings.config.character.handleInput()