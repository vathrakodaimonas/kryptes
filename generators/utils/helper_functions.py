import argparse
import os


def ask_for_treasure_type():
    treasure_type_file = 'treasure_type.txt'

    if os.path.exists(treasure_type_file):
        with open(treasure_type_file, 'r') as file:
            treasure_type = int(file.read())
    else:
        parser = argparse.ArgumentParser(description='Treasure type')
        parser.add_argument('treasure_type', nargs='?', help='Define treasure type', type=int, choices=list(range(16)))

        args = parser.parse_args()
        try:
            treasure_type = int(input('Enter treasure type (0-15): '))
            if 0 <= treasure_type <= 15:
                pass
            else:
                raise ValueError('Invalid input. Please enter a value between 0 and 15.')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

    with open(treasure_type_file, 'w') as file:
        file.write(str(treasure_type))

    return treasure_type

def remove_treasure_type_file():
    treasure_type_file = 'treasure_type.txt'
    if os.path.exists(treasure_type_file):
        os.remove(treasure_type_file)