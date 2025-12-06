
# Este sirve mucho para mostrar los reportes en ui

class ReportService:
    def __init__(self):
        pass

    def generate(self, city, balance, crecimiento):
        # Formatear la comida
        comida_formateada = round(city.food, 2)
        
        # Información de edificios
        buildings_in_progress = []
        buildings_completed = []
        
        for building in city.buildings:
            if building.completed:
                buildings_completed.append(building.name)
            else:
                buildings_in_progress.append(f"{building.name} ({building.get_progress()})")
        
        return {
            "ciudad": city.name,
            "poblacion": city.population,
            "granjeros": city.farmers,
            "obreros": city.workers,  # Nuevo campo
            "ociosos": city.idle,
            "comida": comida_formateada,
            "balance_comida": balance,
            "crecimiento": crecimiento,
            "felicidad": city.happiness,  # Nuevo campo
            "edificios_en_construccion": buildings_in_progress if buildings_in_progress else "Ninguno",
            "edificios_completados": buildings_completed if buildings_completed else "Ninguno"
        }