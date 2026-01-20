class City:
    def __init__(
        self,
        name,
        population,
        farmers,
        workers,
        idle,
        food,
        happiness_per_capita,
        happiness
    ):
        self.name = name

        self.farmers = farmers
        self.workers = workers
        self.idle = idle
        self.population = population

        self.food = food
        self.consumo_per_capita = 0.25

        self.happiness_per_capita = happiness_per_capita
        self.happiness = happiness

        self.buildings = []

        self._validate()

    # --------------------
    # VALIDACIÓN CENTRAL
    # --------------------
    def _validate(self):
        if self.farmers + self.workers + self.idle != self.population:
            raise ValueError("Estado inconsistente de población")

        if min(self.farmers, self.workers, self.idle, self.population, self.food) < 0:
            raise ValueError("Valores negativos inválidos")

    # --------------------
    # ASIGNACIONES
    # --------------------
    def assign_farmers(self, amount):
        if amount <= 0 or self.idle < amount:
            return False

        self.idle -= amount
        self.farmers += amount
        self._validate()
        return True

    def assign_workers(self, amount):
        if amount <= 0 or self.idle < amount:
            return False

        self.idle -= amount
        self.workers += amount
        self._validate()
        return True

    # --------------------
    # PRODUCCIÓN / CONSUMO
    # --------------------
    def produce_food(self):
        produced = self.farmers * 2
        self.food += produced
        return produced

    def consume_food(self):
        consumed = self.population * self.consumo_per_capita
        self.food -= consumed
        return consumed

    # --------------------
    # CRECIMIENTO
    # --------------------
    def apply_population_growth(self):
        balance = self.farmers * 2 - self.population * self.consumo_per_capita

        if balance <= 0:
            loss = min(5, int(abs(balance) // 10))
            self._decrease_population(loss)
            return -loss

        growth = min(3, int(balance // 20))
        self.idle += growth
        self.population += growth
        self._validate()
        return growth

    def _decrease_population(self, amount):
        for _ in range(amount):
            if self.idle > 0:
                self.idle -= 1
            elif self.workers > 0:
                self.workers -= 1
            elif self.farmers > 0:
                self.farmers -= 1

            self.population -= 1

        self._validate()

    # --------------------
    # CONSTRUCCIÓN
    # --------------------
    def start_building(self, building):
        if self.food < building.food_cost:
            return False
        if self.workers < building.workers_required:
            return False

        self.food -= building.food_cost
        self.buildings.append(building)
        return True

    def process_buildings(self):
        completed = []
        for b in self.buildings:
            if not b.completed and b.work_on():
                if b.completed:
                    completed.append(b.name)
        return completed


