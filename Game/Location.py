from Utility.DocReader import DocReader


class Location:

    _available_locations = {}
    _performance_log = {}
    _hype_tracker = {}

    def __init__(self, name=None):
        if name:
            self.location_name = name
        else:
            self.location_name = ""
        self.performance_score = 0
        self.hype_generated = 0
        self.ticket_cost = 0
        self.tickets_sold = 0
        self.income_generated = 0
        self.venue_cost = 0
        self.year = 0

    def set_performance_score(self, score: int):
        self.performance_score = score

    def set_hype_generated(self, hype: int):
        self.hype_generated = hype

    def set_ticket_cost(self, cost: int):
        self.ticket_cost = cost

    def set_tickets_sold(self, sold: int):
        self.tickets_sold = sold

    def calculate_income_generated(self):
        income = self.ticket_cost * self.tickets_sold
        self.income_generated = income

    def set_venue_cost(self, cost: int):
        self.venue_cost = cost

    @classmethod
    def create_random_location(cls):
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
        Location._hype_tracker[location_name] = Location

    @classmethod
    def get_hype_generated(cls):
        album_hype = 0
        for performance in Location._hype_tracker.keys():
            hype = Location._hype_tracker[performance].hype_generated
            album_hype += hype
        return album_hype

    @classmethod
    def clear_hype(cls, album_name: str):
        Location._performance_log[album_name] = Location._hype_tracker
        Location._hype_tracker = {}

    @classmethod
    def get_performance_log(cls):
        return Location._performance_log
