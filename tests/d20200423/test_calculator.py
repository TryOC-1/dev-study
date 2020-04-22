import math
import os
import unittest

from d20200423.calculator import Calculator

print(os.curdir)


class CalculatorTest(unittest.TestCase):
    def test_add(self):
        x = 5
        y = 3
        self.assertEqual(Calculator.add(x, y), x + y)

    def test_sub(self):
        x = 5
        y = 3
        self.assertEqual(Calculator.sub(x, y), x - y)

    def test_mul(self):
        x = 5
        y = 3
        self.assertEqual(Calculator.mul(x, y), x * y)

    def test_div(self):
        x = 5
        y = 3
        self.assertEqual(Calculator.div(x, y), x / y)

    def test_sqrt(self):
        x = 5
        self.assertEqual(Calculator.sqrt(x), math.sqrt(x))


if __name__ == "__main__":
    unittest.main()
