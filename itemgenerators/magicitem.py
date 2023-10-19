from dice import Dice
from treasuretype import define_treasure_type
import random
import regex as re

def determine_magic_item():
    result = 14
    print(f'Dice result is {result}')
    magic_item = ''

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
    print(magic_item)
    return magic_item

magic_item = determine_magic_item()

def determine_magic_potion():
    potion_container_list = [
    'Γυάλινο',
    'Πέτρινο',
    'Δερμάτινο',
    'Πήλινο',
    'Τσίγκινο',
    'Κοκάλινο',
    'Κρυστάλλινο',
    'Μπρούτζινο',
    'Χρυσό',
    'Ασημένιο',
    'Ξύλινο',
    'Κέρας'
]
    potion_colour_list =  [
    'Διαφανές',
    'Λευκό',
    'Μαύρο',
    'Κόκκινο',
    'Γαλάζιο',
    'Πράσινο',
    'Κίτρινο',
    'Μωβ',
    'Καφέ',
    'Ροζ',
    'Γκρίζο',
    'Πορφυρό'
]
    potion_other_list = [
    'Υφή νερού',
    'Παχύρευστο',
    'Αναβράζον',
    'Λαδερό',
    'Μεταλλικό',
    'Ατμός',
    'Γλοιώδες',
    'Σχεδόν αέριο',
    'Ιριδίζον',
    'Φωσφορούχο',
    'Ζεστό',
    'Κρύο'
]
    potion_odour_list = [
    'Καμία',
    'Όξινη',
    'Γλυκιά',
    'Σάπια',
    'Άρωμα',
    'Αλκοόλ',
    'Καπνός',
    'Γρασίδι',
    'Χημική',
    'Μούχλα',
    'Θειάφι',
    'Σκόρδο'
]

    magic_potions_list = [
        'Αντίδοτο',
        'Αντίδοτο',
        'Απόσταγμα Παγωνιάς',
        'Βασιλικό Ύδωρ',
        'Δηλητήριο',
        'Εκρηκτικό Φίλτρο',
        'Ελιξίριο Νεότητας',
        'Ελιξίριο Υγείας',
        'Λάδι Οξύτητας',
        'Λάδι του Χελιού',
        'Υγρό Πυρ',
        'Φίλτρο Αέριας Υπόστασης',
        'Φίλτρο Αλήθειας',
        'Φίλτρο Ανάσας Δράκοντα',
        'Φίλτρο Αορατότητας',
        'Φίλτρο της Αράχνης',
        'Φίλτρο Ατρωσιμότητας',
        'Φίλτρο Ελέγχου',
        'Φίλτρο Ελέγχου',
        'Φίλτρο Ελέγχου',
        'Φίλτρο Ελέγχου',
        'Φίλτρο Ελέγχου',
        'Φίλτρο Ζωτικότητας',
        'Φίλτρο Ηρωισμού',
        'Φίλτρο Ίασης',
        'Φίλτρο Ίασης',
        'Φίλτρο Μεγέθυνσης',
        'Φίλτρο Μεταμόρφωσης',
        'Φίλτρο Οξείας Όρασης',
        'Φίλτρο Όρασης Αοράτων',
        'Φίλτρο Όρασης Αοράτων',
        'Φίλτρο Πτήσης',
        'Φίλτρο Σμίκρυνσης',
        'Φίλτρο Στοιχειακής Αντίστασης',
        'Φίλτρο Στοιχειακής Αντίστασης',
        'Φίλτρο Ταχύτητας',
        'Φίλτρο Τηλεπάθειας',
        'Φίλτρο Υποβρύχιας Αναπνοής',
        'Φίλτρο Υποβρύχιας Αναπνοής'
    ]
    magic_potion = random.choice(magic_potions_list)
    magic_potion_properties = f'{random.choice(potion_container_list)} δοχείο, χρώμα {random.choice(potion_colour_list).lower()}. {random.choice(potion_other_list)}, οσμή/γεύση: {random.choice(potion_odour_list).lower()}'
    print(magic_potion + '. ' + magic_potion_properties)
    return magic_potion

def determine_misc_magic_item():
    misc_magic_items_list = [
    'Αθόρυβες Μπότες',
    'Αθόρυβες Μπότες',
    'Αντικείμενο ελέγχου στοιχειακών',
    'Γάντια Θηριώδους Δύναμης',
    'Δόντια του Δράκοντα',
    'Εύχαντρο της Εξαίσιας Ανάπαυλας',
    'Ζώνη Γιγαντοδύναμης',
    'Καθρέφτης Εγκλωβισμού',
    'Κέρας της Αφθονίας',
    'Κέρας της Καταστροφής',
    'Κράνος Κατανόησης',
    'Κράνος Κατανόησης',
    'Κράνος Προστασίας Μυαλού',
    'Κράνος Τηλεμεταφοράς',
    'Κράνος Τηλεπάθειας',
    'Κρυστάλλινη Σφαίρα',
    'Λαίμαργος Σάκος',
    'Μαγική Λύρα',
    'Μαγικό Αυγό',
    'Μαγικό Διαπασών',
    'Μαγικό Χαλί',
    'Μαγικός Σάκος',
    'Μαγικός Σάκος',
    'Μανδύας Διατοπισμού',
    'Μάσκα του Στοιχειού',
    'Μάτι του Χολσόρνα',
    'Μπότες Αιώρησης',
    'Μπότες Ακαταμάχητου Χορού',
    'Μπότες Άλματος και Διασκελισμού',
    'Μπότες της Ταχύτητας',
    'Μπουκάλι Μαγικού Καπνού',
    'Σκοινί της Περίπλεξης',
    'Τύμπανα του Πανικού',
    'Φακοί Ερυθρόρασης',
    'Φορητή Κρύπτη',
    'Χαμαιλεοντικός Μανδύας'
]
    misc_magic_item = random.choice(misc_magic_items_list)
    print(misc_magic_item)
    return misc_magic_item

def determine_magic_rod():
    magic_rods_list = [
    'Ραβδί Ακύρωσης',
    'Ραβδί Ακύρωσης',
    'Ραβδί Ανίχνευσης Εχθρών',
    'Ραβδί Ανίχνευσης Εχθρών',
    'Ραβδί Ανίχνευσης Μαγείας',
    'Ραβδί Ανίχνευσης Μαγείας',
    'Ραβδί Ανίχνευσης Μετάλλων',
    'Ραβδί Ανίχνευσης Μετάλλων',
    'Ραβδί Ανίχνευσης Παγίδων και Διόδων',
    'Ραβδί Ανίχνευσης Παγίδων και Διόδων',
    'Ραβδί Κεραυνοπληξίας',
    'Ραβδί Κεραυνοπληξίας',
    'Ραβδί Μεταμόρφωσης',
    'Ραβδί Παραίσθησης',
    'Ραβδί Παραίσθησης',
    'Ραβδί Παράλυσης',
    'Ραβδί Παράλυσης',
    'Ραβδί Τρόμου',
    'Ραβδί Τρόμου',
    'Ραβδί Τρόμου',
    'Ραβδί Τρόμου',
    'Ραβδί Τρόμου',
    'Ραβδί Τρόμου',
    'Ραβδί Φωτιάς',
    'Ραβδί Φωτιάς',
    'Ραβδί Ψύχους',
    'Ραβδί Ψύχους',
    'Ράβδος Ακινησίας',
    'Ράβδος Εξουσίας',
    'Ράβδος Ισχύος',
    'Ράβδος Μαρασμού',
    'Ράβδος Μαρασμού',
    'Ράβδος Πλήγματος',
    'Ράβδος Πλήγματος',
    'Ράβδος του Όφεως',
    'Ράβδος του Όφεως',
    'Θαυματουργική Ράβδος',
    'Ιαματική Ράβδος',
    'Ιαματική Ράβδος',
    'Μεταβαλλόμενη Ράβδος'
]
    magic_rod = random.choice(magic_rods_list)
    magic_wand = re.findall(r'^\S{5}', magic_rod)
    if magic_wand[0] == 'Ραβδί':
        number_of_charges = random.randint(3, 18)
    else:
        number_of_charges = random.randint(6, 37)
    print(f'{magic_rod} με {number_of_charges} χρήσεις')
    return magic_rod

def determine_magic_ring():
    magic_rings_list = [
    'Δαχτυλίδι Αδυναμίας',
    'Δαχτυλίδι Αδυναμίας',
    'Δαχτυλίδι Αλλαγής Θέσης',
    'Δαχτυλίδι Αλλαγής Θέσης',
    'Δαχτυλίδι Αναγέννησης',
    'Δαχτυλίδι Αντανάκλασης',
    'Δαχτυλίδι Αντανάκλασης',
    'Δαχτυλίδι Αντανάκλασης',
    'Δαχτυλίδι Αντανάκλασης',
    'Δαχτυλίδι Αντανάκλασης',
    'Δαχτυλίδι Αορατότητας',
    'Δαχτυλίδι Αυταπάτης',
    'Δαχτυλίδι Αυταπάτης',
    'Δαχτυλίδι Ελέγχου Θηρίων',
    'Δαχτυλίδι Ελέγχου Θηρίων',
    'Δαχτυλίδι Ελεύθερης Κίνησης',
    'Δαχτυλίδι Ελεύθερης Κίνησης',
    'Δαχτυλίδι Ισχύος',
    'Δαχτυλίδι Ισχύος',
    'Δαχτυλίδι Καλέσματος Ιφρίτη',
    'Δαχτυλίδι Ξορκιών',
    'Δαχτυλίδι Πουπουλένιας Πτώσης',
    'Δαχτυλίδι Πουπουλένιας Πτώσης',
    'Δαχτυλίδι Προστασίας',
    'Δαχτυλίδι Προστασίας',
    'Δαχτυλίδι Τηλεκίνησης',
    'Δαχτυλίδι Τηλεκίνησης',
    'Δαχτυλίδι των Τριών Ευχών',
    'Δαχτυλίδι Υδατοβάδισης',
    'Δαχτυλίδι Υδατοβάδισης',
    'Δαχτυλίδι Φωτός',
    'Δαχτυλίδι Φωτός',
    'Φυλαχτό Διαπεραστικής Όρασης',
    'Φυλαχτό Διαπεραστικής Όρασης',
    'Φυλαχτό Διαπεραστικής Όρασης',
    'Φυλαχτό Διαπεραστικής Όρασης',
    'Φυλαχτό Διαπεραστικής Όρασης',
    'Φυλαχτό Προστασίας Ζωής',
    'Φυλαχτό Προστασίας Ζωής',
    'Φυλαχτό Στοιχειακής Αντίστασης',
    'Φυλαχτό Στοιχειακής Αντίστασης',
    'Φυλαχτό Στραγγαλισμού'
]
    magic_ring = random.choice(magic_rings_list)
    print(magic_ring)
    return magic_ring

def determine_magic_armour():
    magic_armour_type_light_list = ['Σκουτάρι', 'Σκούτα', 'Δερμάτινη', 'Καββάδιο']
    special_armours_list = [
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
    magic_armour_types_list = [
        'Καταραμένη',
        'Καταραμένη',
        'Ειδική',
        'Μαγική',
        'Μαγική',
        'Μαγική',
        'Μαγική',
        'Μαγική',
        'Μαγική',
        'Μαγική',
        'Μαγική',
    ]
    magic_armour_equipment_list = [
        'Σκουτάρι',
        'Σκούτα',
        'Σκούτα',
        'Σκούτα',
        'Σκούτα',
        'Σκούτα',
        'Σκούτα',
        'Σκούτα',
        'Σκούτα',
        'Σκούτα',
        'Σκούτα',
        'Σκούτα',
        'Θυρεός',
        'Θυρεός',
        'Δερμάτινη',
        'Δερμάτινη',
        'Καββάδιο',
        'Καββάδιο',
        'Καββάδιο',
        'Λωρίκιο',
        'Λωρίκιο',
        'Λωρίκιο',
        'Λωρίκιο',
        'Λωρίκιο',
        'Λωρίκιο',
        'Λωρίκιο',
        'Λωρίκιο',
        'Λωρίκιο',
        'Λωρίκιο',
        'Λωρίκιο',
        'Λωρίκιο',
        'Ζάβα',
        'Ζάβα',
        'Ζάβα',
        'Ζάβα',
        'Ζάβα',
        'Ζάβα',
        'Ζάβα',
        'Ζάβα',
        'Ζάβα',
        'Ζάβα',
        'Ζάβα',
        'Ζάβα',
        'Κλιβάνιο',
        'Κλιβάνιο',
        'Κλιβάνιο',
        'Κλιβάνιο',
    ]

    magic_armour_equipment_type = ''
    magic_armour_bonus = ''

    magic_armour_type = random.choice(magic_armour_types_list)

    if magic_armour_type == 'Ειδική':
        magic_armour_equipment_type = random.choice(special_armours_list)

    elif magic_armour_type == 'Μαγική':
        magic_armour_equipment_type = random.choice(magic_armour_equipment_list)

        if magic_armour_equipment_type in magic_armour_type_light_list:
            magic_armour_bonus = '+1'
        else:
            result = Dice.two_D6()
            if result >= 10:
                magic_armour_bonus = '+1'
            else:
                magic_armour_bonus = '+2'
    else:
        magic_armour_equipment_type = magic_armour_type + ' θωράκιση: ' + random.choice(magic_armour_equipment_list)

    magic_armour = magic_armour_equipment_type + ' ' + magic_armour_bonus

    print(magic_armour)
    return magic_armour

def determine_magic_weapon():
    special_weapons_list = [
        "Νοήμον Ξίφος",
    ]
    magic_weapons_attribute_list = [
        "Ειδικό",
    ]
    magic_weapons_type_list = [
    "Ακόντιο",
    "Σφύρα",
    "Απελατίκι",
    "Απελατίκι",
    "Απελατίκι",
    "Ράβδος",
    "Σαλίβα",
    "Ρομφαία",
    "Λογχοπέλεκυς",
    "Ξίφος",
    "Ξίφος",
    "Ξίφος",
    "Βέλη",
    "Βέλη",
    "Βέλη",
    "Σφαιρίδια",
    "Σπάθη",
    "Σπάθη",
    "Σφενδόνη",
    "Δορυδρέπανο",
    "Τζάγγρα",
    "Εγχειρίδιο",
    "Εγχειρίδιο",
    "Τόξο",
    "Τόξο",
    "Δόρυ",
    "Δόρυ",
    "Δόρυ",
    "Τόξο, σύνθετο",
    "Μύδροι",
    "Μύδροι",
    "Τσεκούρι",
    "Τσεκούρι",
    "Μάχαιρα",
    "Φαλξ",
    "Πέλεκυς"
    ]
    magic_weapon_bonus = [
        '+1',
        '+1',
        '+1',
        '+1',
        '+1',
        '+1',
        '+1',
        '+2',
        '+2',
        '+3',
        '+3'
    ]
    magic_weapon_herculean = ''
    intelligent_sword = ''


    magic_weapon_type = random.choice(magic_weapons_attribute_list)
    magic_weapon = ''
    if magic_weapon_type == 'Ειδικό':
        magic_weapon = random.choice(special_weapons_list)
        if magic_weapon == 'Κρατερό Όπλο':
            magic_weapon_herculean = 'Κρατερό: ' + random.choice(magic_weapons_type_list) + ' ' + random.choice(magic_weapon_bonus)
            print(magic_weapon_herculean)
        elif magic_weapon == "Νοήμον Ξίφος":
            magic_weapon_powers_counter = ''
            magic_weapon_spells_counter = ''

            def roll_intelligent_sword_power():
                intelligent_sword_powers = [
                    'Εντοπισμός μυστικών διόδων (1μ)',
                    'Εντοπισμός ψευδαισθήσεων (3μ)',
                    'Εντοπισμός δομικών παγίδων (3μ)',
                    'Όραση αοράτων (3μ)',
                    'Εντοπισμός χρυσού και αργύρου (6μ)',
                    'Εντοπισμός πετραδιών (6μ)',
                    'Εντοπισμός μαγείας (3μ)',
                    'Ανίχνευση κακόβουλων δυνάμεων (3μ)',
                    'Ξόρκι'
                ]
                return random.choice(intelligent_sword_powers)

            def roll_intelligent_sword_spell():
                intelligent_sword_spells = [
                    'Γητεία',
                    'Γητεία',
                    'Γητεία',
                    'Διαταγή',
                    'Διαταγή',
                    'Διαταγή',
                    'Πτήση',
                    'Πτήση',
                    'Πτήση',
                    'Κλείσιμο Πληγής',
                    'Κλείσιμο Πληγής',
                    'Τηλεκίνηση',
                    'Τηλεκίνηση',
                    'Τηλεκίνηση',
                    'Τηλεμεταφορά',
                    'Τηλεμεταφορά',
                    'Τηλεμεταφορά',
                    'Αιώρηση',
                    'Αιώρηση',
                    'Αιώρηση',
                    'Αιώρηση',
                    'Δύναμη',
                    'Δύναμη',
                    'Δύναμη',
                    'Φασματική Εκδήλωση',
                    'Φασματική Εκδήλωση',
                    'Φασματική Εκδήλωση',
                    'Ανίχνευση Σκέψεων',
                    'Ανίχνευση Σκέψεων',
                    'Ανίχνευση Σκέψεων',
                    'Τηλεπάθεια',
                    'Τηλεπάθεια',
                    'Τηλεπάθεια',
                    'Διαπεραστική όραση',
                    'Διαπεραστική όραση',
                    'Διαπεραστική όραση',
                    'Δύο ζαριές στον πίνακα'
                ]
                return random.choice(intelligent_sword_spells)

            def roll_intelligent_sword_extra_language():
                intelligent_sword_extra_languages = [
                    'νομαδική.',
                    'χθόνια.',
                    'γλωκτική.',
                    'αρχαϊκή.',
                    'στυγική.',
                    'δαιμονική.'
                ]
                return random.choice(intelligent_sword_extra_languages)

            def roll_intelligent_sword_ambition():
                ambitions_list = [
                    'σφαγή ενός τύπου τεράτων.',
                    'σφαγή μελών ενός κράτους, έθνους ή φυλής.',
                    'σφαγή ακολούθων κάποιας θρησκείας/σέκτας.',
                    'σφαγή φονιάδων, κλεφτών ή άλλων κακοποιών.',
                    'σφαγή βασιλέων ή ευγενών.',
                    'σφαγή των πάντων.'
                ]
                return random.choice(ambitions_list)

            intelligent_sword_weapon_bonus = [
                '+1',
                '+1',
                '+1',
                '+1',
                '+1',
                '+1',
                '+2',
                '+2',
                '+3',
                '+3',
                '+3'
            ]

            powers = []
            spells = []

            result = Dice.d66()
            if result in range(11, 37):
                _power = roll_intelligent_sword_power()
                if _power != 'Ξόρκι':
                    magic_weapon_powers_counter += 1
                else:
                    magic_weapon_spells_counter += 1
            elif result in range(41, 54):
                _power = roll_intelligent_sword_power()
                _power1 = roll_intelligent_sword_power()
                if _power != 'Ξόρκι':
                    magic_weapon_powers_counter += 1
                elif _power1 != 'Ξόρκι':
                    magic_weapon_powers_counter += 1
                elif _power or _power1 == 'Ξόρκι':
                    magic_weapon_spells_counter += 1
            elif result in range(54, 64):
                _power = roll_intelligent_sword_power()
                _power1 = roll_intelligent_sword_power()
                _power2 = roll_intelligent_sword_power()
                if _power != 'Ξόρκι':
                    magic_weapon_powers_counter += 1
                elif _power1 != 'Ξόρκι':
                    magic_weapon_powers_counter += 1
                elif _power or _power1 == 'Ξόρκι':
                    magic_weapon_spells_counter += 1
            else:
                magic_weapon_powers_counter += 3
                if powers[0] == 'Ξόρκι':
                    powers[0] = roll_intelligent_sword_spell()
                elif powers[1] == 'Ξόρκι':
                    powers[1] = roll_intelligent_sword_spell()
                elif powers[2] == 'Ξόρκι':
                    powers[2] = roll_intelligent_sword_spell()
                spells.append(roll_intelligent_sword_spell())

            extra_language_roll = Dice.one_D6()
            if extra_language_roll < 3:
                extra_language = f'Γνωρίζει άλλη μια επιπλέον γλώσσα, την {roll_intelligent_sword_extra_language()}'
            else:
                extra_language = 'Δεν γνωρίζει κάποια άλλη γλώσσα πέραν της κοινής.'

            ambition_roll = Dice.one_D6()
            if ambition_roll < 3:
                ambition = f'Επιδιώκει την {roll_intelligent_sword_ambition()}'
            else:
                ambition = 'Δεν έχει κάποια ειδική επιδίωξη.'

            intelligent_sword = f'Νοήμον Ξίφος {random.choice(intelligent_sword_weapon_bonus)} Δυνάμεις: {", ".join(powers)}. Ξόρκια: {", ".join(spells)}. {extra_language} {ambition}'

    elif magic_weapon_type == 'Μαγικό':
        magic_weapon = random.choice(magic_weapons_type_list) + ' ' + random.choice(magic_weapon_bonus)
    elif magic_weapon_type == "Καταραμένο":
        magic_weapon = f"{magic_weapon_type}: {random.choice(magic_weapons_type_list)}"
    if magic_weapon_herculean:
        print(magic_weapon_herculean)
        return magic_weapon_herculean
    elif intelligent_sword:
         print(intelligent_sword)
         return(intelligent_sword)
    else:
        print(magic_weapon)
        return magic_weapon


if magic_item == 'Διάφορα':
    determine_misc_magic_item()
elif magic_item == 'Μαγικό φίλτρο':
    determine_magic_potion()
elif magic_item == 'Μαγικό ραβδί ή ράβδος':
    determine_magic_rod()
elif magic_item == 'Μαγικό δακτυλίδι ή φυλακτό':
    determine_magic_ring()
elif magic_item == 'Μαγική θωράκιση':
    determine_magic_armour()
elif magic_item == 'Μαγικό όπλο':
    determine_magic_weapon()

# ToDo: Νοήμοντα Ξίφη, Σφαγείς