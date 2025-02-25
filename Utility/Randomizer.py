import random


class Randomizer:

    @classmethod
    def get_random_person_name(cls):
        first_names = ["John", "Joe", "Mike", "Steve", "Sean", "Daniel", "Jonny", "Roy"]
        last_names = ["Fierce", "Skewer", "Fisto"]
        i = random.randint(0, len(first_names))
        name = first_names[i]
        j = random.randint(0, len(last_names))
        name += " "
        name += last_names[j]
        return name

    @classmethod
    def get_random_genre(cls):
        genres = []