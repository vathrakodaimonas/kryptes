import random

class KillerArrowGenerator():

    def __init__(self):
        self.killer_arrow_list = ['Αγριάνθρωποι', 'Άνθρωποι', 'Νέρτεροι', 'Γίγαντες', 'Γκόλεμ', 'Δαίμονες',
                         'Δαιμονογενείς', 'Δράκοντες', 'Ερπετά', 'Ευγενείς', 'Θαλάσσια όντα', 'Θηλαστικά',
                         'Θηριόμορφοι', 'Κοβαλογενείς', 'Κυνοκέφαλοι', 'Μάγοι', 'Πτηνά', 'Στοιχειακά όντα']
        self.killer_arrow = ''
    def determine_killer_arrow(self):
        self.killer_arrow = random.choice(self.killer_arrow_list)