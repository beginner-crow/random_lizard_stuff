from components.position import Position
from components.velocity import Velocity

class MovementSystem:
    def __init__(self, world, clock):
        self.world = world
        self.clock = clock
        
    def update(self):
        position_entities = set(self.world.components[Position].keys())
        velocity_entities = set(self.world.components[Velocity].keys())
       
        moving_entities = position_entities & velocity_entities

        for entity_id in moving_entities:
            position = self.world.components[Position][entity_id]
            velocity = self.world.components[Velocity][entity_id]

            position.x += velocity.x * self.clock.delta_time
            position.y += velocity.y * self.clock.delta_time
            position.z += velocity.z * self.clock.delta_time