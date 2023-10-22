import random

magic_weapons_type_list = ['Ακόντιο', 'Σφύρα', 'Απελατίκι', 'Ράβδος', 'Σαλίβα', 'Ρομφαία', 'Λογχοπέλεκυς', 'Ξίφος',
                           'Βέλη', 'Σφαιρίδια', 'Σπάθη', 'Σφενδόνη', 'Δορυδρέπανο', 'Τζάγγρα', 'Εγχειρίδιο', 'Τόξο',
                           'Δόρυ', 'Τόξο, σύνθετο', 'Μύδροι', 'Τσεκούρι', 'Μάχαιρα', 'Φαλξ', 'Πέλεκυς']

magic_weapon_bonus = [
    '+1',
    '+2',
    '+3'
]


def determine_herculean_weapon():
    magic_weapon_herculean = 'Κρατερό: ' + random.choice(magic_weapons_type_list) + ' ' + ''.join(random.choices(
        magic_weapon_bonus, weights=[0.6, 0.25,
                                     0.15]))
    return magic_weapon_herculean
