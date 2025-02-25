from Utility.DocReader import DocReader
from Game.Member import Member




data = Member.get_starting_stats(3, "Guitar")
m = Member(data)
print(m)

data = Member.get_starting_stats(3, "Vocals")
a = Member(data)
print(a)

data = Member.get_starting_stats(3, "Drums")
b = Member(data)
print(b)

band_name = DocReader.get_random_variable("Band")
print(band_name)