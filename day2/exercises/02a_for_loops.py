# -*- coding: utf-8 -*-


unicorns = [
    "Joachim Kerpner",
    "Nina Svanberg",
    "Johan Ronge",
    "Christian Holmén",
    "Fredrik Laurin",
    "Olle Carlsson",
    "Lolo Tode Palm",
    "Martin Jönsson"
]

"""
ÖVNING:
Gör en for-loop som skriver ut en numrerad deltagarlista.
1. Joachim Kerpner
2. Nina Svanberg
o.s.v.
"""

counter = 1
print("Nu börjar programmet! Vi sätter räknaren på 1.")

for unicorn in unicorns:
    # Skriv kod här!
    if unicorn==("Joachim Kerpner"):    
        print(("%s. "+unicorn+" - JK") % counter)
        counter=counter+1

    elif unicorn==("Martin Jönsson"):
        print(("%s. "+unicorn+" - MJ") % counter)
        counter=counter+1

    else:
        print(("%s. "+unicorn) % counter)
        counter=counter+1
