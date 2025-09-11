from random import choice


def get_name():
    with open("names.txt", "r") as f:
        names = f.read().split(",")
        return choice(names)