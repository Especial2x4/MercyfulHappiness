# MercyfulHappiness/core/commands.py
from abc import ABC, abstractmethod
from core.config import BUILDING_TYPES
from models.building import Building

class Command(ABC):
    """Interfaz base para todos los comandos del juego"""
    
    @abstractmethod
    def execute(self, city):
        """Ejecuta el comando en la ciudad dada"""
        pass
    
    def undo(self, city):
        """Deshace el comando (opcional)"""
        pass
    
    @abstractmethod
    def __str__(self):
        """Descripción del comando para logging"""
        pass


class AssignFarmersCommand(Command):
    """Comando para asignar ociosos a granjeros"""
    
    def __init__(self, amount):
        self.amount = amount
        self.executed = False
        self.previous_state = None
    
    def execute(self, city):
        if self.amount > 0 and city.idle >= self.amount:
            # Guardar estado anterior para undo
            self.previous_state = {
                'idle': city.idle,
                'farmers': city.farmers
            }
            
            # Ejecutar asignación
            city.farmers += self.amount
            city.idle -= self.amount
            city._sync_population()
            self.executed = True
            return True
        return False
    
    def undo(self, city):
        if self.executed and self.previous_state:
            city.idle = self.previous_state['idle']
            city.farmers = self.previous_state['farmers']
            city._sync_population()
            self.executed = False
    
    def __str__(self):
        return f"Asignar {self.amount} granjeros"


class AssignWorkersCommand(Command):
    """Comando para asignar ociosos a obreros"""
    
    def __init__(self, amount):
        self.amount = amount
        self.executed = False
        self.previous_state = None
    
    def execute(self, city):
        if self.amount > 0 and city.idle >= self.amount:
            # Guardar estado anterior para undo
            self.previous_state = {
                'idle': city.idle,
                'workers': city.workers
            }
            
            # Ejecutar asignación
            city.workers += self.amount
            city.idle -= self.amount
            city._sync_population()
            self.executed = True
            return True
        return False
    
    def undo(self, city):
        if self.executed and self.previous_state:
            city.idle = self.previous_state['idle']
            city.workers = self.previous_state['workers']
            city._sync_population()
            self.executed = False
    
    def __str__(self):
        return f"Asignar {self.amount} obreros"


class BuildCommand(Command):
    """Comando para iniciar construcción de un edificio"""
    
    def __init__(self, building_type):
        self.building_type = building_type
        self.executed = False
        self.created_building = None
        self.building_map = {
            "1": "escuela",
            "2": "laboratorio", 
            "3": "club",
            "4": "Poligono"
        }
    
    def execute(self, city):
        # Convertir selección a tipo de edificio
        if self.building_type in self.building_map:
            building_type_key = self.building_map[self.building_type]
        else:
            # Si ya viene como clave directa (escuela, laboratorio, etc.)
            building_type_key = self.building_type
        
        if building_type_key not in BUILDING_TYPES:
            print(f"Tipo de edificio '{building_type_key}' no válido")
            return False
        
        building_info = BUILDING_TYPES[building_type_key]
        
        # Verificar recursos
        if city.food < building_info["food_cost"]:
            print(f"No hay suficiente comida. Necesitas {building_info['food_cost']}")
            return False
        
        if city.workers < building_info["workers_required"]:
            print(f"No hay suficientes obreros. Necesitas {building_info['workers_required']}")
            return False
        
        # Crear el edificio
        self.created_building = Building(
            name=building_info["name"],
            food_cost=building_info["food_cost"],
            build_time=building_info["build_time"],
            workers_required=building_info["workers_required"]
        )
        
        # Consumir recursos
        city.food -= building_info["food_cost"]
        city.buildings.append(self.created_building)
        
        self.executed = True
        print(f"¡{building_info['name']} en construcción! ({building_info['build_time']} turnos)")
        return True
    
    def undo(self, city):
        if self.executed and self.created_building:
            # Devolver recursos
            city.food += self.created_building.food_cost
            
            # Remover edificio si existe
            if self.created_building in city.buildings:
                city.buildings.remove(self.created_building)
            
            self.executed = False
            print(f"Construcción de {self.created_building.name} cancelada")
    
    def __str__(self):
        building_name = "edificio"
        if self.building_type in self.building_map:
            key = self.building_map[self.building_type]
            if key in BUILDING_TYPES:
                building_name = BUILDING_TYPES[key]["name"]
        return f"Construir {building_name}"


class CommandParser:
    """Parser para convertir instrucciones del usuario en comandos"""
    
    @staticmethod
    def parse_instructions(instructions):
        """
        Convierte un diccionario de instrucciones en una lista de comandos
        """
        commands = []
        
        # Asignar granjeros
        farmers = instructions.get("farmers", 0)
        if farmers > 0:
            commands.append(AssignFarmersCommand(farmers))
        
        # Asignar obreros
        workers = instructions.get("workers", 0)
        if workers > 0:
            commands.append(AssignWorkersCommand(workers))
        
        # Construir edificio
        building_choice = instructions.get("building", "0")
        if building_choice != "0":
            commands.append(BuildCommand(building_choice))
        
        return commands