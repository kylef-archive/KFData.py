class Model(object):
    def __init__(self, entities=None):
      self.entities = entities or []

    def __repr__(self):
      return '<Model %s>' % self.entities

    def __eq__(self, other):
      return self.entities == other.entities
