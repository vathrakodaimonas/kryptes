from generators.expendables import *
from generators.magic_items import *


if __name__ == "__main__":
    coin_generator = CoinGenerator()
    coin_generator.generate_coins()

    gem_generator = GemGenerator()
    gem_generator.generate_gems()

    jewelry_roller = JewelryRoller()
    jewelry_roller.roll_and_print()

    magic_item_roller = MagicItemGenerator()
    magic_item_roller.determine_magic_item()
    b=1
