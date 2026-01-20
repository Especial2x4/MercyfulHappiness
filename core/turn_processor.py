from core.config import BUILDING_TYPES
from models.building import Building


class TurnProcessor:
    def process_turn(self, city, instructions):
        city.assign_farmers(instructions.get("farmers", 0))
        city.assign_workers(instructions.get("workers", 0))

        building_choice = instructions.get("building", "0")
        if building_choice != "0":
            self._handle_building(city, building_choice)

        produced = city.produce_food()
        consumed = city.consume_food()

        completed = city.process_buildings()
        growth = city.apply_population_growth()

        # 🔴 ESTA LÍNEA FALTABA
        city.update_happiness()

        balance = produced - consumed
        return balance, growth, completed



    

    
