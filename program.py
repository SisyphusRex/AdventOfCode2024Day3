"""program module"""

import re
import sys


def main(*args):
    """main method"""
    do_part_one()
    do_part_2()


def do_part_2():
    """solve part 2"""
    lines = read_data("data.txt")
    final_mul_list = []
    pair_collection = []

    for string in lines:
        count = 0
        list_of_do_split_strings = re.split("do\(\)", string)

        for substring in list_of_do_split_strings:
            list_of_dont_split_strings = re.split("don't\(\)", substring, 1)

            for index2, stringt in enumerate(list_of_dont_split_strings):
                if index2 == 0:

                    list_of_muls = re.findall("mul\([0-9]+,[0-9]+\)", stringt)
                    final_mul_list.extend(list_of_muls)

        count += 1

    for mul in final_mul_list:
        first_index = mul.index("(") + 1
        second_index = mul.index(")")
        new_str = mul[first_index:second_index]
        pair = new_str.split(",")
        inted_pair = []
        for element in pair:
            inted_pair.append(int(element))
        pair_collection.append(inted_pair)

    product_collection = []
    for pair in pair_collection:
        product = pair[0] * pair[1]
        product_collection.append(product)

    total = 0

    for product in product_collection:
        total += product

    print(f"part 2: {total}")


def do_part_one():
    """solve part one"""
    lines = read_data("data.txt")
    final_mul_list = []
    pair_collection = []

    for string in lines:
        list_of_muls = re.findall("mul\([0-9]+,[0-9]+\)", string)
        final_mul_list.extend(list_of_muls)

    for mul in final_mul_list:
        first_index = mul.index("(") + 1
        second_index = mul.index(")")
        new_str = mul[first_index:second_index]
        pair = new_str.split(",")
        inted_pair = []
        for element in pair:
            inted_pair.append(int(element))
        pair_collection.append(inted_pair)

    product_collection = []
    for pair in pair_collection:
        product = pair[0] * pair[1]
        product_collection.append(product)

    total = 0

    for product in product_collection:
        total += product

    print(f"part 1: {total}")


def read_data(filename) -> list[str]:
    """read data from txt file"""
    lines = []
    with open(filename, "r") as f:
        for line in f:
            lines.append(line)
    final_lines = [""]
    for line in lines:
        final_lines[0] += line

    return final_lines
