from Utility.DocReader import DocReader
from Game.Member import Member

# instrument = DocReader.get_random_variable("Instrument")
# print("Instrument: " + str(instrument))
# genre = DocReader.get_random_variable("Genre")
# print("Genre: " + str(genre))
# member = DocReader.get_random_variable("Member")
# print("Member Name: " + str(member))
# band = DocReader.get_random_variable("Band")
# print("Band Name: " + str(band))
# location = DocReader.get_random_variable("Location")
# print("Location: " + str(location))

data = {"Name": "John", "Genre Specialty": "Metal", "Active Instrument": "Guitar", "Instrument Stats": {"Guitar": 3},
        "Stats": {"Salary": 1000, "Music Theory": 2, "Performance": 3, "Stamina": 4, "Fame": 5}}
m = Member(data)
print(m)
