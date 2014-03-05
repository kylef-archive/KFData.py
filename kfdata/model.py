class Model(object):
    def __init__(self, entities=None):
      self.entities = entities or []

    def __repr__(self):
      return '<Model %s>' % self.entities

    def __eq__(self, other):
      return self.entities == other.entities

    def find_entity(self, entity_name):
        for entity in self.entities:
            if entity.name == entity_name:
                return entity
