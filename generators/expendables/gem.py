import random

from generators.utils.dice import Dice
from treasuretype import define_treasure_type


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

    def print_gems(self, num_gems):
        for _ in range(num_gems):
            print(self.roll_gem())

    def generate_gems(self):
        if self.treasure_type is None:
            self.treasure_type = define_treasure_type()

        result = Dice.two_D6()
        print(f"Dice roll is {result}")

        if self.treasure_type in range(0, 2):
            if result >= 11:
                self.print_gems(1)
            else:
                print("No gems")
        elif self.treasure_type == 2:
            if result >= 10:
                self.print_gems(1)
            else:
                print("No gems")
        elif self.treasure_type in range(3, 8):
            if result >= 9:
                self.print_gems(2)
            else:
                print("No gems")
        elif self.treasure_type == 8:
            if result >= 8:
                self.print_gems(3)
            else:
                print("No gems")
        elif self.treasure_type == 9:
            if result >= 8:
                self.print_gems(4)
            else:
                print("No gems")
        elif self.treasure_type == 10:
            if result >= 8:
                self.print_gems(5)
            else:
                print("No gems")
        elif self.treasure_type == 11:
            if result >= 8:
                self.print_gems(6)
            else:
                print("No gems")
        elif self.treasure_type in range(12, 16):
            if result >= 7:
                self.print_gems(8)
            else:
                print("No gems")


a = GemGenerator().roll_gem()
b=1