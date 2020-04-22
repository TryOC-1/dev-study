import math


class Calculator:
    """Simple class implementing a calculator with basic operations."""

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

    @staticmethod
    def mul(x, y):
        return x * y

    @staticmethod
    def div(x, y):
        return x / y

    @staticmethod
    def sqrt(x):
        return math.sqrt(x)
