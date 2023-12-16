import random
import regex as re


class MagicRodGenerator():
    def __init__(self):
        self.magic_rods_list = [
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
        self.magic_rod = ''

    def determine_magic_rod(self):

        self.magic_rod = ' '.join(random.choices(self.magic_rods_list,
                                                 weights=[0.05, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05, 0.1, 0.1, 0.2, 0.1, 0.1,
                                                          0.05,
                                                          0.05, 0.05, 0.1, 0.1, 0.1, 0.05, 0.1, 0.05]
                                                 ))
        magic_wand = re.findall(r'^\S{5}', self.magic_rod)
        if magic_wand[0] == 'Ραβδί':
            number_of_charges = random.randint(3, 18)
        else:
            number_of_charges = random.randint(6, 37)
        return f'{self.magic_rod} με {number_of_charges} χρήσεις'
