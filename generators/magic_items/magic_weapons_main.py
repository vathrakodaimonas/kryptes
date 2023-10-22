import random
from generators.magic_items.magic_weapons import *

magic_weapons_attribute_list = [
    "Καταραμένο",
    "Ειδικό",
    'Μαγικό'
]

magic_weapons_type_list = ['Ακόντιο', 'Σφύρα', 'Απελατίκι', 'Ράβδος', 'Σαλίβα', 'Ρομφαία', 'Λογχοπέλεκυς', 'Ξίφος',
                           'Βέλη', 'Σφαιρίδια', 'Σπάθη', 'Σφενδόνη', 'Δορυδρέπανο', 'Τζάγγρα', 'Εγχειρίδιο', 'Τόξο',
                           'Δόρυ', 'Τόξο, σύνθετο', 'Μύδροι', 'Τσεκούρι', 'Μάχαιρα', 'Φαλξ', 'Πέλεκυς']

magic_weapon_bonus = [
    '+1',
    '+2',
    '+3'
]


def determine_magic_weapon():
    magic_weapon_type = ''.join(random.choices(magic_weapons_attribute_list, weights=[0.2, 0.1, 0.7]))
    magic_weapon = ''

    if magic_weapon_type == 'Ειδικό':
        magic_weapon = determine_special_weapon()

    elif magic_weapon_type == 'Μαγικό':
        magic_weapon = ''.join(random.choices(magic_weapons_type_list,
                                              weights=[0.03, 0.08, 0.03, 0.03, 0.08, 0.05, 0.03, 0.05, 0.08, 0.05, 0.03,
                                                       0.03, 0.03, 0.03, 0.03, 0.08, 0.03, 0.03, 0.03, 0.05, 0.03, 0.05,
                                                       0.03])
                               ) + ' ' + ''.join(random.choices(magic_weapon_bonus, weights=[0.68, 0.16, 0.16]))

    elif magic_weapon_type == "Καταραμένο":
        magic_weapon = f"{magic_weapon_type}: {random.choice(magic_weapons_type_list)}"
    print(magic_weapon)
    return magic_weapon
