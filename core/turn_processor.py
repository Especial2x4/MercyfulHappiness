from core.config import BUILDING_TYPES
from models.building import Building


class TurnProcessor:
    def process_turn(self, city, instructions):
        # 1. Asignaciones
        city.assign_farmers(instructions.get("farmers", 0))
        city.assign_workers(instructions.get("workers", 0))

        # 2. Construcción (ESTO FALTABA)
        building_choice = instructions.get("building", "0")
        if building_choice != "0":
            self._handle_building(city, building_choice)

        # 3. Producción y consumo
        produced = city.produce_food()
        consumed = city.consume_food()

        # 4. Procesar edificios
        completed = city.process_buildings()

        # 5. Crecimiento
        growth = city.apply_population_growth()

        balance = produced - consumed
        return balance, growth, completed

    def _handle_building(self, city, choice):
        mapping = {
            "1": "escuela",
            "2": "laboratorio",
            "3": "club",
            "4": "poligono"
        }

        key = mapping.get(choice)
        if not key or key not in BUILDING_TYPES:
            return

        data = BUILDING_TYPES[key]

        building = Building(
            name=data["name"],
            food_cost=data["food_cost"],
            build_time=data["build_time"],
            workers_required=data["workers_required"]
        )

        city.start_building(building)


    
