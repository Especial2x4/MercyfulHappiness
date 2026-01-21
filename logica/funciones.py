
# logica/funciones.py
from modelo.City import *
from data.config import *

def asignacion_de_granjeros(city, amount):

    # 1- sumar la cantidad de granjeros siempre y cuando haya idles disponibles
    if(validacion_de_idles(city,amount) == True):
        city.set_farmers(amount) # se asigna la nueva cantidad de granjeros
        city.set_idle(amount) # se quita la cantidad a los idles
        # Cada granjero asignado produce 2 puntos de comida por turno
        factor_por_granjero = FACTOR_PRODUCCION_POR_GRANJERO
        granjeros_asignados = amount 
        food_production = factor_por_granjero * granjeros_asignados
        city.set_food(food_production)
    else:
        print("Algo malió sal")


def validacion_de_idles(city, amount):

    if city.get_idle() >= amount:
        print("hay suficientes idles")
        print(f"idels disponibles {city.get_idle()}")
        return True
    else:
        print("No hay suficientes idles")
        return False


def calculo_de_poblacion(city):
    #Los idles aumentan cuando hay felicidad y disminuyen cuando hay infelicidad
    amount = city.get_idle() + city.get_farmers
    city.set_population(amount)


def calculo_de_felicidad_por_turno(city):
    # Cuando hay balance positivo de comida, la felicidad per capita aumenta 0.01 punto y sino disminuye 0.02 puntos
    if(balance_de_comida(city) == "Positivo"):
        city.set_happiness_per_capita(0.01)
    else:
        city.set_happiness_per_capita(0 - 0.02)


def balance_de_comida(city):
    # Se calcula por turno, si la comida almacenada es mayor a la comida consumida el balance es positivo
    # si es al revés el balance es negativo
    food_balance = city.get_food() - city.get_population()
    if(food_balance >= 0):
        return "Positivo"
    else:
        return "Negativo"
    

def food_consumo_por_turno(city):
    # El consumo por turno se calcula multiplicando la población por el consumo per cápita
    consumo_per_capita = CONSUMO_PER_CAPITA
    consumo_total_por_turno = city.get_population() * consumo_per_capita
    # Se transforma en negativo para que se reste en el seter de city
    consumo_total_por_turno_parseado = 0 - consumo_total_por_turno
    city.set_food(consumo_total_por_turno_parseado)
