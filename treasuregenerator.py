from generators import CoinGenerator
from generators import GemGenerator
from generators import JewelryRoller


if __name__ == "__main__":
    coin_generator = CoinGenerator()
    coin_generator.generate_coins()

    gem_generator = GemGenerator()
    gem_generator.generate_gems()

    jewelry_roller = JewelryRoller()
    jewelry_roller.roll_and_print()
