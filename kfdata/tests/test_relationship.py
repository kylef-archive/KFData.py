import unittest

from kfdata.relationship import Relationship


class RelationshipTests(unittest.TestCase):
    def setUp(self):
        self.relationship = Relationship(name='owner')

    def test_creation(self):
        self.assertEqual(self.relationship.name, 'owner')

    def test_str(self):
        self.assertEqual(str(self.relationship), 'owner')

    def test_repr(self):
        self.assertEqual(repr(self.relationship), '<Relationship owner>')

    def test_equality(self):
        self.assertEqual(self.relationship, Relationship(name='owner'))

    def test_inequality(self):
        self.assertNotEqual(self.relationship, Relationship(name='otherOwner'))

    def test_relstionship_to_many(self):
        self.assertTrue(self.relationship.is_to_many)
        self.assertFalse(self.relationship.is_to_one)

    def test_relstionship_to_one(self):
        relationship = Relationship(name='owner', maximum_count=1)
        self.assertFalse(relationship.is_to_many)
        self.assertTrue(relationship.is_to_one)
