from Utility.DocReader import DocReader


class Cheats:
    @classmethod
    def make_music_pro(cls, instrument=None):
        #  {"Name": str, "Genre Specialty": str, "Active Instrument": str, "Instrument Stats": {"Guitar": int}},
        #  "Stats": {"Salary": int, "Music Theory": int, "Performance": int, "Stamina": int, "Fame": int}}
        if not instrument:
            instrument = DocReader.get_random_variable("Instrument")
        starting_stats = {"Name": "Herman Li", "Genre Specialty": "Metal", "Active Instrument": instrument,
                          "Instrument Stats": {instrument: 10},
                          "Stats": {"Salary": 100, "Music Theory": 10, "Performance": 10, "Stamina": 10000, "Fame": 10}}
        return starting_stats

