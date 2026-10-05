# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
favartist={
         "BandName":"Chase Atlantic",
         "BandPlayers":["Mitchel","Clinton","Christian"],
         "Albums":{"Nostalgia":2015,"Paradise":2016,"PHASES":2019,"BEAUTY IN DEATH":2021},
         "Genre":["Dark Alternative Pop","Rock","Alternative R&B"]
}
# (keys are artist names, values are lists of album names)
print(favartist.keys())
print(favartist.values())

# Pretty-print the data structure
pprint(favartist)
# Display details of one album recorded by a specific artist
print(favartist["Albums"]["PHASES"])
count=len(favartist.get("Albums"))
print(count)