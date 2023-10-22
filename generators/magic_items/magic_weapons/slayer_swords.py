import random

def determine_slayer_sword():
    slayer_sword_list = ['Χοιροσφάχτης',
                         'Γιγαντομάχος', 'Δρακοντοκτόνος', 'Θηριογδάρτης', 'Δαιμονοφάγος', 'Οστεοθραύστης',
                         'Ολεσήνωρ', 'Μαγοκτόνος']
    slayer_sword = random.choice(slayer_sword_list)
    return slayer_sword