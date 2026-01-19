# MercyfulHappiness/core/composite_commands.py
from core.commands import Command

class CompositeCommand(Command):
    """Comando que agrupa múltiples comandos"""
    
    def __init__(self, name):
        self.name = name
        self.commands = []
        self.executed = False
    
    def add_command(self, command):
        self.commands.append(command)
    
    def execute(self, city):
        executed_commands = []
        
        for command in self.commands:
            if command.execute(city):
                executed_commands.append(command)
            else:
                # Si falla un comando, deshacer todos los anteriores
                for executed in reversed(executed_commands):
                    executed.undo(city)
                return False
        
        self.executed = True
        return True
    
    def undo(self, city):
        if self.executed:
            for command in reversed(self.commands):
                command.undo(city)
            self.executed = False
    
    def __str__(self):
        return f"{self.name} ({len(self.commands)} sub-comandos)"


class BuildAndAssignCommand(CompositeCommand):
    """Comando para construir y asignar obreros automáticamente"""
    
    def __init__(self, building_type, assign_workers=True):
        super().__init__(f"Construir {building_type} con asignación")
        self.building_type = building_type
        
        if assign_workers:
            # Primero asignar obreros si es necesario
            from core.config import BUILDING_TYPES
            if building_type in BUILDING_TYPES:
                workers_needed = BUILDING_TYPES[building_type]["workers_required"]
                from core.commands import AssignWorkersCommand
                self.add_command(AssignWorkersCommand(workers_needed))
        
        # Luego construir
        from core.commands import BuildCommand
        self.add_command(BuildCommand(building_type))