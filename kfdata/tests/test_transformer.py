import unittest

from kfdata.transformer import ValueTransformer


class ValueTransformerTests(unittest.TestCase):
    def setUp(self):
        self.transformer = ValueTransformer(name='KFColorTransformer')

    def test_creation(self):
        self.assertEqual(self.transformer.name, 'KFColorTransformer')

    def test_str(self):
        self.assertEqual(str(self.transformer), 'KFColorTransformer')

    def test_repr(self):
        self.assertEqual(repr(self.transformer), '<ValueTransformer KFColorTransformer>')


