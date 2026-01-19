# MercyfulHappiness/core/command_manager.py
class CommandManager:
    """Maneja la ejecución y historial de comandos"""
    
    def __init__(self):
        self.history = []  # Historial de todos los comandos ejecutados
        self.undo_stack = []  # Pila para redo
    
    def execute_command(self, command, city):
        """Ejecuta un comando y lo guarda en el historial"""
        if command.execute(city):
            self.history.append(command)
            self.undo_stack.clear()  # Limpiar redo stack al ejecutar nuevo comando
            return True
        return False
    
    def undo_last(self, city):
        """Deshace el último comando ejecutado"""
        if self.history:
            command = self.history.pop()
            command.undo(city)
            self.undo_stack.append(command)
            return True
        return False
    
    def redo_last(self, city):
        """Rehace el último comando deshecho"""
        if self.undo_stack:
            command = self.undo_stack.pop()
            if command.execute(city):
                self.history.append(command)
                return True
        return False
    
    def get_command_history(self, limit=10):
        """Obtiene el historial reciente de comandos"""
        return self.history[-limit:] if self.history else []
    
    def clear_history(self):
        """Limpia todo el historial"""
        self.history.clear()
        self.undo_stack.clear()