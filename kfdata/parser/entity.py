from kfdata.entity import Entity
from kfdata.parser.attributes import AttributeParser
from kfdata.parser.relationship import RelationshipParser

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

        entity.relationships = [RelationshipParser.parse(relationship_document) \
                for relationship_document in relationship_documents]

        return entity
