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

    if coins:
        treasure += 'Νομίσματα:\n'
        for coin in coins:
            treasure += f'  - {coin}\n'
    else:
        treasure += 'Χωρίς νομίσματα\n'

    if gems:
        treasure += 'Πετράδια:\n'
        for gem in gems:
            treasure += f'  - {gem}\n'
    else:
        treasure += 'Χωρίς πετράδια\n'

    if jewels:
        treasure += 'Κοσμήματα:\n'
        for jewel in jewels:
            treasure += f'  - {jewel}\n'
    else:
        treasure += 'Χωρίς κοσμήματα\n'

    if magic_items:
        treasure += 'Μαγικά αντικείμενα:\n'
        for magic_item in magic_items:
            treasure += f'  - {magic_item}\n'
    else:
        treasure += 'Χωρίς μαγικά αντικείμενα\n'

    atexit.register(remove_treasure_type_file)

    return treasure

if __name__ == "__main__":
    print(create_treasure())
