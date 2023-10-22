from generators.utils.dice import Dice
def determine_magic_item():
    result = Dice.d66()
    print(f'Dice result is {result}')
    magic_item = ''

    if result in range(11, 24):
        magic_item = 'Μαγικό όπλο'
    elif result in range(24, 34):
        magic_item = 'Μαγική θωράκιση'
    elif result in range(34, 46):
        magic_item = 'Μαγικό φίλτρο'
    elif result in range(46, 57):
        magic_item = 'Μαγική περγαμηνή'
    elif result in range(61, 63):
        magic_item = 'Μαγικό δακτυλίδι ή φυλακτό'
    elif result in range(63, 65):
        magic_item = 'Μαγικό ραβδί ή ράβδος'
    elif result in range(65, 67):
        magic_item = 'Διάφορα'
    print(magic_item)
    return magic_item

    if magic_item == 'Διάφορα':
        determine_misc_magic_item()
    elif magic_item == 'Μαγικό φίλτρο':
        determine_magic_potion()
    elif magic_item == 'Μαγικό ραβδί ή ράβδος':
        determine_magic_rod()
    elif magic_item == 'Μαγικό δακτυλίδι ή φυλακτό':
        determine_magic_ring()
    elif magic_item == 'Μαγική θωράκιση':
        determine_magic_armour()
    elif magic_item == 'Μαγικό όπλο':
        determine_magic_weapon()
