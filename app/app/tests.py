"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        response = calc.add(5, 6)
        self.assertEquals(response, 11)

    def test_subtract_numbers(self):
        response = calc.subtract(10, 15)
        self.assertEquals(-5, response)
