# city.py - eliminar métodos redundantes
class City:
    def __init__(self, name, population, farmers, idle, workers, food, happiness_per_capita, total_happiness):
        self.name = name
        self.population = population
        self.population_factor = 1
        self.farmers = farmers
        self.idle = idle
        self.workers = workers
        self.food = food
        self.happiness_per_capita = happiness_per_capita
        self.total_happiness = total_happiness

    #===========================================================================================
    # -------------------------------- SETERS Y GETERS -----------------------------------------
    #===========================================================================================

    def set_name(self, city_name):
        self.name = city_name

    def get_name(self):
        return self.name
    
    def set_population(self, amount):
        self.population = amount

    def get_population(self):
        return self.population
    
    def set_farmers(self, amount):
        self.farmers = self.farmers + amount
        
    def get_farmers(self):
        return self.farmers
    
    def set_idle(self, amount):
        self.idle = self.idle - amount

    def get_idle(self):
        return self.idle
    
    def set_workers(self):
        return self.workers
    
    def set_food(self,amount):
        self.food = self.food + amount
    
    def get_food(self):
        return self.food
    
    def set_happiness_per_capita(self,amount):
        self.happiness_per_capita = self.happiness_per_capita + amount

    def get_happiness_per_capita(self):
        return self.happiness_per_capita
    
    def set_total_happiness(self):
        self.total_happiness = self.happiness_per_capita * 100

    def get_total_happiness(self):
        return self.total_happiness
