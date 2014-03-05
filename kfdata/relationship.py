class Relationship(object):
    def __init__(self, name, is_optional=False, minimum_count=0, maximum_count=0, is_ordered=False):
        self.name = name
        self.is_optional = is_optional
        self.is_ordered = is_ordered
        self.minimum_count = minimum_count
        self.maximum_count = maximum_count

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Relationship {}>'.format(self.name)

    def __eq__(self, other):
        return self.name == other.name and \
                self.is_optional == other.is_optional and \
                self.minimum_count == other.minimum_count and \
                self.maximum_count == other.maximum_count and \
                self.is_ordered == other.is_ordered

    @property
    def is_to_many(self):
      return self.maximum_count != 1

    @property
    def is_to_one(self):
        return self.maximum_count == 1
