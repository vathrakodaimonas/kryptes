# Imports
import random

class Dice:
    @staticmethod
    def one_D6():
        return random.randint(1, 6)

    @staticmethod
    def two_D6():
        return random.randint(2, 12)

    @staticmethod
    def d66():
        tens_digit = random.randint(1, 6)
        ones_digit = random.randint(1, 6)
        result = int(str(tens_digit) + str(ones_digit))
        return int(result)