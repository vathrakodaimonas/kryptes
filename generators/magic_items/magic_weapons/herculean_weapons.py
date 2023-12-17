import random


class HerculeanWeaponGenerator:

    def __init__(self):
        self.magic_weapons_type_list = ['Ακόντιο', 'Σφύρα', 'Απελατίκι', 'Ράβδος', 'Σαλίβα', 'Ρομφαία', 'Λογχοπέλεκυς',
                                        'Ξίφος',
                                        'Βέλη', 'Σφαιρίδια', 'Σπάθη', 'Σφενδόνη', 'Δορυδρέπανο', 'Τζάγγρα',
                                        'Εγχειρίδιο', 'Τόξο',
                                        'Δόρυ', 'Τόξο, σύνθετο', 'Μύδροι', 'Τσεκούρι', 'Μάχαιρα', 'Φαλξ', 'Πέλεκυς']
        self.magic_weapon_bonus = [
            '+1',
            '+2',
            '+3'
        ]
        self.magic_weapon_herculean = ''

    def determine_herculean_weapon(self):
        self.magic_weapon_herculean = 'Κρατερό: ' + random.choice(self.magic_weapons_type_list) + ' ' + ''.join(
            random.choices(
                self.magic_weapon_bonus, weights=[0.6, 0.25,
                                                  0.15]))

        return self.magic_weapon_herculean
