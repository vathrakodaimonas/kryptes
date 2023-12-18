import random


class MagicPotionGenerator:
    def __init__(self):
        self.potion_container_list = [
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
            'Κεράτινο'
        ]
        self.potion_colour_list = [
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
        self.potion_other_list = [
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
        self.potion_odour_list = [
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
        self.magic_potions_list = [
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
            'Φίλτρο Ζωτικότητας',
            'Φίλτρο Ηρωισμού',
            'Φίλτρο Ίασης',
            'Φίλτρο Μεγέθυνσης',
            'Φίλτρο Μεταμόρφωσης',
            'Φίλτρο Οξείας Όρασης',
            'Φίλτρο Όρασης Αοράτων',
            'Φίλτρο Πτήσης',
            'Φίλτρο Σμίκρυνσης',
            'Φίλτρο Στοιχειακής Αντίστασης',
            'Φίλτρο Ταχύτητας',
            'Φίλτρο Τηλεπάθειας',
            'Φίλτρο Υποβρύχιας Αναπνοής'
        ]
        self.magic_potion = ''
        self.potion_of_control = [
            f'Ανθρώπων (συνολικά επίπεδα {random.randint(3, 18)}',
            f'Νέρτερων (συνολικά επίπεδα {random.randint(2, 12)}',
            f'Γιγάντων ({random.randint(1, 3)} γίγαντες',
            f'Δαιμόνων (συνολικά επίπεδα {random.randint(2, 12)})',
            f'Δρακόντων ({random.randint(1, 3)} δράκοντες',
            f'Φυτών και μυκήτων (περιοχή 3x3 μέτρων ή {random.randint(1, 6)}'
        ]

    def determine_magic_potion(self):
        self.magic_potion = ' '.join(
            random.choices(self.magic_potions_list, weights=[0.05, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                                                             0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.05, 0.03, 0.03, 0.05,
                                                             0.03,
                                                             0.03,
                                                             0.03, 0.05, 0.03, 0.03, 0.05, 0.03, 0.03, 0.05]

                           ))
        container = random.choice(self.potion_container_list)
        colour = random.choice(self.potion_colour_list).lower()
        other_property = random.choice(self.potion_other_list)
        odour = random.choice(self.potion_odour_list).lower()
        magic_potion_properties = f'{container} δοχείο, χρώματος {colour}. {other_property}, οσμή/γεύση: {odour}'

        if self.magic_potion == 'Φίλτρο Ελέγχου':
            control = random.choice(self.potion_of_control)
            self.magic_potion = self.magic_potion + f' {control}. ' + magic_potion_properties
        else:
            self.magic_potion = self.magic_potion + '. ' + magic_potion_properties
        return self.magic_potion
