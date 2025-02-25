from Game.Member import Member
from Game.Album import Album
import random


class Band:
    _negative_money = False

    @classmethod
    def set_negative_money(cls, state=None):
        if state:
            Band._negative_money = state
        else:
            if Band._negative_money:
                Band._negative_money = False
            else:
                Band._negative_money = True

    @classmethod
    def get_negative_money(cls):
        return Band._negative_money

    def __init__(self):
        self.members = {}  # Dict of "Member Name": Member object
        self.albums = {}  # Dict of "Album Title": Album Object
        self.fame_level = 0
        self.money = 0

    def add_member(self, member: Member):
        member_name = member.name
        self.members[member_name] = member

    def remove_member(self, member_name: str):
        del self.members[member_name]

    def check_if_album_name_exists(self, name: str):
        if name in self.albums.keys():
            return True
        return False

    def add_album(self, album: Album):
        album_name = album.name
        self.albums[album_name] = album

    def set_album_credits(self):
        album_credits = {}
        for member in self.members.keys():
            band_member_obj = self.members[member]
            active_instrument = band_member_obj.get_active_instrument()
            if active_instrument:
                album_credits[member] = active_instrument
            else:
                album_credits[member] = "Special Thanks"
        return album_credits

    def set_fame_level(self):
        self.fame_level = self.calculate_fame_level()

    def calculate_fame_level(self):
        sum_fame = 0
        for member in self.members.keys():
            current_member = self.members[member]
            sum_fame += current_member.stats["Fame"]
        average_fame = int(sum_fame / len(self.members))
        fame = average_fame
        if self.albums:
            album_fame = self.get_album_fame()
            fame += album_fame
        return fame

    def set_money(self, amount: int):
        self.money = amount

    def increase_money(self, increase_amount: int):
        self.money += increase_amount

    def decrease_money(self, decrease_amount: int):
        self.money -= decrease_amount
        if self.money < 0:
            Band.set_negative_money(True)
            self.money = 0

    def get_member_salaries(self):
        salary_total = 0
        for member in self.members.keys():
            current_member = self.members[member]
            salary_total += current_member.stats["Salary"]
        return salary_total

    def pay_member_salaries(self):
        salary_payment = self.get_member_salaries()
        self.decrease_money(salary_payment)
        if Band.get_negative_money():
            self.fire_random_member()
            Band.set_negative_money()

    def get_member_roulette(self):
        roulette = {}
        i = 1
        for member in self.members.keys():
            current_member = self.members[member]
            roulette[i] = current_member.name
            i += 1
        return roulette

    def fire_random_member(self):
        roulette = self.get_member_roulette()
        i = random.randint(1, len(roulette))
        fired_member = roulette[i]
        # Display a notification of some kind
        print("Fired Member: " + str(fired_member))
        del self.members[fired_member]

    def get_album_fame(self):
        album_total_score = 0
        for album in self.albums.keys():
            current_album = self.albums[album]
            review_score = current_album.rating["Overall"]
            album_total_score += review_score
        album_fame_score = int(album_total_score / len(self.albums))
        return album_fame_score
