import random
from Utility.DocReader import DocReader


class Album:

    _album_multiplier = DocReader.get_album_types()
    _bass_album_cost = 10000

    @classmethod
    def get_album_types(cls):
        album_types = []
        for album_type in Album._album_multiplier.keys():
            album_types.append(album_type)
        return album_types

    @classmethod
    def get_album_cost(cls, album_type: str):
        return int(Album._bass_album_cost * Album._album_multiplier[album_type])

    def __init__(self, album_name: str, genre: str, album_type: str):
        self.album_name = album_name
        self.genre = genre
        self.album_type = album_type
        self.album_credits = {}
        self.rating = {"Music Theory": 0, "Performance": 0, "Overall": 0}
        self.num_sold = 0
        self.year_released = 0

    def set_album_name(self, name: str):
        self.album_name = name

    def set_album_genre(self, genre: str):
        self.genre = genre

    def set_album_credits(self, album_credits: dict):
        self.album_credits = album_credits

    def stringify_credits(self):
        credits_string = ""
        for member in self.album_credits.keys():
            credit = member + ": " + self.album_credits[member]
            credits_string += credit
            if member != list(self.album_credits.keys())[-1]:
                credits_string += ", \n"
        return credits_string

    def set_rating(self, category: str, value: int):
        self.rating[category] = value

    def increase_num_sold(self, amount: int):
        self.num_sold += amount

    def review_album(self, theory_score: int, performance_score: int):
        self.rating["Music Theory"] = theory_score
        self.rating["Performance"] = performance_score
        reviewer1 = int((theory_score + performance_score) / 2)
        min_score = min(theory_score, performance_score)
        max_score = max(theory_score, performance_score)
        reviewer2 = random.randint(min_score, max_score)
        combined_score = theory_score + performance_score
        reviewer3 = random.randint(1, combined_score)
        scores = [reviewer1, reviewer2, reviewer3]
        avg = int(sum(scores) / len(scores))
        self.rating["Overall"] = avg
        return avg
