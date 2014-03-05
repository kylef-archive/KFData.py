from xml.dom.minidom import parse

from kfdata.model import Model
from kfdata.parser.entity import EntityParser


class ModelParser(object):
    @classmethod
    def parse(cls, document):
        models = document.getElementsByTagName('model')

        if len(models) != 1:
            raise Exception('Invalid model file')

        model_document = models[0]
        model = Model()

        entities = []
        for entity_document in model_document.getElementsByTagName('entity'):
            entity = EntityParser.parse(entity_document)
            entities.append(entity)

        model.entities = entities

        for entity in entities:
            for relationship in entity.relationships:
                entity = model.find_entity(relationship.destination_entity)
                relationship.destination_entity_class_name = entity.represented_class_name

        return model


    @classmethod
    def parse_file(cls, filename):
        document = parse(filename)
        return cls.parse(document)
