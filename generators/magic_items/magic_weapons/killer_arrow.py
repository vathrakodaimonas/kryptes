import random
def determine_killer_arrow():
    killer_arrow_list = ['Αγριάνθρωποι', 'Άνθρωποι', 'Νέρτεροι', 'Γίγαντες', 'Γκόλεμ', 'Δαίμονες',
                         'Δαιμονογενείς', 'Δράκοντες', 'Ερπετά', 'Ευγενείς', 'Θαλάσσια όντα', 'Θηλαστικά',
                         'Θηριόμορφοι', 'Κοβαλογενείς', 'Κυνοκέφαλοι', 'Μάγοι', 'Πτηνά', 'Στοιχειακά όντα']

    killer_arrow = random.choice(killer_arrow_list)
    return killer_arrow