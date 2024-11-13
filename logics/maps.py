import os
import json
import logics.settings as settings

class Maps:
    def __init__(self):
        self.places = []
        self.currentPlace = "TermiVille"
        self.initializeMaps()

    def createMap(self, name, description, row, col):
        place = {
            "name": name,
            "description": description,
            "row": row,
            "col": col,
            "map": None
        }
        self.generateMap(place)
        self.places.append(place)

    def initializeMaps(self):
        with open('data/maps.json', 'r', encoding='utf-8') as f:
            maps = json.load(f)
        for map in maps:
            self.createMap(map["name"], map["description"], map["row"], map["col"])
            if len(map["characters"]) > 0:
                for character in map["characters"]:
                    self.setCharMap(map["name"], character["symbol"], character["x"], character["y"])

    def generateMap(self, place):
        place["map"] = [["#" for j in range(place["col"])] for i in range(place["row"])]
        for i in range(1, place["row"] - 1):
            for j in range(1, place["col"] - 1):
                place["map"][i][j] = " "
    
    def getMapInformation(self):
        settings.config.utils.clear()
        place = self.getCurrentMap()
        if place:
            print(place["name"])
            print("Description: " + place["description"])
            self.getMap()
    
    def getMap(self):
        place = self.getCurrentMap()
        if place:
            for i in range(place["row"]):
                for j in range(place["col"]):
                    print(place["map"][i][j], end="")
                print()

    def getCurrentMap(self):
        filtered_places = list(filter(lambda place: place["name"] == self.currentPlace, self.places))
        if filtered_places:
            return filtered_places[0]

    def setCharMap(self, name, char, row, col):
        for place in self.places:
            if place["name"] == name:
                place["map"][row][col] = char