# main.py
from models.city import City
from services.report_service import ReportService
from core.turn_processor import TurnProcessor
from core.game_manager import GameManager
from ui.cli import CLI
from data.gamestate import GameState

def main():
    # Inicializar servicios
    game_state = GameState()
    cli = CLI()
    
    # Cargar o nueva partida
    saved = game_state.load()
    if saved:
        city_data = saved["city"]
        city = City(
            name=city_data["name"],
            population=city_data["population"],
            farmers=city_data["farmers"],
            idle=city_data["idle"],
            workers=city_data.get("workers", 0),
            food=city_data["food"],
            happiness_per_capita=city_data["happiness_per_capita"],
            happiness=city_data["happiness"]

        )
        # Cargar edificios si existen
        if "buildings" in city_data:
            from models.building import Building
            for bld_data in city_data["buildings"]:
                building = Building(
                    name=bld_data["name"],
                    food_cost=bld_data["food_cost"],
                    build_time=bld_data["build_time"],
                    workers_required=bld_data["workers_required"]
                )
                building.progress = bld_data["progress"]
                building.completed = bld_data["completed"]
                city.buildings.append(building)
        
        turn = saved["turn"]
        print(f"Cargando partida guardada (Turno {turn})...")
    else:
        # Si no hay partida guardada se crea un nuevo objeto city
        city = City(
            name=cli.enter_city_name(),
            population=100,
            farmers=0,
            idle=100,
            workers=0,
            food=100,
            happiness_per_capita=0.5,
            happiness=50
        )
        turn = 1
        print("Iniciando nueva partida...")

    # Inicializar servicios y procesador

    report_service = ReportService()
    processor = TurnProcessor()
    
    # Inicializar game manager
    manager = GameManager(city, processor, report_service)
    manager.turn = turn

    # Bucle principal del juego
    for _ in range(10):
        # Obtener instrucciones del usuario
        instructions = cli.enter_instructions()
        
        # Ejecutar turno completo
        report = manager.run_turn(instructions)
        
        # Mostrar resultados
        cli.show_report(report, manager.turn - 1)

    # Guardar partida
    game_state.save(manager.city, manager.turn)
    print("Partida guardada.")

if __name__ == "__main__":
    main()
