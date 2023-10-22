import random
def determine_magic_weapon():
    magic_weapons_attribute_list = [
        "Καταραμένο",
        "Καταραμένο",
        "Ειδικό",
        'Μαγικό',
        'Μαγικό',
        'Μαγικό',
        'Μαγικό',
        'Μαγικό',
        'Μαγικό',
        'Μαγικό',
        'Μαγικό'

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
    special_weapons_list = [
        'Αυτόματη Τζάγγρα',
        'Βαρδούκι της Σύνθλιψης',
        'Βασιλικό Φαλξ',
        'Γιαταγάνι του Ουν Ουμ', 'Γοργό Ξίφος',
        'Γυάλινο Ξίφος', 'Επανερχόμενο Τσεκούρι', 'Έχιδνα', 'Κεραύνιο Ακόντιο', 'Κίτρινο Δόρυ', 'Κρατερό Όπλο',
        'Κρατερό Όπλο', 'Κρατερό Όπλο', 'Κρατερό Όπλο', 'Κρατερό Όπλο',
        'Μαύρο Τόξο', 'Νέρτερο Ξίφος', 'Νοήμον Ξίφος', 'Νοήμον Ξίφος', 'Νοήμον Ξίφος', 'Νοήμον Ξίφος', 'Νοήμον Ξίφος',
        'Ουρά του Διαβόλου', 'Παγερό Ξίφος', 'Σεληνιακό Ξίφος',
        'Σκόθειο Τόξο', 'Σφαγέας', 'Σφαγέας', 'Σφαγέας', 'Σφαγέας', 'Σφαγέας', 'Φλεγόμενο Ξίφος', 'Φλεγόμενο Ξίφος',
        'Φονικό Βέλος',
    ]

    magic_weapon_herculean = ''
    intelligent_sword = ''
    slayer_sword = ''
    killer_arrow = ''

    magic_weapon_type = random.choice(magic_weapons_attribute_list)
    magic_weapon = ''
    if magic_weapon_type == 'Ειδικό':
        magic_weapon = random.choice(special_weapons_list)
        if magic_weapon == 'Κρατερό Όπλο':
            magic_weapon_herculean = 'Κρατερό: ' + random.choice(magic_weapons_type_list) + ' ' + random.choice(
                magic_weapon_bonus)
        elif magic_weapon == "Νοήμον Ξίφος":
            magic_weapon_spells_counter = 0

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

            def roll_intelligent_sword_spell(number_of_spells: int) -> str:
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

                return [str(random.choice(intelligent_sword_spells)) for _ in range(number_of_spells)]

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

            def roll_intelligent_sword_personality():
                personalities_list = ['Η προσωπικότητά του είναι πονηρή και χειριστική.',
                                      'Η προσωπικότητά του είναι σαδιστική και βάρβαρη.',
                                      'Η προσωπικότητά του είναι ψευδολόγα και διαβολική.',
                                      'Η προσωπικότητά του είναι παράλογη και ψυχωτική.',
                                      'Η προσωπικότητά του είναι απαισιόδοξη και μελαγχολική.',
                                      'Η προσωπικότητά του είναι ευγενική και τίμια.']
                return random.choice(personalities_list)

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
                power = roll_intelligent_sword_power()
                if power != 'Ξόρκι':
                    powers.append(power)
                else:
                    magic_weapon_spells_counter += 1
            elif result in range(41, 54):
                for _ in range(2):
                    power = roll_intelligent_sword_power()
                    if power != 'Ξόρκι':
                        powers.append(power)
                    else:
                        magic_weapon_spells_counter += 1
            elif result in range(54, 64):
                for _ in range(3):
                    power = roll_intelligent_sword_power()
                    if power != 'Ξόρκι':
                        powers.append(power)
                    else:
                        magic_weapon_spells_counter += 1
            else:
                for _ in range(3):
                    power = roll_intelligent_sword_power()
                    if power != 'Ξόρκι':
                        powers.append(power)
                    else:
                        magic_weapon_spells_counter += 1

            if 'Δύο ζαριές στον πίνακα' in spells:
                magic_weapon_spells_counter += 2
                spells.remove('Δύο ζαριές στον πίνακα')

            spells.append(roll_intelligent_sword_spell(magic_weapon_spells_counter))

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

            intelligent_sword = f'Νοήμον Ξίφος {random.choice(intelligent_sword_weapon_bonus)} Δυνάμεις: {powers}. Ξόρκια: {spells}. {extra_language} {ambition} {roll_intelligent_sword_personality()}'
        elif magic_weapon == 'Σφαγέας':
            def determine_slayer_sword():
                slayer_sword_list = ['Χοιροσφάχτης',
                                     'Γιγαντομάχος', 'Δρακοντοκτόνος', 'Θηριογδάρτης', 'Δαιμονοφάγος', 'Οστεοθραύστης',
                                     'Ολεσήνωρ', 'Μαγοκτόνος']
                slayer_sword = random.choice(slayer_sword_list)
                return slayer_sword

            determine_slayer_sword()
        elif magic_weapon == 'Φονικό Βέλος':
            def killer_arrow():
                killer_arrow_list = ['Αγριάνθρωποι', 'Αγριάνθρωποι', 'Άνθρωποι', 'Άνθρωποι', 'Νέρτεροι', 'Νέρτεροι',
                                     'Γίγαντες', 'Γίγαντες', 'Γκόλεμ', 'Γκόλεμ', 'Δαίμονες', 'Δαίμονες',
                                     'Δαιμονογενείς', 'Δαιμονογενείς', 'Δράκοντες', 'Δράκοντες', 'Ερπετά', 'Ερπετά',
                                     'Ευγενείς', 'Ευγενείς', 'Θαλάσσια όντα', 'Θαλάσσια όντα', 'Θηλαστικά', 'Θηλαστικά',
                                     'Θηριόμορφοι', 'Θηριόμορφοι', 'Κοβαλογενείς', 'Κοβαλογενείς', 'Κυνοκέφαλοι',
                                     'Κυνοκέφαλοι', 'Μάγοι', 'Μάγοι', 'Πτηνά', 'Πτηνά', 'Στοιχειακά όντα',
                                     'Στοιχειακά όντα']
                killer_arrow = random.choice(killer_arrow_list)
                return killer_arrow

            killer_arrow()



    elif magic_weapon_type == 'Μαγικό':
        magic_weapon = random.choice(magic_weapons_type_list) + ' ' + random.choice(magic_weapon_bonus)
    elif magic_weapon_type == "Καταραμένο":
        magic_weapon = f"{magic_weapon_type}: {random.choice(magic_weapons_type_list)}"

    if magic_weapon_herculean:
        print(magic_weapon_herculean)
        return magic_weapon_herculean
    elif intelligent_sword:
        print(intelligent_sword)
        return intelligent_sword
    elif slayer_sword:
        print(slayer_sword)
        return slayer_sword
    elif killer_arrow:
        print(killer_arrow)
        return killer_arrow
    else:
        print(magic_weapon)
        return magic_weapon