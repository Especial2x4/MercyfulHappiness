# MercyfulHappiness/ui/cli.py (actualizado)
from modelo.City import *
from logica.funciones import *

class CLI:
    def __init__(self):
        pass

    def enter_city_name(self, city):
        city_name = input("Ingresar el nombre de la ciudad: ")
        city.set_name(city_name)

    # Metodo para debuguear
    def show_name(self, city):
        print(f"El nombre de la ciudad es : {city.get_name()}")

    
    def enter_instructions(self, city):
        print("\n--- Acciones del Turno ---")
        
        # Asignar granjeros
        asigned_farmers = int(input("Asignar granjeros desde ociosos: "))
        asignacion_de_granjeros(city,asigned_farmers)

        
        # Asignar obreros
        #asigned_workers = int(input("Asignar obreros desde ociosos: "))
        
        # Construir edificios
        #print("\n¿Construir edificio?")
        #print("1. Escuela (50 comida, 3 turnos, 2 obreros)")
        #print("2. Laboratorio (100 comida, 5 turnos, 3 obreros)")
        #print("3. Club Recreativo (30 comida, 2 turnos, 1 obrero)")
        #print("4. Poligono (500 comida, 5 turnos, 10 obreros)")
        #print("0. No construir")
        
        #building_choice = input("Selección: ")
        
        # Verificar si es comando especial
        #if building_choice.lower() == 'u':
        #    return {"undo": True}
        
        # Asegurar que devuelve diccionario
        #return {
        #    "farmers": asigned_farmers,
        #    "workers": asigned_workers,
        #    "building": building_choice
        #}

    def show_report(self, report, turn):
        print(f"\n=== Turno {turn} ===")
        print(f"Ciudad: {report['ciudad']}")
        print(f"👨‍👨‍👦- Población: {report['poblacion']}")
        print(f"🧑🏻‍🌾- Granjeros: {report['granjeros']}")
        print(f"👷‍♀️- Obreros: {report['obreros']}")
        print(f"🧏‍♂️- Ociosos: {report['ociosos']}")
        print(f"🥕- Comida: {report['comida']}")
        print(f"😊- Felicidad: {report['felicidad']}")
        print(f"💹🥕- Balance comida: {report['balance_comida']}")
        print(f"📈👨‍👨‍👦- Crecimiento: {report['crecimiento']}")
        print(f"🏦- Edificios en construcción: {report['edificios_en_construccion']}")
        print(f"✅- Edificios completados: {report['edificios_completados']}")
        print("=" * 30)