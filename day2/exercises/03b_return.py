# -*- coding: utf-8 -*-

"""
 ÖVNING
 Gör en funktion som räknar ut ökningen/minskningen i arbetslöshet,
 mellan två år.
"""

data = [
    {"municipality": "Ale",
     "unemployment_2009": 5.5,
     "unemployment_2014": 4.9
     },
    {"municipality": "Alingsås",
     "unemployment_2009": 5.7,
     "unemployment_2014": 6.0
     },
    {"municipality": "Alvesta",
     "unemployment_2009": 4.7,
     "unemployment_2014": 8.9
     }
]

def get_change(unemployment_now, unemployment_then):
    diff=unemployment_now-unemployment_then
    return diff

for row in data:
    change=get_change(row["unemployment_2014"], row["unemployment_2009"])
    kommun=row["municipality"]
    print("Skillnaden i arbetslöshet i %s är %s" %(kommun, change))


"""

    ale = data[0]
    alvesta = data[2]
    print(ale)
    print(alvesta)
    print(get_change(ale["unemployment_2014"], ale["unemployment_2009"]))
    print(get_change(alvesta["unemployment_2014"], ale["unemployment_2009"]))

"""