class World:
    def __init__(self):
        self.entities = {}
        self.components = {}

    def create_entity(self):
        entity_id = len(self.entities)
        self.entities[entity_id] = {}
        return entity_id
    
    def add_component(self,entity_id,component):
        if type(component) not in self.components:
            self.components[type(component)] = {}
        self.components[type(component)][entity_id] = component
        return entity_id, component