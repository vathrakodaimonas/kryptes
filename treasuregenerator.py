from generators.expendables.coins import CoinGenerator
from generators.expendables.gem import GemGenerator
from generators.expendables.jewels import JewelryRoller


if __name__ == "__main__":
    coin_generator = CoinGenerator()
    coin_generator.generate_coins()

    gem_generator = GemGenerator()
    gem_generator.generate_gems()

    jewelry_roller = JewelryRoller()
    jewelry_roller.roll_and_print()
