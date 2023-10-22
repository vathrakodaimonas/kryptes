import random

from generators.utils.dice import Dice


class MagicArmourGenerator():
    def __init__(self):
        self.magic_armour_type_light_list = ['Σκουτάρι', 'Σκούτα', 'Δερμάτινη', 'Καββάδιο']
        self.special_armours_list = [
            'Αιθέριος Θώρακας',
            'Αποτρόπαιος Θώρακας',
            'Ασπίδα Εκτροπής',
            'Δρακόντειο Δέρας',
            'Μαγνητικός Θώρακας',
            'Πανοπλία των Ματιών',
            'Τελχινοθώραξ',
            'Φιδοπουκάμισο',
            'Φτερωτός Θώρακας'
        ]
        self.magic_armour_types_list = [
            'Καταραμένη',
            'Ειδική',
            'Μαγική'
        ]
        self.magic_armour_equipment_list = [
            'Σκουτάρι',
            'Σκούτα',
            'Θυρεός',
            'Δερμάτινη',
            'Καββάδιο',
            'Λωρίκιο',
            'Ζάβα',
            'Κλιβάνιο',
        ]
        self.magic_armour = ''

    def determine_magic_armour(self):

        magic_armour_equipment_type = ''
        magic_armour_bonus = ''

        magic_armour_type = ' '.join(random.choices(self.magic_armour_types_list, weights=[0.16, 0.083, 0.757]))

        if magic_armour_type == 'Ειδική':
            magic_armour_equipment_type = random.choice(self.special_armours_list)

        elif magic_armour_type == 'Μαγική':
            magic_armour_equipment_type = ' '.join(random.choices(self.magic_armour_equipment_list,
                                                                  weights=[0.083, 0.13, 0.05, 0.05, 0.1, 0.22, 0.22,
                                                                           0.1]))

            if magic_armour_equipment_type in self.magic_armour_type_light_list:
                magic_armour_bonus = '+1'
            else:
                result = Dice.two_D6()
                if result >= 10:
                    magic_armour_bonus = '+1'
                else:
                    magic_armour_bonus = '+2'
        else:
            magic_armour_equipment_type = magic_armour_type + ' θωράκιση: ' + random.choice(
                self.magic_armour_equipment_list)

        self.magic_armour = magic_armour_equipment_type + ' ' + magic_armour_bonus

        return self.magic_armour
