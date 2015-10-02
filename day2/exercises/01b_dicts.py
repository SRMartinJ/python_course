# -*- coding: utf-8 -*-

""" ÖVNING
"""

stockholm = {
    'unemployment_2009': 4.0,
    'unemployment_2014': 5.1
}

solna = {
    'unemployment_2009': 2.7,
    'unemployment_2014': 4.1
}


""" Hur många procentenheter har arbetslösheten stigit i Stockholm?
"""
sthlm_perc=(
	stockholm["unemployment_2014"]-stockholm["unemployment_2009"]
	)
print("Stockholm:\nArbetslösheten i Stockholm har stigit med %s procentenheter sedan 2009\n" % sthlm_perc)


""" Hur många procentenheter har arbetslösheten stigit i Solna?
"""
solna_perc=(
	solna["unemployment_2014"]-solna["unemployment_2009"]
	)
print("Solna:\nArbetslösheten i Solna har stigit med %s procentenheter sedan 2009\n" % solna_perc)

""" Hur mycket högra arbetslöshet hade Stockholm än Solna 2014?
"""
sthlm_jfr_solna=(
	stockholm["unemployment_2014"]-solna["unemployment_2014"]
	)
print("\nStockholms arbetslöshet var %s högre än Solnas" % sthlm_jfr_solna)