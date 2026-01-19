# En config.py
BUILDING_TYPES = {
    "escuela": {
        "name": "Escuela",
        "food_cost": 50,
        "build_time": 3,
        "workers_required": 2,
        "effect": {
            "type": "education",
            "value": 0.1,  # +10% productividad futura
            "requires": ["teachers"]  # Nuevo tipo de trabajador
        }
    },
    "laboratorio": {
        "name": "Laboratorio",
        "food_cost": 100,
        "build_time": 5,
        "workers_required": 3,
        "effect": {
            "type": "technology",
            "unlocks": ["advanced_farming", "medicine"],
            "research_rate": 0.2  # +20% velocidad investigación
        }
    }
}