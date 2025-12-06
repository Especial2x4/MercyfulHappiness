
# POR CADA TURNO SE PROCESAN LOS SERVICIOS DE COMIDA Y POBLACIÓN
# EN ESTE MODULO ESTÁN LOS ALGORITMOS DEL JUEGO

# turn_processor.py
from core.config import BUILDING_TYPES

class TurnProcessor:
    def __init__(self):
        self.factor_scale = 3   # ajustable

    def process_turn(self, city, instructions):
        """
        Procesa todas las acciones de un turno
        el parámetro instructions debe ser un diccionario
        Returns: (balance_comida, crecimiento)
        """
        # 1. Asignar granjeros
        self._assign_farmers(city, instructions.get("farmers", 0))
        
        # 2. Asignar obreros
        self._assign_workers(city, instructions.get("workers", 0))

        # 3. Consumir comida
        self._consume_food(city)

        # 4. Producir comida
        self._production_food(city)
        
        # 5. Procesar construcción de edificios
        building_choice = instructions.get("building", "0")
        if building_choice != "0":
            self._process_building(city, building_choice)
        
        
        # 6. Procesar edificios en construcción
        self._process_buildings(city)

        # 7. Calcular balance de comida
        balance = self._calculate_food_balance(city)
        
        # 8. Calcular crecimiento poblacional
        growth = self._calculate_population_growth(city)
        
        
        return balance, growth

    def _assign_farmers(self, city, amount):
        """Asignar ociosos a granjeros"""
        if amount > 0 and city.idle >= amount:
            city.farmers += amount
            city.idle -= amount
            city._sync_population()

    def _assign_workers(self, city, amount):
        """Asignar ociosos a obreros"""
        if amount > 0 and city.idle >= amount:
            city.workers += amount
            city.idle -= amount
            city._sync_population()

    def _process_building(self, city, building_choice):
        """Procesar construcción de un nuevo edificio"""
        building_map = {"1": "escuela", "2": "laboratorio", "3": "club"}
        
        if building_choice in building_map:
            building_type = building_map[building_choice]
            
            if building_type not in BUILDING_TYPES:
                print(f"Tipo de edificio '{building_type}' no válido")
                return
            
            building_info = BUILDING_TYPES[building_type]
            
            # Verificar recursos
            costo_comida = building_info["food_cost"]
            if city.food < costo_comida:
                print(f"No hay suficiente comida. Necesitas {building_info['food_cost']}")
                return
            else:
                city.food - costo_comida
            
            if city.workers < building_info["workers_required"]:
                print(f"No hay suficientes obreros. Necesitas {building_info['workers_required']}")
                return
            
            # Crear el edificio
            from models.building import Building
            building = Building(
                name=building_info["name"],
                food_cost=building_info["food_cost"],
                build_time=building_info["build_time"],
                workers_required=building_info["workers_required"]
            )
            
            # Consumir recursos
            city.food -= building_info["food_cost"]
            city.buildings.append(building)
            print(f"¡{building_info['name']} en construcción! ({building_info['build_time']} turnos)")

    def _consume_food(self, city):
        """Consumir comida por la población"""
        consumo = city.consumo_per_capita
        indice_de_consumo_por_turno = city.population * consumo
        city.food -= indice_de_consumo_por_turno
        print(f"Ahora se ha consumido {indice_de_consumo_por_turno} de comida" )

    def _production_food(self, city):
        """Producir comida por granjero"""
        produccion = city.farmers * 2
        city.food += produccion
        print(f"Ahora se ha producido {produccion} de comida" )
    

    def _process_buildings(self, city):
        """Procesar avance de edificios en construcción"""
        for building in city.buildings:
            if not building.completed:
                building.work_on()
                if building.completed:
                    print(f"¡{building.name} completado!")
                    self._apply_building_effect(city, building)

    def _apply_building_effect(self, city, building):
        """Aplicar efectos del edificio cuando se completa"""
        # Aquí puedes agregar efectos especiales
        if building.name == "Escuela":
            print("¡La educación de la ciudad ha mejorado!")
            # Educación sirve para hacer cientificos y los cientificos se requieren para
            # hacer laboratorios y de los laboratorios salen tecnologías
        elif building.name == "Laboratorio":
            print("¡Se ha avanzado en investigación!")
        elif building.name == "Club Recreativo":
            valor_happiness = 0.1
            self._aumentar_happines(city, valor_happiness)
            print(f"¡La felicidad de la población ha aumentado {valor_happiness}!")

    def _calculate_food_balance(self, city):
        """Calcular balance de comida"""
        balance = city.food - city.population
        return balance

    def _calculate_population_growth(self, city):
        """Calcular crecimiento poblacional basado en comida"""
        balance = self._calculate_food_balance(city)
        factor = max(1, abs(balance) // self.factor_scale)

        if balance < 0:
            # Reducir población
            city.update_population(-factor)
            print(f"Balance negativo {balance}. Población decrece en {factor}.")
            return -factor
        else:
            # Aumentar población
            city.update_population(factor)
            print(f"Balance positivo {balance}. Población crece en {factor}.")
            return factor
    

    def _aumentar_happines(self, city, valor):
        """El valor pasado por parámetro debe estar entre el 0.1 y el 0.9"""
        city.happiness_per_capita = city.happiness_per_capita + valor
        city.happiness = city.happiness_per_capita * 100
        print(f"la felicidad per capita ahora es {city.happiness_per_capita}")
        print(f"la felicidad total ahora es {city.happiness}")

    
