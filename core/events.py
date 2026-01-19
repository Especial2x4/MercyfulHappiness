# core/events.py
import random

class EventSystem:
    EVENTS = {
        "drought": {
            "probability": 0.05,
            "effect": "farmers_production-50%",
            "duration": 3
        },
        "festival": {
            "probability": 0.03,
            "effect": "happiness+0.3",
            "cost": 20
        },
        "plague": {
            "probability": 0.02,
            "effect": "population-10%",
            "requires_low_happiness": True
        }
    }
    
    def check_events(self, city):
        """Verificar eventos aleatorios por turno"""
        for event_id, event_data in self.EVENTS.items():
            if random.random() < event_data["probability"]:
                self.trigger_event(event_id, city)