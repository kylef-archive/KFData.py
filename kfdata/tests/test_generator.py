import unittest
import os
from tempfile import NamedTemporaryFile

from kfdata.entity import Entity
from kfdata.attributes import StringAttribute
from kfdata.relationship import Relationship
from kfdata.generator import EntityInterfaceWriter, EntityImplementationWriter

class GeneratorTests(unittest.TestCase):
    def fixture_entity(self):
        return Entity('Person', attributes=[
            StringAttribute('firstName', is_optional=True),
            StringAttribute('lastName', is_optional=True),
            StringAttribute('username', is_indexed=True),
        ], relationships=[
            Relationship('companies', 'Company', is_optional=True, is_ordered=True),
            Relationship('parent', 'Person', is_optional=False, maximum_count=1)
        ])

    def test_entity_header_writer(self):
        with NamedTemporaryFile() as fd:
            writer = EntityInterfaceWriter(self.fixture_entity())
            writer.write(fd.name)

            base_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
            model_fixture = 'fixtures/Person.h'
            filename = os.path.join(base_path, model_fixture)

            with open(filename) as fixture:
                self.assertEqual(fd.read(), fixture.read())

    def test_entity_implementation_writer(self):
        with NamedTemporaryFile() as fd:
            writer = EntityImplementationWriter(self.fixture_entity())
            writer.write(fd.name)

            base_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
            model_fixture = 'fixtures/Person.m'
            filename = os.path.join(base_path, model_fixture)

            with open(filename) as fixture:
                self.assertEqual(fd.read(), fixture.read())
