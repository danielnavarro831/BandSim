

class Album:
    def __init__(self):
        self.name = ""
        self.genre = ""
        self.album_credits = {}
        self.track_titles = []
        self.rating = {"Theory": 0, "Performance": 0, "Overall": 0}
        self.release_method = ""
        self.num_sold = 0

    def set_album_name(self, name: str):
        self.name = name

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

