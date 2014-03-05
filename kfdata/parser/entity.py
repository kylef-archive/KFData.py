from kfdata.entity import Entity
from kfdata.parser.attributes import AttributeParser


class EntityParser(object):
    @classmethod
    def parse(cls, document):
        entity_name = document.getAttribute('name')
        class_name = document.getAttribute('representedClassName')
        attribute_documents = document.getElementsByTagName('attribute')
        relationship_documents = document.getElementsByTagName('relationship')

        entity = Entity(entity_name, represented_class_name=class_name)

        entity.attributes = [AttributeParser.parse(attribute_document) \
                for attribute_document in attribute_documents]

        return entity

