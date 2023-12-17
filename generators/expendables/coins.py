from generators.utils.dice import Dice


class CoinGenerator:
    def __init__(self):
        self.bronze_coins_list = [
            20, 200, 400, 600, 1000, 1400, 1800, 2400, 3000, 3600, 5000, 6000, 8000,
            100000, 140000, 200000
        ]
        self.silver_coins_list = [
            10, 100, 200, 300, 500, 700, 900, 1200, 1500, 1800, 2500, 3000, 4000, 5000,
            7500, 10000
        ]
        self.gold_coins_list = [
            1, 10, 20, 30, 50, 70, 90, 120, 150, 180, 250, 300, 400, 500, 750, 1000
        ]

    def generate_coins(self, treasure_type: int):
        coins = []
        # bronze coins
        result_bronze_coins = Dice.two_D6()
        if result_bronze_coins >= 8:
            bronze_coins = f'Χάλκινα νομίσματα: {Dice.one_D6() * self.bronze_coins_list[treasure_type]}'
            if bronze_coins:
                coins.append(bronze_coins)

        # silver coins
        silver_coins_result = Dice.two_D6()
        if silver_coins_result >= 8:
            silver_coins = f'Αργυρά νομίσματα: {Dice.one_D6() * self.silver_coins_list[treasure_type]}'
            if silver_coins:
                coins.append(silver_coins)

        # silver coins
        gold_coins_result = Dice.two_D6()
        if gold_coins_result >= 9:
            gold_coins = f'Χρυσά νομίσματα: {Dice.one_D6() * self.gold_coins_list[treasure_type]}'
            if gold_coins:
                coins.append(gold_coins)

        return coins
