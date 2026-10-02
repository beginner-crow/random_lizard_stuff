from engine.spacetime import Spacetime
from engine.world import World
from systems.movement_system import MovementSystem
from systems.physics_system import PhysicsSystem

class Simulation: 
    def __init__(self): 
        self.world = World() 
        self.spacetime = Spacetime() 
        self.systems = [ 
            MovementSystem(self.world, self.spacetime.clock), 
            PhysicsSystem(self.world, self.spacetime.clock) ] 
        self.agents = {} 
        
    def tick(self): 
        self.spacetime.clock.tick() 
        for system in self.systems: 
            system.update()