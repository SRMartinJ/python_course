# -*- coding: utf-8 -*-

def categorize_unemployment(unemployment):
    if unemployment < 5.0:
        return "låg"

    elif unemployment < 7.5:
        return "medel"

    elif unemployment >=7.5:
        return "hög"

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
     },
    {"municipality": "Aneby",
     "unemployment_2009": 4.9,
     "unemployment_2014": 6.2
     },
    {"municipality": "Arboga",
     "unemployment_2009": 6.5,
     "unemployment_2014": 9.4
     },
    {"municipality": "Arjeplog",
     "unemployment_2009": 6.1,
     "unemployment_2014": 5.6
     },
    {"municipality": "Arvidsjaur",
     "unemployment_2009": 7.8,
     "unemployment_2014": 7.7
     },
    {"municipality": "Arvika",
     "unemployment_2009": 7.0,
     "unemployment_2014": 6.9
     },
    {"municipality": "Askersund",
     "unemployment_2009": 5.7,
     "unemployment_2014": 5.5
     },
    {"municipality": "Avesta",
     "unemployment_2009": 5.8,
     "unemployment_2014": 8.1
     },
    {"municipality": "Bengtsfors",
     "unemployment_2009": 8.0,
     "unemployment_2014": 8.3
     },
    {"municipality": "Berg",
     "unemployment_2009": 6.4,
     "unemployment_2014": 7.3
     },
    {"municipality": "Bjurholm",
     "unemployment_2009": 5.7,
     "unemployment_2014": 9.2
     },
    {"municipality": "Bjuv",
     "unemployment_2009": 7.0,
     "unemployment_2014": 8.2
     },
    {"municipality": "Boden",
     "unemployment_2009": 6.7,
     "unemployment_2014": 7.8
     }
]



for row in data:
    category=categorize_unemployment(row["unemployment_2014"])
    kommun=(row["municipality"])
    print("\n")
    print("%s tillhör kategori %s" % (kommun, category))
