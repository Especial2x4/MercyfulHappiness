# main.py
from models.city import City
from services.report_service import ReportService
from core.turn_processor import TurnProcessor
from core.game_manager import GameManager
from ui.cli import CLI
from data.gamestate import GameState


def main():
    game_state = GameState()
    cli = CLI()

    saved = game_state.load()

    if saved:
        city_data = saved["city"]

        population = city_data["population"]
        farmers = city_data.get("farmers", 0)
        workers = city_data.get("workers", 0)

        # NORMALIZACIÓN de datos legacy
        idle = population - farmers - workers
        if idle < 0:
            idle = 0

        city = City(
            name=city_data["name"],
            population=population,
            farmers=farmers,
            workers=workers,
            idle=idle,
            food=max(0, city_data["food"]),
            happiness_per_capita=city_data["happiness_per_capita"],
            happiness=city_data["happiness"]
        )

        # Cargar edificios
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
        city_name = cli.enter_city_name()

        city = City(
            name=city_name,
            population=100,
            farmers=0,
            workers=0,
            idle=100,
            food=100,
            happiness_per_capita=0.5,
            happiness=50
        )

        turn = 1
        print("Iniciando nueva partida...")

    report_service = ReportService()
    processor = TurnProcessor()
    manager = GameManager(city, processor, report_service)
    manager.turn = turn

    while True:
        instructions = cli.enter_instructions()
        report = manager.run_turn(instructions)
        cli.show_report(report, manager.turn - 1)

        game_state.save(manager.city, manager.turn)


if __name__ == "__main__":
    main()

