class Clock:
    def __init__(self):
        self.simulation_time = 0.0
        self.delta_time = 0.01

    def tick(self):
        self.simulation_time += self.delta_time