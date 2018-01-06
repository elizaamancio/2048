import unittest
from board.field import Field

class FieldTest(unittest.TestCase):
    def test_if_field_is_empty(self):
        field = Field(0)
        self.assertEqual(field.value, 0)

    def test_if_double_doubles_0_and_squeeze_equals_true(self):
        field = Field(0)
        field.squeeze()
        self.assertEqual(field.value, 0)
        self.assertEqual(field.squeezed, True)

    def test_if_doubles_1(self):
        field = Field(1)
        field.squeeze()
        self.assertEqual(field.value,2)
        self.assertEqual(field.squeezed, True)



