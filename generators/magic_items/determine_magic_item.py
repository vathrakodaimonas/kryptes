import random

from generators.utils.dice import Dice
from generators.magic_items import *
from generators.spells import SpellGenerator


class MagicItemGenerator():
    def roll_magic_items(self, treasure_type: int):
        treasure_result = Dice.d66()
        print(f'Treasure result is {treasure_result}')
        treasure_type = treasure_type

        if treasure_type == 0 and treasure_result == 66:
            return self.determine_magic_item()
        elif treasure_type == 1 and treasure_result >= 64:
            return self.determine_magic_item()
        elif treasure_type == 2 and treasure_result >= 62:
            return self.determine_magic_item()
        elif treasure_type == 3 and treasure_result >= 56:
            return self.determine_magic_item()
        elif treasure_type == 4 and treasure_result >= 55:
            return self.determine_magic_item()
        elif treasure_type == 5 and treasure_result >= 53:
            return self.determine_magic_item()
        elif treasure_type == 6 and treasure_result >= 52:
            return self.determine_magic_item()
        elif treasure_type == 7 and treasure_result >= 46:
            return self.determine_magic_item()
        elif treasure_type == 8 and treasure_result >= 45:
            return self.determine_magic_item()
        elif treasure_type == 9 and treasure_result >= 43:
            return self.determine_magic_item()
        elif treasure_type == 10 and treasure_result >= 42:
            return self.determine_magic_item()
        elif treasure_type == 11 and treasure_result >= 36:
            return self.determine_magic_item()
        elif treasure_type == 12 and treasure_result >= 35:
            return self.determine_magic_item()
        elif treasure_type == 13 and treasure_result >= 33:
            return self.determine_magic_item()
        elif treasure_type == 14 and treasure_result >= 32:
            return self.determine_magic_item()
        elif treasure_type == 15 and treasure_result >= 26:
            return self.determine_magic_item()

    def determine_magic_item(self):
        treasure_location = input('Enter treasure location (dungeon or wilderness): ')

        if treasure_location.lower() == 'dungeon':
            num_magic_items = random.randint(1, 3)
        elif treasure_location.lower() == 'wilderness':
            num_magic_items = random.randint(1, 6)
        else:
            raise ValueError('Location value not valid')

        magic_items_list = []

        for _ in range(num_magic_items + 1):
            result = Dice.d66()
            if result in range(11, 24):
                magic_item = 'Μαγικό όπλο'
            elif result in range(24, 34):
                magic_item = 'Μαγική θωράκιση'
            elif result in range(34, 46):
                magic_item = 'Μαγικό φίλτρο'
            elif result in range(46, 57):
                magic_item = 'Μαγική περγαμηνή'
            elif result in range(61, 63):
                magic_item = 'Μαγικό δακτυλίδι ή φυλακτό'
            elif result in range(63, 65):
                magic_item = 'Μαγικό ραβδί ή ράβδος'
            elif result in range(65, 67):
                magic_item = 'Διάφορα'

            if magic_item == 'Διάφορα':
                magic_item = MiscMagicItemGenerator().determine_misc_magic_item()
            elif magic_item == 'Μαγικό φίλτρο':
                magic_item = MagicPotionGenerator().determine_magic_potion()
            elif magic_item == 'Μαγικό ραβδί ή ράβδος':
                magic_item = MagicRodGenerator().determine_magic_rod()
            elif magic_item == 'Μαγικό δακτυλίδι ή φυλακτό':
                magic_item = MagicRingGenerator().determine_magic_ring()
            elif magic_item == 'Μαγική θωράκιση':
                magic_item = MagicArmourGenerator().determine_magic_armour()
            elif magic_item == 'Μαγικό όπλο':
                magic_item = MagicWeaponGenerator().determine_magic_weapon()
            elif magic_item == 'Μαγική περγαμηνή':
                magic_item = SpellGenerator().generate_scroll()

            magic_items_list.append(magic_item)

        return magic_items_list
