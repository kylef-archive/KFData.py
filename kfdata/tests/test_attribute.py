import unittest

from kfdata.attributes import Attribute, NumberAttribute, BooleanAttribute


class AttributeTests(unittest.TestCase):
    def setUp(self):
        self.attribute = Attribute(name='firstName', is_indexed=True, is_optional=False)

    def test_creation(self):
        self.assertEqual(self.attribute.name, 'firstName')
        self.assertTrue(self.attribute.is_indexed)
        self.assertFalse(self.attribute.is_optional)
        self.assertFalse(self.attribute.is_transient)

    def test_str(self):
        self.assertEqual(str(self.attribute), 'firstName')

    def test_repr(self):
        self.assertEqual(repr(self.attribute), '<Attribute firstName>')

    def test_equality(self):
        self.assertEqual(self.attribute, Attribute(name='firstName',
            is_indexed=True, is_optional=False))

    def test_inequality(self):
        self.assertNotEqual(self.attribute, Attribute(name='firstName',
            is_indexed=True, is_optional=True))

class NumberAttributeTests(unittest.TestCase):
    def test_creation(self):
        attribute = NumberAttribute('age', minimum_value=5, maximum_value=10)
        self.assertEqual(attribute.name, 'age')
        self.assertEqual(attribute.default_value, 0)
        self.assertEqual(attribute.minimum_value, 5)
        self.assertEqual(attribute.maximum_value, 10)

class BooleanAttributeTests(unittest.TestCase):
    def test_default(self):
        attribute = BooleanAttribute('isHuman')
        self.assertEqual(attribute.default_value, False)

