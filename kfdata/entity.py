class Entity(object):
    def __init__(self, name, represented_class_name=None, parent_entity=None,
            is_abstract=False, attributes=None, relationships=None):
        self.name = name
        self.represented_class_name = represented_class_name or name
        self.parent_entity = parent_entity
        self.is_abstract = is_abstract
        self.attributes = attributes or []
        self.relationships = relationships or []

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Entity {}>'.format(self.name)

    def __eq__(self, other):
        return isinstance(other, Entity) and \
                other.name == self.name and \
                other.represented_class_name == self.represented_class_name and \
                other.parent_entity == self.parent_entity and \
                other.is_abstract == self.is_abstract and \
                other.attributes == self.attributes and \
                other.relationships == self.relationships

    @property
    def super_class_name(self):
        if self.parent_entity:
            return self.parent_entity.represented_class_name
        return 'NSManagedObject'
