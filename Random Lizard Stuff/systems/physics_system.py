from components.velocity import Velocity
from components.acceleration import Acceleration

class PhysicsSystem:
    def __init__(self, world, clock):
        self.world = world
        self.clock = clock

    def update(self):
        velocity_entities = set(self.world.components[Velocity].keys())
        acceleration_entities = set(self.world.components[Acceleration].keys())

        accelerated_entities = velocity_entities & acceleration_entities

        for entity_id in accelerated_entities:
            velocity = self.world.components[Velocity][entity_id]
            acceleration = self.world.components[Acceleration][entity_id]

            velocity.x += acceleration.x * self.clock.delta_time
            velocity.y += acceleration.y * self.clock.delta_time
            velocity.z += acceleration.z * self.clock.delta_time