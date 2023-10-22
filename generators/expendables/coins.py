from generators.utils.dice import Dice
from treasuretype import define_treasure_type

class CoinGenerator:
    def __init__(self):
        self.bronze_coins_list = [
            20, 200, 400, 600, 1000, 1400, 1800, 2400, 3000, 3600, 5000, 6000, 8000,
            100000, 140000, 200000,
        ]
        self.silver_coins_list = [
            10, 100, 200, 300, 500, 700, 900, 1200, 1500, 1800, 2500, 3000, 4000, 5000,
            7500, 10000,
        ]
        self.gold_coins_list = [
            1, 10, 20, 30, 50, 70, 90, 120, 150, 180, 250, 300, 400, 500, 750, 1000,
        ]
        self.bronze_coins_sum = 0
        self.silver_coins_sum = 0
        self.gold_coins_sum = 0
        self.treasure_type = None

    def generate_coins(self):
        if self.treasure_type is None:
            self.treasure_type = define_treasure_type()

        self.bronze_coins()
        self.silver_coins()
        self.gold_coins()

    def bronze_coins(self):
        result = Dice.twoD6()
        print(f'Dice result: {result}')
        one_d6 = int(Dice.oneD6())
        if result >= 8:
            self.bronze_coins_sum = one_d6 * self.bronze_coins_list[self.treasure_type]
            print(f'Bronze coins: {self.bronze_coins_sum}')
        else:
            self.bronze_coins_sum = 0
            print('No bronze coins')
        return self.bronze_coins_sum

    def silver_coins(self):
        result = Dice.twoD6()
        print(f'Dice result: {result}')
        one_d6 = int(Dice.oneD6())
        if result >= 8:
            self.silver_coins_sum = one_d6 * self.silver_coins_list[self.treasure_type]
            print(f'Silver coins: {self.silver_coins_sum}')
        else:
            self.silver_coins_sum = 0
            print('No silver coins')
        return self.silver_coins_sum

    def gold_coins(self):
        result = Dice.twoD6()
        print(f'Dice result: {result}')
        one_d6 = int(Dice.oneD6())
        if result >= 9:
            self.gold_coins_sum = one_d6 * self.gold_coins_list[self.treasure_type]
            print(f'Gold coins: {self.gold_coins_sum}')
        else:
            self.gold_coins_sum = 0
            print('No gold coins')
        return self.gold_coins_sum

