import atexit

from generators.expendables import *
from generators.magic_items import *
from generators.utils.helper_functions import ask_for_treasure_type, remove_treasure_type_file


def create_treasure():
    treasure_type = ask_for_treasure_type()
    coins = CoinGenerator().generate_coins(treasure_type=treasure_type)
    gems = GemGenerator().generate_gems(treasure_type=treasure_type)
    jewels = JewelryRoller().generate_jewels(treasure_type=treasure_type)
    magic_items = MagicItemGenerator().roll_magic_items(treasure_type=treasure_type)

    treasure = f'Treasure type: {treasure_type}\n'
    treasure += f'Coins: {coins}\n'
    treasure += f'Gems: {gems}\n'
    treasure += f'Jewels: {jewels}\n'

    if magic_items:
        treasure += f'Magic items: {magic_items}'
    else:
        treasure += 'No magic items'

    atexit.register(remove_treasure_type_file)

    return treasure


if __name__ == "__main__":
   print(create_treasure())
