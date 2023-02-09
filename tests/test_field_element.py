import unittest
from strawberrycurve.field_element import FieldElement

y_base = 41

x_0 = 4
x_1 = 12

x_2 = 17
x_3 = 26

x_4 = 32
x_5 = 6

x_6 = 11
x_7 = 29

x_8 = 26
x_9 = 18

x_10 = 16
x_11 = 8
x_12 = 13

x_13 = 5
x_14 = 39

class FieldElementTest(unittest.TestCase):
    def test_field_element_ne(self):
        print(f'[strawberry-curve] Test: FieldElement - equality')
        a = FieldElement(x_0, y_base)
        b = FieldElement(x_0, y_base)
        c = FieldElement(x_1, y_base)
        self.assertEqual(a, b)
        self.assertTrue(a != c)
        self.assertFalse(a != b)

    def test_field_element_add(self):
        print(f'[strawberry-curve] Test: FieldElement - addition')
        a = FieldElement(x_0, y_base)
        b = FieldElement(x_1, y_base)
        self.assertEqual(a + b, FieldElement(((x_0 + x_1) % y_base), y_base))
        a = FieldElement(x_2, y_base)
        b = FieldElement(x_3, y_base)
        self.assertEqual(a + b, FieldElement(((x_2 + x_3) % y_base), y_base))

    def test_field_element_sub(self):
        print(f'[strawberry-curve] Test: FieldElement - subtraction')
        a = FieldElement(x_4, y_base)
        b = FieldElement(x_5, y_base)
        self.assertEqual(a - b, FieldElement(((x_4 - x_5) % y_base), y_base))
        a = FieldElement(x_6, y_base)
        b = FieldElement(x_7, y_base)
        self.assertEqual(a - b, FieldElement(((x_6 - x_7) % y_base), y_base))

    def test_field_element_mul(self):
        print(f'[strawberry-curve] Test: FieldElement - multiplication')
        a = FieldElement(x_8, y_base)
        b = FieldElement(x_9, y_base)
        self.assertEqual(a * b, FieldElement(((x_8 * x_9) % y_base), y_base))

    def test_field_element_pow(self):
        print(f'[strawberry-curve] Test: FieldElement - exponentiation')
        a = FieldElement(x_10, y_base)
        self.assertEqual(a**3, FieldElement(((pow(x_10, (3 % (y_base - 1)), y_base))), y_base))
        a = FieldElement(x_11, y_base)
        b = FieldElement(x_12, y_base)
        self.assertEqual(a**5 * b, FieldElement(((((pow(x_11, (5 % (y_base - 1)), y_base))) * x_12) % y_base), y_base))

    def test_field_element_div(self):
        print(f'[strawberry-curve] Test: FieldElement - division')
        a = FieldElement(x_13, y_base)
        b = FieldElement(x_14, y_base)
        self.assertEqual(a / b, FieldElement((x_13 * pow(x_14, (y_base -2), y_base) % y_base), y_base))
        
if __name__ == '__main__':
    unittest.main()