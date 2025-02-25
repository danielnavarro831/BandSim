

class Member:
    def __init__(self, starting_stats=None):
        self.name = ""  # Create method to generate a random name
        self.genre_specialty = ""
        self.active_instrument = {"Guitar": False, "Drums": False, "Bass": False, "Vocals": False, "Keyboard": False}
        self.instrument_stats = {"Guitar": 0, "Drums": 0, "Bass": 0, "Vocals": 0, "Keyboard": 0}
        self.stats = {"Salary": 0, "Music Theory": 0, "Performance": 0, "Stamina": 0, "Fame": 0}  # Create method to generate start values
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