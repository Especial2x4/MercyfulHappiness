

# city.py - eliminar métodos redundantes
class City:
    def __init__(self, name, population, farmers, idle, workers, food, happiness_per_capita, happiness):
        self.name = name
        self.population = population
        self.population_factor = 1
        self.farmers = farmers
        self.idle = idle
        self.workers = workers
        self.food = food
        self.consumo_per_capita = 0.25
        self.happiness_per_capita = happiness_per_capita
        self.happiness = happiness
        self.buildings = []
        self._sync_population()
        self.happiness_effects = {
            "productivity": 1.0,  # Multiplicador productividad
            "growth": 1.0,       # Multiplicador crecimiento
            "revolt_risk": 0.0   # Riesgo de revuelta
        }

    def _sync_population(self):
        """Asegura que farmers + idle + workers = population"""
        self.population = self.farmers + self.idle + self.workers

    def update_population(self, growth):
        """Actualiza población manteniendo la consistencia"""
        if growth > 0:
            self.idle += growth
        else:
            # Primero quitar de ociosos, luego de obreros, luego de granjeros
            lost = min(self.idle, abs(growth))
            self.idle -= lost
            remaining = abs(growth) - lost
            
            if remaining > 0:
                lost_workers = min(self.workers, remaining)
                self.workers -= lost_workers
                remaining -= lost_workers
            
            if remaining > 0:
                self.farmers = max(0, self.farmers - remaining)
        
        self._sync_population()

    # Eliminar: set_assign_farmers, set_assign_workers, start_building, 
    # set_food_consumer, process_buildings (ahora están en turn_processor)
    
    # Solo mantener getters simples
    def get_food(self):
        return self.food
    
    def get_population_stats(self):
        return {
            "total": self.population,
            "farmers": self.farmers,
            "workers": self.workers,
            "idle": self.idle
        }
    
    def update_happiness_effects(self):
        """Actualizar efectos basados en felicidad"""
        if self.happiness_per_capita < 0.3:
            self.happiness_effects["productivity"] = 0.7
            self.happiness_effects["growth"] = 0.5
            self.happiness_effects["revolt_risk"] = 0.1
        elif self.happiness_per_capita < 0.6:
            self.happiness_effects["productivity"] = 0.9
            self.happiness_effects["growth"] = 0.8
            self.happiness_effects["revolt_risk"] = 0.01
        else:
            self.happiness_effects["productivity"] = 1.2
            self.happiness_effects["growth"] = 1.1
            self.happiness_effects["revolt_risk"] = 0.0

