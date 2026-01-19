# core/victory_conditions.py
class VictoryConditions:
    CONDITIONS = {
        "population": {
            "type": "population",
            "target": 1000,
            "description": "Alcanzar 1000 habitantes"
        },
        "technology": {
            "type": "technology",
            "target": 5,
            "description": "Investigar 5 tecnologías"
        },
        "happiness": {
            "type": "happiness",
            "target": 0.8,
            "duration": 10,
            "description": "Mantener felicidad >80% por 10 turnos"
        },
        "construction": {
            "type": "buildings",
            "target": ["Escuela", "Laboratorio", "Hospital"],
            "description": "Construir todos los edificios principales"
        }
    }