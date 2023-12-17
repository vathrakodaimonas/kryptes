import random


class SlayerSwordGenerator:

    def __init__(self):
        self.slayer_sword_list = ['Χοιροσφάχτης',
                         'Γιγαντομάχος', 'Δρακοντοκτόνος', 'Θηριογδάρτης', 'Δαιμονοφάγος', 'Οστεοθραύστης',
                         'Ολεσήνωρ', 'Μαγοκτόνος']
        self.slayer_sword = ''
    def determine_slayer_sword(self):
        self.slayer_sword = random.choice(self.slayer_sword_list)
        return self.slayer_sword