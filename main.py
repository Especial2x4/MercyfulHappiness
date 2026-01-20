# main.py
from modelo.City import *
from UI.CLI import *
from data.GameState import *

def main():
    
    cli = CLI()
    city = City(
            name="",
            population=100,
            farmers=0,
            idle=100,
            workers=0,
            food=100,
            happiness_per_capita=0.5
        )
    print("Iniciando nueva partida...")
    cli.enter_city_name(city)
    cli.show_name(city)
    cli.enter_instructions(city)
    cli.show_farmers(city)

if __name__ == "__main__":
    main()