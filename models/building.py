# models/building.py
class Building:
    def __init__(self, name, food_cost, build_time, workers_required):
        self.name = name
        self.food_cost = food_cost
        self.build_time = build_time
        self.workers_required = workers_required
        self.progress = 0
        self.completed = False

    def work_on(self):
        """Avanzar en la construcción"""
        if not self.completed:
            self.progress += 1
            if self.progress >= self.build_time:
                self.completed = True
            return True
        return False

    def get_progress(self):
        return f"{self.progress}/{self.build_time}"