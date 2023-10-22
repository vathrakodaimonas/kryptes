from generators.utils.dice import Dice
from generators.magic_items import *



class MagicItemGenerator():
    def __init__(self):
        self.magic_item = ''
    def determine_magic_item(self):
        result = Dice.d66()
        print(f'Dice result is {result}')

        if result in range(11, 24):
            self.magic_item = 'Μαγικό όπλο'
        elif result in range(24, 34):
            self.magic_item = 'Μαγική θωράκιση'
        elif result in range(34, 46):
            self.magic_item = 'Μαγικό φίλτρο'
        elif result in range(46, 57):
            self.magic_item = 'Μαγική περγαμηνή'
        elif result in range(61, 63):
            self.magic_item = 'Μαγικό δακτυλίδι ή φυλακτό'
        elif result in range(63, 65):
            self.magic_item = 'Μαγικό ραβδί ή ράβδος'
        elif result in range(65, 67):
            self.magic_item = 'Διάφορα'
        print(self.magic_item)

        if self.magic_item == 'Διάφορα':
            self.magic_item = MiscMagicItemGenerator().determine_misc_magic_item()
        elif self.magic_item == 'Μαγικό φίλτρο':
            self.magic_item = MagicPotionGenerator().determine_magic_potion()
        elif self.magic_item == 'Μαγικό ραβδί ή ράβδος':
            self.magic_item = MagicRodGenerator().determine_magic_rod()
        elif self.magic_item == 'Μαγικό δακτυλίδι ή φυλακτό':
            self.magic_item = MagicRingGenerator().determine_magic_ring()
        elif self.magic_item == 'Μαγική θωράκιση':
            self.magic_item = MagicArmourGenerator().determine_magic_armour()
        elif self.magic_item == 'Μαγικό όπλο':
            self.magic_item = MagicWeaponGenerator().determine_magic_weapon()

        return self.magic_item
