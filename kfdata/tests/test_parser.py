import os
import unittest

from kfdata.parser import ModelParser
from kfdata.model import Model
from kfdata.entity import Entity
from kfdata.attributes import *
from kfdata.relationship import Relationship


class ModelParserTests(unittest.TestCase):
    def fixture_model(self):
        model = Model()
        model.entities = [
            Entity('Company', attributes=[
                StringAttribute('name'),
            ], relationships=[
                Relationship('jobs', is_optional=True, is_ordered=True),
            ]),

            Entity('Job', attributes=[
                BooleanAttribute('manager', default_value=False),
                FloatAttribute('salary', default_value=0.0),
            ], relationships=[
                Relationship('company', is_optional=True, maximum_count=1),
                Relationship('person', is_optional=True, maximum_count=1),
            ]),

            Entity('Person', attributes=[
                StringAttribute('firstName', is_optional=True),
                StringAttribute('lastName', is_optional=True),
                StringAttribute('username', is_indexed=True),
            ], relationships=[
                Relationship('job', is_optional=True, maximum_count=1),
            ]),
        ]
        return model


    def test_parser(self):
        base_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
        model_fixture = 'fixtures/KFDataFixture/Model.xcdatamodeld/Model.xcdatamodel/contents'
        filename = os.path.join(base_path, model_fixture)
        model = ModelParser.parse_file(filename)
        self.assertEqual(model, self.fixture_model())
