import random
from generators.utils.dice import Dice


class IntelligentSwordGenerator():

    def __init__(self):
        self.magic_weapon_spells_counter = 0
        self.intelligent_sword = ''
        self.intelligent_sword_spells = [
            'Γητεία',
            'Διαταγή',
            'Πτήση',
            'Κλείσιμο Πληγής',
            'Τηλεκίνηση',
            'Τηλεμεταφορά',
            'Αιώρηση',
            'Δύναμη',
            'Φασματική Εκδήλωση',
            'Ανίχνευση Σκέψεων',
            'Τηλεπάθεια',
            'Διαπεραστική όραση',
            'Δύο ζαριές στον πίνακα',
        ]
        self.intelligent_sword_powers = [
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
        self.intelligent_sword_extra_languages = [
            'νομαδική.',
            'χθόνια.',
            'γλωκτική.',
            'αρχαϊκή.',
            'στυγική.',
            'δαιμονική.'
        ]
        self.intelligent_sword_weapon_bonus = [
            '+1',
            '+2',
            '+3'
        ]
        self.ambitions_list = [
            'σφαγή ενός τύπου τεράτων.',
            'σφαγή μελών ενός κράτους, έθνους ή φυλής.',
            'σφαγή ακολούθων κάποιας θρησκείας/σέκτας.',
            'σφαγή φονιάδων, κλεφτών ή άλλων κακοποιών.',
            'σφαγή βασιλέων ή ευγενών.',
            'σφαγή των πάντων.'
        ]
        self.personalities_list = ['Η προσωπικότητά του είναι πονηρή και χειριστική.',
                                   'Η προσωπικότητά του είναι σαδιστική και βάρβαρη.',
                                   'Η προσωπικότητά του είναι ψευδολόγα και διαβολική.',
                                   'Η προσωπικότητά του είναι παράλογη και ψυχωτική.',
                                   'Η προσωπικότητά του είναι απαισιόδοξη και μελαγχολική.',
                                   'Η προσωπικότητά του είναι ευγενική και τίμια.']

    def roll_intelligent_sword_spell(self, number_of_spells: int) -> str:
        return ''.join([str(random.choices(self.intelligent_sword_spells,
                                           weights=[0.08, 0.08, 0.08, 0.05, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08,
                                                    0.08, 0.08, 0.02])) for _ in range(number_of_spells)])

    def roll_intelligent_sword_power(self):
        return random.choice(self.intelligent_sword_powers)

    def roll_intelligent_sword_extra_language(self):
        return random.choice(self.intelligent_sword_extra_languages)

    def roll_intelligent_sword_ambition(self):
        return random.choice(self.ambitions_list)

    def roll_intelligent_sword_personality(self):
        return random.choice(self.personalities_list)

    def determine_intelligent_sword(self):

        powers = []
        spells = []

        result = Dice.d66()
        if result in range(11, 37):
            power = self.roll_intelligent_sword_power()
            if power != 'Ξόρκι':
                powers.append(power)
            else:
                self.magic_weapon_spells_counter += 1
        elif result in range(41, 54):
            for _ in range(2):
                power = self.roll_intelligent_sword_power()
                if power != 'Ξόρκι':
                    powers.append(power)
                else:
                    self.magic_weapon_spells_counter += 1
        elif result in range(54, 64):
            for _ in range(3):
                power = self.roll_intelligent_sword_power()
                if power != 'Ξόρκι':
                    powers.append(power)
                else:
                    self.magic_weapon_spells_counter += 1
        else:
            for _ in range(3):
                power = self.roll_intelligent_sword_power()
                if power != 'Ξόρκι':
                    powers.append(power)
                else:
                    self.magic_weapon_spells_counter += 1

        if 'Δύο ζαριές στον πίνακα' in spells:
            self.magic_weapon_spells_counter += 2
            spells.remove('Δύο ζαριές στον πίνακα')

        spells.append(self.roll_intelligent_sword_spell(self.magic_weapon_spells_counter))

        extra_language_roll = Dice.one_D6()
        if extra_language_roll < 3:
            extra_language = f'Γνωρίζει άλλη μια επιπλέον γλώσσα, την {self.roll_intelligent_sword_extra_language()}'
        else:
            extra_language = 'Δεν γνωρίζει κάποια άλλη γλώσσα πέραν της κοινής.'

        ambition_roll = Dice.one_D6()
        if ambition_roll < 3:
            ambition = f'Επιδιώκει την {self.roll_intelligent_sword_ambition()}'
        else:
            ambition = 'Δεν έχει κάποια ειδική επιδίωξη.'

        self.intelligent_sword = 'Νοήμον Ξίφος ' + ''.join(
            random.choices(self.intelligent_sword_weapon_bonus, weights=[0.6, 0.25,
                                                                         0.15])) + f'. Δυνάμεις: {powers}. Ξόρκια: {spells}. {extra_language} {ambition} {self.roll_intelligent_sword_personality()}'
        print(self.intelligent_sword)