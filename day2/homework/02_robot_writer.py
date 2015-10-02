# coding: utf-8 

"""
HEMUPPGIFT 2
============
Skriv 290 notiser om arbetslösheten!

Jobba vidare på funktionen du skrev i förra hemläxan som skrev en 
nyhetstext om arbetslöshetsutvecklingen i en kommun.
Den här gången ska du skriva notiser om ALLA kommuner genom att loopa
genom en kommunlista.

BONUS:
Utveckla din write_story()-funktion så att den också 
använder categorize_unemployment() som vi skrev under lektionen.
"""

"""
Hämta in en lista med kommundata från filen unemployment.py
"""
from unemployment import data

total_unemployment_2009 = 5.9
total_unemployment_2014 = 8.0

def write_story(municipality, unemployment_2009, unemployment_2014):
	neg_text=("I "+municipality+" gar var %s:e utan jobb" %int(round(100/unemployment_2014)) +"\n"+ 
		"Arbetslosheten i "+municipality+" var forra aret %s procent. " %unemployment_2014+
		"Det ar %s procentenheter hogre an i riket som helhet." %abs(total_unemployment_2014-unemployment_2014)+
		"Pa fem ar har arbetslosheten i "+municipality+" okat med %s procenenheter." %abs(unemployment_2014-unemployment_2009))

	pos_text=(municipality+" klarar sig bra"+"\n"+
		"I "+municipality+" var arbetslosheten %s procent under 2014. " %unemployment_2014+
		"Jamfort med 2009 ar det en minskning med %s procentenheter. " %abs(unemployment_2014-unemployment_2009)+
		"Arets siffra ar %s procentenheter lagre an den totala arbetslosheten forra aret." %abs(total_unemployment_2014-unemployment_2014))

	mkt_pos_text=("Supersiffror for "+municipality+"\n"+
		municipality+"s arbetsloshet var %s procent under 2014. " %unemployment_2014+
		"Det ar hela %s procentenheter lagre an totalsiffran for Sverige. " %(total_unemployment_2014-unemployment_2014)+
		"Arbetslosheten i "+municipality+" har sjunkit med %s procentenheter sedan 2009." %abs(unemployment_2009-unemployment_2014))

	if (total_unemployment_2014-unemployment_2014)>=3.0:
		return(mkt_pos_text)

	elif (total_unemployment_2014-unemployment_2014)<0.0:
		return(neg_text)

	elif (total_unemployment_2014-unemployment_2014)>=0.0:
		return(pos_text)

def categorize_unemployment(unemployment):
    if unemployment < 5.0:
        return "Lag arbetsloshet"

    elif unemployment < 7.5:
    	return "Medelhog arbetsloshet"

    elif unemployment >=7.5:
    	return "Hog arbetsloshet"

for row in data:
	print(categorize_unemployment(row["unemployment_2014"]))
	print(write_story(row["municipality"], row["unemployment_2009"], row["unemployment_2014"]))
	print("\n")
