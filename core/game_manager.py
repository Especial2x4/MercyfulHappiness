
# EL GAMEMANAGER SOLO SE USA PARA LLAMAR AL PROCESADOR DE TURNOS Y AL SERVICIO DE REPORTE

# game_manager.py
class GameManager:
    def __init__(self, city, turn_processor, report_service):
        self.city = city
        self.turn_processor = turn_processor
        self.report_service = report_service
        self.turn = 1

    def run_turn(self, instructions):
        """
        Ejecuta un turno completo
        instructions: dict con acciones del usuario
        """
        # Procesar todas las acciones del turno
        balance_comida, crecimiento = self.turn_processor.process_turn(self.city, instructions)
        
        # Generar reporte
        report = self.report_service.generate(self.city, balance_comida, crecimiento)
        
        self.turn += 1
        return report
