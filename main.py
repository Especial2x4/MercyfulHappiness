# main.py
from modelo.City import *
from UI.CLI import *
from data.GameState import *
from data.config import *

import math

def main():
    

    game_state = GameState()
    cli = CLI()

    # Cargar o nueva partida
    saved = game_state.load()

    if(saved):
        city_data = saved["city"]
        city = City(
            name=city_data["name"],
            population=city_data["population"],
            farmers=city_data["farmers"],
            idle=city_data["idle"],
            workers=city_data.get("workers", 0),
            food=city_data["food"],
            happiness_per_capita=city_data["happiness_per_capita"],
            total_happiness=["total_happiness"])
    else:
        # Si no hay partida guardada se crea un nuevo objeto city
        city = City(
            name="",
            population=100,
            farmers=0,
            idle=100,
            workers=0,
            food=100,
            happiness_per_capita=HAPPINESS_PER_CAPITA,
            total_happiness=50
        )
        print("Iniciando nueva partida...")

        cli.enter_city_name(city)

    
    
    cli.show_name(city)
    cli.enter_instructions(city)
    food_consumo_por_turno(city)
    calculo_de_felicidad_por_turno(city)
    calculo_felicidad_total(city)
    
    print(f"la cantidad total de granjeros es : {city.get_farmers()}")
    print(f"la cantidad total de idles es : {city.get_idle()}")
    print(f"Ahora hay : {city.get_food()} puntos de comida")
    print(f"Ahora la población de es de : {city.get_population()}")
    print(f"El balance de comida es : {balance_de_comida(city)}")
    print(f"La cantidad de comida total es : {city.get_food()}")
    print(f"La felicidad per cápita es : {math.trunc(city.get_happiness_per_capita() * 10**2) / 10**2}")
    print(f"La felicidad total es : {city.get_total_happiness()}")

    game_state.save(city)

if __name__ == "__main__":
    main()