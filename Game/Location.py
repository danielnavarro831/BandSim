import random

from Utility.DocReader import DocReader


class Location:

    _available_locations = {}
    _performance_log = {}
    _hype_tracker = {}

    def __init__(self, name: str):
        self.location_name = name
        self.performance_score = 0
        self.hype_generated = self.set_hype_generated()
        self.ticket_cost = self.set_ticket_cost()
        self.tickets_sold = 0
        self.income_generated = 0
        self.venue_cost = self.set_venue_cost()
        self.year = 0

    def calculate_income_generated(self):
        income = self.ticket_cost * self.tickets_sold
        return income

    def sell_tickets(self, fame: int):
        num_tickets = 10 * random.randint(1, 10)
        num_tickets *= fame
        num_tickets *= self.hype_generated
        self.tickets_sold = num_tickets
        self.income_generated = self.calculate_income_generated()
        return self.income_generated

    def generate_hype(self, performance_score: int):
        self.hype_generated *= performance_score

    @classmethod
    def get_hype_tracker(cls):
        return Location._hype_tracker

    @classmethod
    def set_hype_generated(cls):
        rand_3 = random.randint(5, 20)
        hype_generated = rand_3 * Location.get_num_current_hype_performances()
        return hype_generated

    @classmethod
    def set_ticket_cost(cls):
        rand_2 = random.randint(1, 10)
        ticket_cost = 10 * rand_2
        return ticket_cost

    @classmethod
    def set_venue_cost(cls):
        rand = random.randint(2, 10)
        venue_cost = 1000 * rand
        return venue_cost

    @classmethod
    def create_random_location(cls):
        location_name = DocReader.get_random_variable("Location")
        while Location.check_for_duplicate_location(location_name):
            location_name = DocReader.get_random_variable("Location")
        location = Location(location_name)
        Location.set_location(location)

    @classmethod
    def remove_available_location(cls, location_name: str):
        del Location._available_locations[location_name]

    @classmethod
    def get_available_locations(cls):
        return Location._available_locations

    @classmethod
    def get_specific_location(cls, location_name: str):
        location = Location._available_locations[location_name]
        return location

    @classmethod
    def set_location(cls, location: 'Location'):
        location_name = location.location_name
        Location._available_locations[location_name] = location

    @classmethod
    def log_performance_hype(cls, location: 'Location'):
        location_name = location.location_name
        if location_name in Location._hype_tracker.keys():
            i = 2
            while location_name in Location._hype_tracker.keys():
                location_name += " " + str(i)
                i += 1
        Location._hype_tracker[location_name] = location
        Location.update_available_locations(location_name)

    @classmethod
    def update_available_locations(cls, location_name: str):
        del Location._available_locations[location_name]
        Location.create_random_location()

    @classmethod
    def get_album_hype_generated(cls):
        album_hype = 0
        for performance in Location._hype_tracker.keys():
            past_performance = Location._hype_tracker[performance]
            hype = past_performance.hype_generated
            album_hype += hype
        return album_hype

    @classmethod
    def clear_hype(cls, album_name: str):
        Location._performance_log[album_name] = Location._hype_tracker
        Location._hype_tracker = {}

    @classmethod
    def get_performance_log(cls):
        return Location._performance_log

    @classmethod
    def check_for_duplicate_location(cls, name_check: str):
        for location in Location._available_locations.keys():
            if location == name_check:
                return True
        return False

    @classmethod
    def create_available_locations(cls):
        for i in range(1, 4):
            Location.create_random_location()

    @classmethod
    def get_num_current_hype_performances(cls):
        num_performances = len(Location._hype_tracker)
        if num_performances <= 0:
            num_performances = 1
        return num_performances
