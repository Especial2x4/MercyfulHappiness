# data/gamestate.py
import json
import os

SAVE_FILE = "savegame.json"

class GameState:
    def __init__(self):
        pass

    def save(self, city):        
        data = {
            "city": {
                "name": city.name,
                "population": city.population,
                "farmers": city.farmers,
                "idle": city.idle,
                "workers": city.workers,
                "food": city.food,
                "happiness_per_capita": city.happiness_per_capita   
            }
        }

        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load(self):
        if not os.path.exists(SAVE_FILE):
            return None
        
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        return data