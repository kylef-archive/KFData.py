import unittest

from kfdata.entity import Entity


class EntityTests(unittest.TestCase):
    def setUp(self):
        self.entity = Entity(name='Person')

    def test_creation(self):
        self.assertEqual(self.entity.name, 'Person')
        self.assertEqual(self.entity.represented_class_name, 'Person')
        self.assertEqual(self.entity.parent_entity, None)
        self.assertEqual(self.entity.is_abstract, False)

    def test_str(self):
        self.assertEqual(str(self.entity), 'Person')

    def test_repr(self):
        self.assertEqual(repr(self.entity), '<Entity Person>')

    def test_equality(self):
        self.assertEqual(self.entity, Entity(name='Person'))

    def test_inequality(self):
        self.assertNotEqual(self.entity, Entity(name='Person', is_abstract=True))

