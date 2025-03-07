import random
from Utility.DocReader import DocReader


class Member:

    @classmethod
    def get_starting_stats(cls, level=1, instrument=None):
        #  {"Name": str, "Genre Specialty": str, "Active Instrument": str, "Instrument Stats": {"Guitar": int}},
        #  "Stats": {"Salary": int, "Music Theory": int, "Performance": int, "Stamina": int, "Fame": int}}
        name = DocReader.get_random_variable("Member")
        if instrument:
            active_instrument = instrument
        else:
            active_instrument = DocReader.get_random_variable("Instrument")
        genre_specialty = DocReader.get_random_variable("Genre")
        stats = Member.roll_stats(active_instrument, level)
        starting_stats = {"Name": name, "Genre Specialty": genre_specialty, "Active Instrument": active_instrument,
                          "Instrument Stats": {active_instrument: stats["Instrument"][active_instrument]},
                          "Stats": {}}
        for stat in stats["Stats"].keys():
            value = stats["Stats"][stat]
            starting_stats["Stats"][stat] = value
        return starting_stats

    @classmethod
    def roll_stats(cls, instrument: str, level=1):
        stats = {"Music Theory": 0, "Performance": 0, "Fame": 0}
        for stat in stats.keys():
            value = random.randint(level, level*3)
            stats[stat] = value
        stats["MaxStamina"] = 50 + (50 * level)
        stats["Stamina"] = stats["MaxStamina"]
        stats["Salary"] = 1000 * level
        instrument_stat = random.randint(level, level*3)
        i_stat = {instrument: instrument_stat}
        member_stats = {"Stats": stats, "Instrument": i_stat}
        return member_stats

    def __init__(self, starting_stats=None):
        self.name = ""
        self.genre_specialty = ""
        self.active_instrument = {"Guitar": False, "Drums": False, "Bass": False, "Vocals": False, "Keyboard": False}
        self.instrument_stats = {"Guitar": 0, "Drums": 0, "Bass": 0, "Vocals": 0, "Keyboard": 0}
        self.stats = {"Salary": 0, "Music Theory": 0, "Performance": 0, "Stamina": 0, "MaxStamina": 0, "Fame": 0}
        if starting_stats:
            self.set_starting_stats(starting_stats)

    def set_starting_stats(self, starting_stats: dict):
        #  {"Name": str, "Genre Specialty": str, "Active Instrument": str, "Instrument Stats": {"Guitar": int}},
        #  "Stats": {"Salary": int, "Music Theory": int, "Performance": int, "Stamina": int, "Fame": int}}
        self.name = starting_stats["Name"]
        self.genre_specialty = starting_stats["Genre Specialty"]
        active_instrument = starting_stats["Active Instrument"]
        self.active_instrument[active_instrument] = True
        int_stats = ["Instrument Stats", "Stats"]
        for i in range(len(int_stats)):
            for j in starting_stats[int_stats[i]].keys():
                if int_stats[i] == "Instrument Stats":
                    value = starting_stats["Instrument Stats"][j]
                    self.instrument_stats[j] = value
                else:
                    value = starting_stats["Stats"][j]
                    self.stats[j] = value

    def __str__(self):
        text = ""
        text += "Name: " + str(self.name) + "\n"
        text += "Genre Specialty: " + str(self.genre_specialty) + "\n"
        for i in self.active_instrument.keys():
            if self.active_instrument[i]:
                text += "Active Instrument: " + str(i) + "\n"
        text += "------------------------\n"
        text += "Instrument Stats\n"
        text += "------------------------" + "\n"
        for j in self.instrument_stats.keys():
            text += str(j) + ": " + str(self.instrument_stats[j]) + "\n"
        text += "------------------------\n"
        text += "Band Member Stats\n"
        text += "------------------------\n"
        for k in self.stats.keys():
            text += str(k) + ": " + str(self.stats[k]) + "\n"
        return text

    def set_name(self, name: str):
        self.name = name

    def set_genre_specialty(self, genre: str):
        self.genre_specialty = genre

    def check_genre_specialty(self, genre: str):
        if self.genre_specialty == genre:
            return True
        return False

    def set_active_instrument(self, instrument_name: str):
        for instrument in self.active_instrument.keys():
            self.active_instrument[instrument] = False
            if instrument == instrument_name:
                self.active_instrument[instrument] = True

    def get_active_instrument(self):
        for instrument in self.active_instrument.keys():
            if self.active_instrument[instrument]:
                return instrument
        return

    def set_instrument_stat(self, instrument_name: str, value: int):
        self.instrument_stats[instrument_name] = value

    def increase_instrument_stat(self, instrument_name: str, increase_amount: int):
        current_value = self.instrument_stats[instrument_name]
        new_value = current_value + increase_amount
        self.set_instrument_stat(instrument_name, new_value)

    def set_stat(self, stat_name: str, value: int):
        self.stats[stat_name] = value

    def increase_stat(self, stat_name: str, increase_amount: int):
        current_value = self.stats[stat_name]
        new_value = current_value + increase_amount
        self.set_stat(stat_name, new_value)

    def decrease_stat(self, stat_name: str, decrease_amount: int):
        current_value = self.stats[stat_name]
        new_value = current_value - decrease_amount
        if new_value < 0:
            new_value = 0
        self.set_stat(stat_name, new_value)

    def check_current_stat_value(self, stat: str):
        if stat in self.stats.keys():
            return self.stats[stat]
        elif stat in self.instrument_stats.keys():
            return self.instrument_stats[stat]
        else:
            print("No stat found: " + stat)
            return
