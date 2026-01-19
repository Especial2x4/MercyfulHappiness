
# MercyfulHappiness/core/turn_processor.py (actualizado)
from core.commands import CommandParser

class TurnProcessor:
    def __init__(self):
        self.factor_scale = 3
        self.command_history = []  # Historial de comandos por turno
    
    def process_turn(self, city, instructions):
        """
        Procesa todas las acciones de un turno usando Command Pattern
        """
        # Limpiar historial del turno anterior
        self.command_history = []
        
        # 1. Parsear instrucciones a comandos
        commands = CommandParser.parse_instructions(instructions)
        
        # 2. Ejecutar comandos del usuario
        executed_commands = []
        for command in commands:
            if command.execute(city):
                executed_commands.append(command)
                print(f"✓ Comando ejecutado: {command}")
        
        # Guardar comandos ejecutados en el historial
        self.command_history.extend(executed_commands)
        
        # 3. Procesar efectos automáticos del turno
        self._consume_food(city)
        self._production_food(city)
        self._process_buildings(city)
        
        # 4. Calcular balance y crecimiento
        balance = self._calculate_food_balance(city)
        growth = self._calculate_population_growth(city)
        
        return balance, growth
    
    def undo_last_command(self, city):
        """Deshace el último comando ejecutado"""
        if self.command_history:
            last_command = self.command_history.pop()
            last_command.undo(city)
            print(f"↶ Comando deshecho: {last_command}")
            return True
        return False
    
    # Métodos auxiliares (sin cambios)
    def _consume_food(self, city):
        consumo = city.consumo_per_capita
        indice_de_consumo_por_turno = city.population * consumo
        city.food -= indice_de_consumo_por_turno
        print(f"Ahora se ha consumido {indice_de_consumo_por_turno} de comida")
    
    def _production_food(self, city):
        produccion = city.farmers * 2
        city.food += produccion
        print(f"Ahora se ha producido {produccion} de comida")
    
    def _process_buildings(self, city):
        for building in city.buildings:
            if not building.completed:
                building.work_on()
                if building.completed:
                    print(f"¡{building.name} completado!")
                    self._apply_building_effect(city, building)
    
    def _apply_building_effect(self, city, building):
        if building.name == "Escuela":
            print("¡La educación de la ciudad ha mejorado!")
        elif building.name == "Laboratorio":
            print("¡Se ha avanzado en investigación!")
        elif building.name == "Club Recreativo":
            valor_happiness = 0.1
            self._aumentar_happines(city, valor_happiness)
            print(f"¡La felicidad de la población ha aumentado {valor_happiness}!")
        elif building.name == "Poligono":
            print("¡La fortaleza de la ciudad ha aumentado!")
    
    def _calculate_food_balance(self, city):
        """Balance real: producción - consumo"""
        produccion = city.farmers * 2  # 2 por granjero
        consumo = city.population * 0.25
        balance = produccion - consumo
        return balance
    
    def _calculate_population_growth(self, city):
        """Crecimiento basado en excedente real"""
        balance = self._calculate_food_balance(city)
        
        if balance <= 0:
            # Hambruna: decrecimiento
            factor = min(abs(balance) // 10, 5)  # Máximo 5 por turno
            city.update_population(-factor)
            return -factor
        else:
            # Excedente: crecimiento moderado
            factor = min(balance // 20, 3)  # Máximo 3 por turno
            city.update_population(factor)
            return factor
    
    def _aumentar_happines(self, city, valor):
        city.happiness_per_capita = city.happiness_per_capita + valor
        city.happiness = city.happiness_per_capita * 100
        print(f"la felicidad per capita ahora es {city.happiness_per_capita}")
        print(f"la felicidad total ahora es {city.happiness}")

    
