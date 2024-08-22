"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        res = calc.add(6, 4)
        self.assertEqual(res, 10)

    def test_sub_numbers(self):
        """Test that values are subtracted and returned"""
        res = calc.sub(10, 5)
        self.assertEqual(res, 5)

    def test_div_numbers(self):
        """Test that values are divided and returned"""
        res = calc.div(10, 5)
        self.assertEqual(res, 2)

    def test_div_by_zero(self):
        """Test that division by zero raises an error"""
        with self.assertRaises(ValueError):
            calc.div(10, 0)
