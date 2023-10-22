from generators.utils.dice import Dice
from treasuretype import define_treasure_type

class JewelryRoller:
    def __init__(self):
        self.price_range = [300, 500, 700, 1000, 1200, 1500]
        self.jewelry_first_name_zero_two = ["Στέμμα ", "Βραχιόλι ", "Περιδέραιο "]
        self.jewelry_first_name_three = ["Αγαλματίδιο ", "Τελετουργικό όπλο ", "Τελετουργική στολή "]
        self.jewelry_first_name_ten = ["Υφάσματα ", "Ελεφαντόδοντο ", "Πίνακας "]
        self.jewelry_first_name_fifteen = ["Ακριβό χαλί ", "Σεντούκι ", "Πανοπλία "]
        self.jewelry_first_name_fifty = ["Σκαλιστός θρόνος ", "Άγαλμα "]
        self.jewelry_materials = [
            "από ελεφαντόδοντο δουλεμένο με ασήμι",
            "από χρυσοποίκιλτο ελεφαντόδοντο",
            "από χρυσοποίκιλτο ασήμι, με σκαλίσματα από χρυσάφι",
            "από πετραδοστόλιστο ασήμι",
            "από πετραδοστόλιστο χρυσάφι",
            "από πετραδοστόλιστη πλατίνα"
        ]
        self.treasure_type = define_treasure_type()

    def roll_jewel(self):
        prices_array = random.choice(self.price_range)
        jewel_value = ""

        if prices_array == self.price_range[0]:
            jewel_value = f"αξίας {prices_array * random.randint(1, 6)} διναρίων {self.jewelry_materials[0]}"
        elif prices_array == self.price_range[1]:
            jewel_value = f"αξίας {prices_array * random.randint(1, 6)} διναρίων {self.jewelry_materials[1]}"
        elif prices_array == self.price_range[2]:
            jewel_value = f"αξίας {prices_array * random.randint(1, 6)} διναρίων {self.jewelry_materials[2]}"
        elif prices_array == self.price_range[3]:
            jewel_value = f"αξίας {prices_array * random.randint(1, 6)} διναρίων {self.jewelry_materials[3]}"
        elif prices_array == self.price_range[4]:
            jewel_value = f"αξίας {prices_array * random.randint(1, 6)} διναρίων {self.jewelry_materials[4]}"
        elif prices_array == self.price_range[5]:
            jewel_value = f"αξίας {prices_array * random.randint(1, 6)} διναρίων {self.jewelry_materials[5]}"

        jewelry_mass = Dice.twoD6()
        jewelry_kilos = ""

        if 2 <= jewelry_mass <= 7:
            jewelry_kilos = random.choice(self.jewelry_first_name_zero_two) + "βάρους 0.2 λιθάρια"
        elif jewelry_mass in [8, 9]:
            jewelry_kilos = random.choice(self.jewelry_first_name_three) + "βάρους 3 λιθάρια"
        elif jewelry_mass == 10:
            jewelry_kilos = random.choice(self.jewelry_first_name_ten) + "βάρους 10 λιθάρια"
        elif jewelry_mass == 11:
            jewelry_kilos = random.choice(self.jewelry_first_name_fifteen) + "βάρους 15 λιθάρια"
        elif jewelry_mass == 12:
            jewelry_kilos = random.choice(self.jewelry_first_name_fifty) + "βάρους 50 λιθάρια"

        jewel = f"{jewelry_kilos} {jewel_value}"
        return jewel

    def print_jewels(self, num_jewels):
        for _ in range(num_jewels):
            print(self.roll_jewel())

    def roll_and_print(self):
        result = Dice.twoD6()
        print(f"Dice roll is {result}")

        num_jewels = 0
        if self.treasure_type == 0 and result >= 11:
            num_jewels = 1
        elif self.treasure_type == 1 and result >= 11:
            num_jewels = random.randint(1, 3)
        elif self.treasure_type == 2 and result >= 10:
            num_jewels = random.randint(1, 3)
        elif self.treasure_type == 3 and result >= 9:
            num_jewels = random.randint(1, 3)
        elif self.treasure_type == 4 and result >= 9:
            num_jewels = random.randint(1, 5)
        elif self.treasure_type == 5 and result >= 9:
            num_jewels = random.randint(2, 6)
        elif self.treasure_type == 6 and result >= 9:
            num_jewels = random.randint(2, 7)
        elif self.treasure_type == 7 and result >= 8:
            num_jewels = random.randint(2, 7)
        elif self.treasure_type == 8 and result >= 8:
            num_jewels = random.randint(3, 8)
        elif self.treasure_type == 9 and result >= 8:
            num_jewels = random.randint(4, 9)
        elif self.treasure_type == 10 and result >= 8:
            num_jewels = random.randint(3, 18)
        elif self.treasure_type == 11 and result >= 8:
            num_jewels = random.randint(4, 24)
        elif self.treasure_type == 12 and result >= 7:
            num_jewels = random.randint(4, 24)
        elif self.treasure_type == 13 and result >= 7:
            num_jewels = random.randint(5, 30)
        elif self.treasure_type == 14 and result >= 7:
            num_jewels = random.randint(6, 36)
        elif self.treasure_type == 15 and result >= 7:
            num_jewels = random.randint(8, 48)

        print(f"Number of jewels: {num_jewels}")
        self.print_jewels(num_jewels)

