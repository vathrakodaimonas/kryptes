import random
from generators.utils import Dice


class SpellGenerator:
    def __init__(self):
        self.first_level_spells = [
            "Αλλαγή Όψης",
            "Ανίχνευση Κακόβουλων Δυνάμεων",
            "Ανίχνευση Μαγείας",
            "Αποκρυπτογράφηση",
            "Αποτροπαϊκή Επωδός",
            "Ασφαλής Πτώση",
            "Αφανής Αρωγός",
            "Γητεία",
            "Διαταγή",
            "Εγγαστριμυθία",
            "Εξορκισμός",
            "Κλείσιμο Πληγής",
            "Κράτημα Πύλης",
            "Μαγική Προστασία",
            "Μαγικός Μύδρος",
            "Σκαρφάλωμα Αράχνης",
            "Ύπνωση",
            "Φως"
        ]
        self.second_level_spells = [
            "Αιώρηση",
            "Ανίχνευση Σκέψεων",
            "Αορατότητα",
            "Εντοπισμός Αντικειμένου",
            "Ηρωισμός",
            "Ήχος",
            "Θηριολαλία",
            "Ιστός",
            "Κάλεσμα Οικείου",
            "Μαγικό Άνοιγμα",
            "Μαγικό Κλείδωμα",
            "Όραση Αοράτων",
            "Πολλαπλά Είδωλα",
            "Ρώμη",
            "Σιωπή",
            "Σκοτάδι",
            "Τύφλωση",
            "Φασματική Εκδήλωση"
        ]
        self.third_level_spells = [
            "Ακινητοποίηση",
            "Ακύρωση Μαγείας",
            "Αποτροπαϊκός Κύκλος",
            "Βραδύτητα",
            "Γλωσσολαλία",
            "Επικοινωνία με Πνεύμα Νεκρού",
            "Ερυθρόραση",
            "Ίαση Νόσων",
            "Κεραυνοπληξία",
            "Προστασία από Βλήματα",
            "Πτήση",
            "Πύρινη Σφαίρα",
            "Σπάσιμο Κατάρας",
            "Σφαίρα Αορατότητας",
            "Ταχύτητα",
            "Τηλαισθησία",
            "Υποβολή",
            "Υποβρύχια Αναπνοή"
        ]
        self.fourth_level_spells = [
            "Αόρατο Μάτι",
            "Γητεία Θηρίου",
            "Διαστατική Πύλη",
            "Εξουδετέρωση Δηλητηρίων",
            "Επούλωση Τραυμάτων",
            "Θέριεμα Φυτών",
            "Μαγεμένο Όπλο",
            "Μαζική Απόκρυψη",
            "Μεταμόρφωση Άλλου",
            "Μεταμόρφωση Εαυτού",
            "Μίασμα",
            "Παγοθύελλα",
            "Παραισθησιακό Τοπίο",
            "Πύρινο Τείχος",
            "Σύγχυση",
            "Τείχος Πάγου",
            "Τρόμος",
            "Ψευδής Τοίχος"
        ]
        self.fifth_level_spells = [
            "Ακινητοποίηση Θηρίου",
            "Αναγέννηση",
            "Αποκατάσταση",
            "Ατσάλινο Τείχος",
            "Επικοινωνία με Ανώτερα Πεδία",
            "Κάλεσμα Στοιχειακού Όντος",
            "Κρετινισμός",
            "Κώνος Ψύχους",
            "Μετουσίωση Πέτρας σε Λάσπη",
            "Νεκρανάσταση",
            "Ξύπνημα Νέρτερων",
            "Όνειρο",
            "Πέρασμα από Τοίχο",
            "Πέτρινο Τείχος",
            "Τηλεκίνηση",
            "Τηλεμεταφορά",
            "Τοξικό Νέφος",
            "Ψυχοδοχείο"
        ]
        self.sixth_level_spells = [
            "Αληθινή Όραση",
            "Αόρατος Διώκτης",
            "Απώθηση",
            "Δαιμονική Φρουρά",
            "Δέσμευση",
            "Έλεγχος Καιρού",
            "Εμφύσηση Ζωής",
            "Εξαΰλωση",
            "Κακοδαίμονας",
            "Κατοπτρική Προβολή",
            "Μετακίνηση Εδάφους",
            "Μετεμψύχωση",
            "Μετουσίωση Πέτρας σε Σάρκα",
            "Ξιφοθύελλα",
            "Ξόρκι Θανάτου",
            "Σεισμός",
            "Φραγμός Μαγείας",
            "Φυλάκιση"
        ]
        self.treasure_map_distance = [
            "Πολύ κοντά",
            "Σχετικά κοντά",
            "Σχετικά μακριά",
            "Μακριά",
            "Πολύ μακριά",
            "Στου διαόλου τη μάνα"
        ]
        self.treasure_map_location = [
            "Μέσα σε έναν υπόγειο τύμβο",
            "Κρυμμένος μέσα σε ερειπωμένο πύργο",
            "Σε μια μυστική κρύπτη, στο άδειο θησαυροφυλάκιο ενός ερειπωμένου κάστρου",
            "Βυθισμένος στο κέντρο μιας λίμνης",
            "Σε ναυάγιο βυθισμένο στη θάλασσα",
            "Θαμμένος σε έρημο νησί",
            "Κρυμμένος σε απρόσιτη κορφή βουνού",
            "Μέσα σε κάποιο απόμακρο σπήλαιο",
            "Κρυμμένος σε παραλιακό σύμπλεγμα σπηλαίων που εμφανίζεται με την άμπωτη",
            "Αόρατος και αιωρούμενος χίλια μέτρα πάνω από το έδαφος",
            "Κρυμμένος σε μυστικό θάλαμο, χτισμένο χίλια μέτρα κάτω από τη γη",
            "Κρυμμένος μέσα σε κάποιο άγαλμα ή μνημείο",
            "Σε μαγική διάσταση της οποίας η πύλη εμφανίζεται υπό συγκεκριμένες συνθήκες",
            "Στον κρατήρα ενός ηφαιστείου",
            "Κάτω από έναν πελώριο βράχο",
            "Μέσα σε έναν πελώριο βράχο",
            "Κρυμμένος στην κουφάλα ενός αρχαίου δέντρου",
            "Στην έπαυλη ενός ανύποπτου ευγενή",
            "Μέσα σε ένα πηγάδι",
            "Μέσα σε μια φυλακή",
            "Σε έναν χαμένο ναό σε δάσος ή ζούγκλα",
            "Σε ένα μαγικό νησί που ταξιδεύει",
            "Σε ένα στοιχειωμένο πλοίο",
            "Στην ερειπωμένη έπαυλη ενός μάγου",
            "Βυθισμένος σε έλος",
            "Θαμμένος σε ένα απόμακρο και αχαρακτήριστο ερημικό μέρος",
            "Σε μυστικό δωμάτιο ενός αρχαίου λαβυρίνθου",
            "Στις κατακόμβες μιας ερειπωμένης πόλης",
            "Στη σκοτεινή πλευρά του φεγγαριού",
            "Παγωμένος μέσα σε κάποιο παγόβουνο ή παγετώνα",
            "Σε μυστική κρύπτη μέσα σε λαβύρινθο",
            "Κρυμμένος σε ένα αρχαίο μαυσωλείο",
            "Στο σώμα κάποιου υπεραιωνόβιου πλάσματος",
            "Σε καταποντισμένο ερείπιο",
            "Στη φωλιά ενός δράκοντα",
            "Μετουσιωμένος με μαγεία σε χάρτη θησαυρού"
        ]
        self.treasure_map_guarded_by = [
            "Αφύλακτος",
            "Αρχαία κατάρα",
            "Παραισθησιακή μαγεία",
            "Σκελετοί ή Τυμβολίκτορες",
            "Στοιχειά ή Φάσματα",
            "Νεκροφάγοι ή Νοσοφόροι",
            "Δράκοντες",
            "Γκόλεμ ή Ζωντανά αγάλματα",
            "Στοιχειακά όντα",
            "Αόρατοι Διώκτες",
            "Παγίδα εγκλωβισμού",
            "Παγίδα εξόντωσης",
            "1.000 φίδια ή σκορπιοί",
            "Παράδοξο θηρίο (βλ. κεφάλαιο τεράτων)",
            "Κακοδαίμονες",
            "Αλίβαντες",
            "Νάγκα",
            "Συνδυασμός δύο αποτελεσμάτων"
        ]

    def generate_scroll(self):
        scroll_result = Dice.d66()
        scroll_number = 0
        cursed = False
        exorcism = False
        protection = False
        protection_from_magic = False
        treasure_map = False
        spell_list = []

        if scroll_result in range(11, 17):
            scroll_number = 1
        elif scroll_result in range(21, 25):
            scroll_number = 2
        elif scroll_result in range(25, 32):
            scroll_number = 3
        elif scroll_result in range(32, 35):
            scroll_number = 5
        elif scroll_result in range(35, 37):
            scroll_number = 7
        elif scroll_result in range(41, 43):
            cursed = True
        elif scroll_result in range(43, 45):
            exorcism = True
        elif scroll_result in range(45, 52):
            protection = True
        elif scroll_result in range(52, 54):
            protection_from_magic = True
        else:
            treasure_map = True

        if scroll_number:
            for _ in range(scroll_number + 1):
                scroll_level = random.randint(1, 6)
                if scroll_level == 1:
                    spell = random.choice(self.first_level_spells)
                    spell_list.append(spell)
                elif scroll_level == 2:
                    spell = random.choice(self.second_level_spells)
                    spell_list.append(spell)
                elif scroll_level == 3:
                    spell = random.choice(self.third_level_spells)
                    spell_list.append(spell)
                elif scroll_level == 4:
                    spell = random.choice(self.fourth_level_spells)
                    spell_list.append(spell)
                elif scroll_level == 5:
                    spell = random.choice(self.fifth_level_spells)
                    spell_list.append(spell)
                elif scroll_level == 6:
                    spell = random.choice(self.sixth_level_spells)
                    spell_list.append(spell)
        elif cursed:
            spell_list.append('Καταραμένη')
        elif exorcism:
            spell_list.append('Περγαμηνή εξορκισμού')
        elif protection:
            spell_list.append('Περγαμηνή προστασίας')
        elif protection_from_magic:
            spell_list.append('Περγαμηνή προστασίας από μαγεία')
        elif treasure_map:
            distance = random.choice(self.treasure_map_distance)
            location = random.choice(self.treasure_map_location).lower()
            guarded_by = random.choice(self.treasure_map_guarded_by).lower()
            if guarded_by == "Συνδυασμός δύο αποτελεσμάτων":
                guarded_by_second = random.choice(self.treasure_map_guarded_by).lower()
                spell_list.append(
                    f'Χάρτης θησαυρού. {distance}, {location}. Φυλάσσεται από {guarded_by} και {guarded_by_second}.')
            else:
                spell_list.append(
                    f'Χάρτης θησαυρού. {distance}, {location}. Φυλάσσεται από {guarded_by}.')

        return f'Περγαμηνή: {", ".join(spell_list)}'

    def generate_grimoire(self):
        magic_user_level = int(input('Select magic user level (1-12) '))
        grimoire_spells = []
        if magic_user_level == 1:
            grimoire_spells.append(random.choice(self.first_level_spells))
        elif magic_user_level == 2:
            for _ in range(2):
                grimoire_spells.append(random.choice(self.first_level_spells))
        elif magic_user_level == 3:
            for _ in range(2):
                grimoire_spells.append(random.choice(self.first_level_spells))
            grimoire_spells.append(random.choice(self.second_level_spells))
        elif magic_user_level == 4:
            for _ in range(3):
                grimoire_spells.append(random.choice(self.first_level_spells))
            for _ in range(2):
                grimoire_spells.append(random.choice(self.second_level_spells))
        elif magic_user_level == 5:
            for _ in range(4):
                grimoire_spells.append(random.choice(self.first_level_spells))
            for _ in range(2):
                grimoire_spells.append(random.choice(self.second_level_spells))
            grimoire_spells.append(random.choice(self.third_level_spells))
        elif magic_user_level == 6:
            for _ in range(4):
                grimoire_spells.append(random.choice(self.first_level_spells))
            for _ in range(2):
                grimoire_spells.append(random.choice(self.second_level_spells))
            grimoire_spells.append(random.choice(self.third_level_spells))
        elif magic_user_level == 7:
            for _ in range(4):
                grimoire_spells.append(random.choice(self.first_level_spells))
            for _ in range(3):
                grimoire_spells.append(random.choice(self.second_level_spells))
            for _ in range(2):
                grimoire_spells.append(random.choice(self.third_level_spells))
            grimoire_spells.append(random.choice(self.fourth_level_spells))
        elif magic_user_level == 8:
            for _ in range(4):
                grimoire_spells.append(random.choice(self.first_level_spells))
            for _ in range(3):
                grimoire_spells.append(random.choice(self.second_level_spells))
            for _ in range(3):
                grimoire_spells.append(random.choice(self.third_level_spells))
            for _ in range(2):
                grimoire_spells.append(random.choice(self.fourth_level_spells))
        elif magic_user_level == 9:
            for _ in range(4):
                grimoire_spells.append(random.choice(self.first_level_spells))
            for _ in range(3):
                grimoire_spells.append(random.choice(self.second_level_spells))
            for _ in range(3):
                grimoire_spells.append(random.choice(self.third_level_spells))
            for _ in range(2):
                grimoire_spells.append(random.choice(self.fourth_level_spells))
            grimoire_spells.append(random.choice(self.fifth_level_spells))
        elif magic_user_level == 10:
            for _ in range(4):
                grimoire_spells.append(random.choice(self.first_level_spells))
            for _ in range(4):
                grimoire_spells.append(random.choice(self.second_level_spells))
            for _ in range(3):
                grimoire_spells.append(random.choice(self.third_level_spells))
            for _ in range(3):
                grimoire_spells.append(random.choice(self.fourth_level_spells))
            for _ in range(2):
                grimoire_spells.append(random.choice(self.fifth_level_spells))
        elif magic_user_level == 11:
            for _ in range(4):
                grimoire_spells.append(random.choice(self.first_level_spells))
            for _ in range(4):
                grimoire_spells.append(random.choice(self.second_level_spells))
            for _ in range(4):
                grimoire_spells.append(random.choice(self.third_level_spells))
            for _ in range(3):
                grimoire_spells.append(random.choice(self.fourth_level_spells))
            for _ in range(3):
                grimoire_spells.append(random.choice(self.fifth_level_spells))
        elif magic_user_level == 12:
            for _ in range(4):
                grimoire_spells.append(random.choice(self.first_level_spells))
            for _ in range(4):
                grimoire_spells.append(random.choice(self.second_level_spells))
            for _ in range(4):
                grimoire_spells.append(random.choice(self.third_level_spells))
            for _ in range(4):
                grimoire_spells.append(random.choice(self.fourth_level_spells))
            for _ in range(4):
                grimoire_spells.append(random.choice(self.fifth_level_spells))
            grimoire_spells.append(random.choice(self.sixth_level_spells))

        return f'Γριμόριο: {", ".join(grimoire_spells)}'
