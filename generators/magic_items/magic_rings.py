import random


def determine_magic_ring():
    magic_rings_list = [
        'Δαχτυλίδι Αδυναμίας',
        'Δαχτυλίδι Αλλαγής Θέσης',
        'Δαχτυλίδι Αναγέννησης',
        'Δαχτυλίδι Αντανάκλασης',
        'Δαχτυλίδι Αορατότητας',
        'Δαχτυλίδι Αυταπάτης',
        'Δαχτυλίδι Ελέγχου Θηρίων',
        'Δαχτυλίδι Ελεύθερης Κίνησης',
        'Δαχτυλίδι Ισχύος',
        'Δαχτυλίδι Καλέσματος Ιφρίτη',
        'Δαχτυλίδι Ξορκιών',
        'Δαχτυλίδι Πουπουλένιας Πτώσης',
        'Δαχτυλίδι Προστασίας',
        'Δαχτυλίδι Τηλεκίνησης',
        'Δαχτυλίδι των Τριών Ευχών',
        'Δαχτυλίδι Υδατοβάδισης',
        'Δαχτυλίδι Φωτός',
        'Φυλαχτό Διαπεραστικής Όρασης',
        'Φυλαχτό Προστασίας Ζωής',
        'Φυλαχτό Στοιχειακής Αντίστασης',
        'Φυλαχτό Στραγγαλισμού'
    ]
    magic_ring = ' '.join(random.choices(magic_rings_list,
                                         weights=[0.06, 0.06, 0.03, 0.11, 0.03, 0.06, 0.06, 0.06, 0.06, 0.03, 0.03,
                                                  0.06, 0.06, 0.06, 0.03, 0.06, 0.06, 0.08, 0.06, 0.06, 0.03])
                          )
    print(magic_ring)
    return magic_ring


determine_magic_ring()
