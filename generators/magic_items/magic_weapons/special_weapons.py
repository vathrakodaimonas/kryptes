import random
from generators.magic_items.magic_weapons import *




class SpecialWeaponGenerator():

    def __init__(self):
        self.special_weapons_list = [
        'Αυτόματη Τζάγγρα',
        'Βαρδούκι της Σύνθλιψης',
        'Βασιλικό Φαλξ',
        'Γιαταγάνι του Ουν Ουμ',
        'Γοργό Ξίφος',
        'Γυάλινο Ξίφος',
        'Επανερχόμενο Τσεκούρι',
        'Έχιδνα',
        'Κεραύνιο Ακόντιο',
        'Κίτρινο Δόρυ',
        'Κρατερό Όπλο',
        'Μαύρο Τόξο',
        'Νέρτερο Ξίφος',
        'Νοήμον Ξίφος',
        'Ουρά του Διαβόλου',
        'Παγερό Ξίφος',
        'Σεληνιακό Ξίφος',
        'Σκόθειο Τόξο',
        'Σφαγέας',
        'Φλεγόμενο Ξίφος',
        'Φονικό Βέλος',
    ]
        self.special_weapon = ''
        self.magic_weapon_herculean = ''
        self.slayer_sword = ''
        self.killer_arrow = ''

    def determine_special_weapon(self):

        self.special_weapon = ''.join(random.choices(self.special_weapons_list,
                                                weights=[0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.14,
                                                         0.03, 0.03, 0.14, 0.03, 0.05, 0.03, 0.03, 0.14, 0.05, 0.03]))
        if self.special_weapon == 'Κρατερό Όπλο':
            self.special_weapon = HerculeanWeaponGenerator().determine_herculean_weapon()
        elif self.special_weapon == "Νοήμον Ξίφος":
            self.special_weapon = IntelligentSwordGenerator().determine_intelligent_sword()
        elif self.special_weapon == 'Σφαγέας':
            self.special_weapon = SlayerSwordGenerator().determine_slayer_sword()
        elif self.special_weapon == 'Φονικό Βέλος':
            self.special_weapon = KillerArrowGenerator().determine_killer_arrow()
