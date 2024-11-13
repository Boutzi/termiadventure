import logics.settings as settings



def testsetEnvironnement():
    settings.config.setEnvironnement("main", "warrior", "village")
    assert settings.config.state == "main"
    assert settings.config.character.job == "warrior"
    assert settings.config.maps.currentPlace == "village"

def testsetEnvironnement2():
    settings.config.setEnvironnement("", "warrior", "village")
    assert settings.config.state != "main"
    assert settings.config.character.job == "warrior"
    assert settings.config.maps.currentPlace == "village"