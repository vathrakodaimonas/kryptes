import random
import regex as re


def determine_magic_rod():
    magic_rods_list = [
        'Ραβδί Ακύρωσης',
        'Ραβδί Ανίχνευσης Εχθρών',
        'Ραβδί Ανίχνευσης Μαγείας',
        'Ραβδί Ανίχνευσης Μετάλλων',
        'Ραβδί Ανίχνευσης Παγίδων και Διόδων',
        'Ραβδί Κεραυνοπληξίας',
        'Ραβδί Μεταμόρφωσης',
        'Ραβδί Παραίσθησης',
        'Ραβδί Παράλυσης',
        'Ραβδί Τρόμου',
        'Ραβδί Φωτιάς',
        'Ραβδί Ψύχους',
        'Ράβδος Ακινησίας',
        'Ράβδος Εξουσίας',
        'Ράβδος Ισχύος',
        'Ράβδος Μαρασμού',
        'Ράβδος Πλήγματος',
        'Ράβδος του Όφεως',
        'Θαυματουργική Ράβδος',
        'Ιαματική Ράβδος',
        'Μεταβαλλόμενη Ράβδος'
    ]
    magic_rod = ' '.join(random.choices(magic_rods_list,
                                        weights=[0.05, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05, 0.1, 0.1, 0.2, 0.1, 0.1, 0.05,
                                                 0.05, 0.05, 0.1, 0.1, 0.1, 0.05, 0.1, 0.05]
                                        ))
    magic_wand = re.findall(r'^\S{5}', magic_rod)
    if magic_wand[0] == 'Ραβδί':
        number_of_charges = random.randint(3, 18)
    else:
        number_of_charges = random.randint(6, 37)
    print(f'{magic_rod} με {number_of_charges} χρήσεις')
    return magic_rod


determine_magic_rod()
