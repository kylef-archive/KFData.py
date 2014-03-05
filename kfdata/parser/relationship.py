from kfdata.relationship import Relationship


class RelationshipParser(object):
    @classmethod
    def parse(cls, document):
        name = document.getAttribute('name')

        minimum_count = document.getAttribute('minCount')
        if len(minimum_count):
            minimum_count = int(minimum_count)
        else:
            minimum_count = 0

        maximum_count = document.getAttribute('maxCount')
        if len(maximum_count):
            maximum_count = int(maximum_count)
        else:
            maximum_count = 0

        is_optional = document.getAttribute('optional') == 'YES'
        is_ordered = document.getAttribute('ordered') == 'YES'

        return Relationship(name=name, minimum_count=minimum_count,
                            maximum_count=maximum_count,
                            is_optional=is_optional, is_ordered=is_ordered)
