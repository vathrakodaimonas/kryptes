import random
from generators.magic_items.magic_weapons import *


class MagicWeaponGenerator:
    def __init__(self):
        self.magic_weapons_attribute_list = [
            "Καταραμένο",
            "Ειδικό",
            'Μαγικό'
        ]
        self.magic_weapons_type_list = ['Ακόντιο', 'Σφύρα', 'Απελατίκι', 'Ράβδος', 'Σαλίβα', 'Ρομφαία', 'Λογχοπέλεκυς',
                                        'Ξίφος',
                                        'Βέλη', 'Σφαιρίδια', 'Σπάθη', 'Σφενδόνη', 'Δορυδρέπανο', 'Τζάγγρα',
                                        'Εγχειρίδιο',
                                        'Τόξο',
                                        'Δόρυ', 'Τόξο, σύνθετο', 'Μύδροι', 'Τσεκούρι', 'Μάχαιρα', 'Φαλξ', 'Πέλεκυς']
        self.magic_weapon_bonus = [
            '+1',
            '+2',
            '+3'
        ]
        self.magic_weapon = ''
        self.magic_weapon_type = ''.join(random.choices(self.magic_weapons_attribute_list, weights=[0.2, 0.1, 0.7]))

    def determine_magic_weapon(self):
        if self.magic_weapon_type == 'Ειδικό':
            self.magic_weapon = SpecialWeaponGenerator().determine_special_weapon()

        elif self.magic_weapon_type == 'Μαγικό':
            self.magic_weapon = ''.join(random.choices(self.magic_weapons_type_list,
                                                       weights=[0.03, 0.08, 0.03, 0.03, 0.08, 0.05, 0.03, 0.05, 0.08,
                                                                0.05, 0.03,
                                                                0.03, 0.03, 0.03, 0.03, 0.08, 0.03, 0.03, 0.03, 0.05,
                                                                0.03, 0.05,
                                                                0.03])
                                        ) + ' ' + ''.join(
                random.choices(self.magic_weapon_bonus, weights=[0.68, 0.16, 0.16]))

        elif self.magic_weapon_type == "Καταραμένο":
            self.magic_weapon = f"{self.magic_weapon_type}: {random.choice(self.magic_weapons_type_list)}"

        return self.magic_weapon
