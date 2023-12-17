import random

from generators.utils.dice import Dice


class GemGenerator:
    def __init__(self):
        self.price_range = [10, 50, 100, 500, 1000, 5000]  # gem price range
        self.types = [
            ["Αζουρίτης", "Αχάτης", "Μαλαχίτης", "Αιματίτης"],  # 10
            ["Όνυχας", "Ίασπις", "Σεληνόλιθος", "Χαλαζίας"],  # 50
            ["Αλεξανδρίτης", "Αμέθυστος", "Κεχριμπάρι"],  # 100
            ["Μαργαριτάρι", "Τοπάζι"],  # 500
            ["Διαμάντι", "Ρουμπίνι", "Ζαφείρι", "Σμαράγδι"],  # 1000
            ["Μεγάλο διαμάντι", "Μεγάλο ρουμπίνι", "Μεγάλο σμαράγδι"]  # 5000
        ]
        self.treasure_type = None

    def roll_gem(self):
        result = Dice.two_D6()
        gem = ""

        if result in range(2, 4):
            gem = f"{str(self.price_range[0])} {random.choice(self.types[0])}"
        elif result in range(4, 6):
            gem = f"{str(self.price_range[1])} {random.choice(self.types[1])}"
        elif result in range(6, 9):
            gem = f"{str(self.price_range[2])} {random.choice(self.types[2])}"
        elif result in range(9, 11):
            gem = f"{str(self.price_range[3])} {random.choice(self.types[3])}"
        elif result == 11:
            gem = f"{str(self.price_range[4])} {random.choice(self.types[4])}"
        elif result == 12:
            gem = f"{str(self.price_range[5])} {random.choice(self.types[5])}"

        return gem

    def generate_gems(self, treasure_type: int):
        result = Dice.two_D6()
        gem_list = []

        if treasure_type in range(0, 2):
            if result >= 11:
                for _ in range(Dice.one_D6()):
                    gem = self.roll_gem()
                    gem_list.append(gem)
            else:
                pass
        elif treasure_type == 2:
            if result >= 10:
                for _ in range(Dice.one_D6()):
                    gem = self.roll_gem()
                    gem_list.append(gem)
            else:
                pass
        elif treasure_type in range(3, 8):
            if result >= 9:
                for _ in range(2 * Dice.one_D6()):
                    gem = self.roll_gem()
                    gem_list.append(gem)
            else:
                pass
        elif treasure_type == 8:
            if result >= 8:
                for _ in range(3 * Dice.one_D6()):
                    gem = self.roll_gem()
                    gem_list.append(gem)
            else:
                pass
        elif treasure_type == 9:
            if result >= 8:
                for _ in range(4 * Dice.one_D6()):
                    gem = self.roll_gem()
                    gem_list.append(gem)
            else:
                pass
        elif treasure_type == 10:
            if result >= 8:
                for _ in range(5 * Dice.one_D6()):
                    gem = self.roll_gem()
                    gem_list.append(gem)
            else:
                pass
        elif treasure_type == 11:
            if result >= 8:
                for _ in range(6 * Dice.one_D6()):
                    gem = self.roll_gem()
                    gem_list.append(gem)
            else:
                pass
        elif treasure_type in range(12, 16):
            if result >= 7:
                for _ in range(7 * Dice.one_D6()):
                    gem = self.roll_gem()
                    gem_list.append(gem)
            else:
                pass
        return gem_list
