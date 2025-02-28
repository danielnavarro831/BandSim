import random


class Album:

    _album_multiplier = {"CD": 1, "CD + DVD": 3, "Vinyl": 5}

    def __init__(self, album_name: str, genre: str):
        self.album_name = album_name
        self.genre = genre
        self.album_credits = {}
        self.track_titles = []
        self.rating = {"Music Theory": 0, "Performance": 0, "Overall": 0}
        self.release_method = ""
        self.num_sold = 0
        self.year_released = 0

    def set_album_name(self, name: str):
        self.album_name = name

    def set_album_genre(self, genre: str):
        self.genre = genre

    def set_album_credits(self, album_credits: dict):
        self.album_credits = album_credits

    def set_track_titles(self):
        #TODO
        return

    def set_rating(self, category: str, value: int):
        self.rating[category] = value

    def set_release_method(self, method: str):
        self.release_method = method

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
