from itemgenerators.coins import CoinGenerator
from itemgenerators.gem import GemGenerator
from itemgenerators.jewels import JewelryRoller


if __name__ == "__main__":
    coin_generator = CoinGenerator()
    coin_generator.generate_coins()

    gem_generator = GemGenerator()
    gem_generator.generate_gems()

    jewelry_roller = JewelryRoller()
    jewelry_roller.roll_and_print()
