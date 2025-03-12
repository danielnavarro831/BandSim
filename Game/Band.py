from Game.Member import Member
from Game.Album import Album
from Utility.DocReader import DocReader
import random


class Band:
    _negative_money = False
    _base_class_cost = 1000
    _base_salary = 1000

    @classmethod
    def get_base_class_cost(cls):
        return Band._base_class_cost

    @classmethod
    def get_cost_of_stat_increase(cls, current_stat_value: int):
        base_cost = Band.get_base_class_cost()
        cost = (current_stat_value + 1) * base_cost
        return cost

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

    @classmethod
    def get_new_members(cls, level=1):
        for_hire = {}
        for i in range(0, 3):
            stats = Member.get_starting_stats(level)
            member = Member(stats)
            for_hire[member.name] = member
        return for_hire

    def __init__(self):
        self.band_name = ""
        self.members = {}  # Dict of "Member Name": Member object
        self.albums = {}  # Dict of "Album Title": Album Object
        self.fame_level = 0
        self.money = 20000

    def add_member(self, member: Member):
        member_name = member.name
        self.members[member_name] = member

    def remove_member(self, member_name: str, member_quit=False):
        del self.members[member_name]
        if member_quit:
            print(member_name + " quit the band due to stress!")
        else:
            print(self.band_name + " decided to part ways with " + member_name)

    def check_if_album_name_exists(self, name: str):
        if name in self.albums.keys():
            return True
        return False

    def add_album(self, album: Album):
        album_name = album.album_name
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
        sum_fame = self.get_group_stat("Fame")
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

    def pay_member_salaries(self):
        salary_payment = self.get_group_stat("Salary")
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

    def get_group_stat(self, stat: str):
        group_score = 0
        for member in self.members.keys():
            band_member = self.members[member]
            member_score = band_member.stats[stat]
            instrument_stat = Band.get_instrument_score(band_member)
            if stat == "Performance" and instrument_stat:
                member_score *= instrument_stat
            group_score += member_score
        return group_score

    @classmethod
    def get_instrument_score(cls, member: Member):
        active_instrument = member.get_active_instrument()
        instrument_score = member.instrument_stats[active_instrument]
        return instrument_score

    def make_album(self, album_name: str, genre: str, hype: int, album_type: str):
        album = Album(album_name, genre, album_type)
        album_credits = self.set_album_credits()
        album.set_album_credits(album_credits)
        print(str(album.album_credits))
        fame = self.calculate_fame_level()
        if fame <= 0:
            fame = 1
        if hype <= 0:
            hype = 1
        theory_score = self.get_group_stat("Music Theory")
        performance_score = self.get_group_stat("Performance")
        review_score = album.review_album(theory_score, performance_score)
        num_sold = fame * (hype + review_score)
        album.increase_num_sold(num_sold)
        self.check_if_fame_increased(review_score)
        self.add_album(album)
        print("Num Sold: " + str(num_sold))

    def check_if_fame_increased(self, album_score: int):
        if album_score >= 100:
            for member in self.members.keys():
                band_member = self.members[member]
                band_member.increase_stat("Fame", 1)
                self.members[member] = band_member
                print(str(member) + "'s Fame increased!")

    def decrease_band_stamina(self, tour_length: int):
        quitting_members = []
        for member in self.members.keys():
            band_member = self.members[member]
            exhaustion = random.randint(1, 5)
            exhaustion *= 5
            if tour_length:
                exhaustion *= tour_length
            band_member.stats["Stamina"] -= exhaustion
            if band_member.stats["Stamina"] <= 0:
                quitting_members.append(member)
            elif band_member.stats["Stamina"] <= 25:
                print(member + " is feeling stressed out!")
            self.members[member] = band_member

    def quit_band(self, quitters: list):
        for i in range(len(quitters)):
            self.remove_member(quitters[i])

    def take_class(self, member_name: str, stat: str):
        band_member = self.members[member_name]
        if stat in band_member.stats.keys():
            member_current_stat_value = band_member.stats[stat]
            cost = Band.get_cost_of_stat_increase(member_current_stat_value)
            band_member.increase_stat(stat, 1)
        else:
            member_current_stat_value = band_member.instrument_stats[stat]
            cost = Band.get_cost_of_stat_increase(member_current_stat_value)
            band_member.increase_instrument_stat(stat, 1)
        band_member.increase_stat("Salary", 1000)
        self.members[member_name] = band_member
        print(member_name + " leveled up their " + stat + " to " + str(member_current_stat_value + 1) + "!")
        print(member_name + "'s Salary increased to " + str(band_member.stats["Salary"]))

    def get_discography(self):
        discography = []
        for album in self.albums.keys():
            discography.append(album)
        return discography

    def get_album(self, album_name: str):
        return self.albums[album_name]
