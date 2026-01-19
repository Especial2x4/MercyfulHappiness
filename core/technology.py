# Nuevo módulo: core/technology.py
class TechnologyTree:
    def __init__(self):
        self.technologies = {
            "basic_farming": {"unlocked": True, "effect": "farmers_production+1"},
            "irrigation": {"unlocked": False, "cost": 50, "effect": "farmers_production+2"},
            "education": {"unlocked": False, "cost": 100, "effect": "unlock_teachers"},
            "medicine": {"unlocked": False, "cost": 150, "effect": "population_growth+20%"}
        }
    
    def research(self, tech_id, city):
        if tech_id in self.technologies and not self.technologies[tech_id]["unlocked"]:
            if city.food >= self.technologies[tech_id]["cost"]:
                city.food -= self.technologies[tech_id]["cost"]
                self.technologies[tech_id]["unlocked"] = True
                self._apply_effect(tech_id, city)
                return True
        return False