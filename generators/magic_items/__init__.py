from .magic_armour import determine_magic_armour
from .magic_items_misc import determine_misc_magic_item
from .magic_potions import determine_magic_potion
from .magic_rings import determine_magic_ring
from .magic_rod import determine_magic_rod
from .magic_weapons.magic_weapons_main import determine_magic_weapon

__all__ = ['determine_misc_magic_item', 'determine_magic_weapon', 'determine_magic_potion',
           'determine_magic_ring', 'determine_magic_rod', 'determine_magic_armour']
