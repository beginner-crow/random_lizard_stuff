from engine.simulation import Simulation
from components.position import Position
from components.velocity import Velocity

simulation = Simulation()

entity1 = simulation.world.create_entity()
entity2 = simulation.world.create_entity()
simulation.world.add_component(entity1, Position())
simulation.world.add_component(entity2, Position())
simulation.world.add_component(entity1, Velocity())
simulation.world.add_component(entity2, Velocity())
simulation.world.components[Position][entity1].x = 10
simulation.world.components[Velocity][entity2].y = 20

print (simulation)
print (simulation.world)
print (simulation.world.entities)
print (simulation.world.components)

print(simulation.world.entities)
while simulation.spacetime.clock.simulation_time < 1:
    simulation.tick()
print(simulation.spacetime.clock.simulation_time)
print(simulation.world.components[Position][entity1].x)
print(simulation.world.components[Velocity][entity2].y)
print(simulation.world.components[Position][entity2].y)
print(simulation.world.components[Position].keys())
print(simulation.world.components[Velocity].keys())