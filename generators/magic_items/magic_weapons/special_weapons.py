import random
from generators.magic_items.magic_weapons import *

magic_weapon_herculean = ''
slayer_sword = ''
killer_arrow = ''


def determine_special_weapon():
    special_weapons_list = [
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
    special_weapon = ''.join(random.choices(special_weapons_list,
                                            weights=[0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.14,
                                                     0.03, 0.03, 0.14, 0.03, 0.05, 0.03, 0.03, 0.14, 0.05, 0.03]))
    if special_weapon == 'Κρατερό Όπλο':
        special_weapon = determine_herculean_weapon()
    elif special_weapon == "Νοήμον Ξίφος":
        special_weapon = determine_intelligent_sword()
    elif special_weapon == 'Σφαγέας':
        special_weapon = determine_slayer_sword()
    elif special_weapon == 'Φονικό Βέλος':
        special_weapon = determine_killer_arrow()

    return special_weapon
