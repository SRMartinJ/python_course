# -*- coding: utf-8 -*-
from riksdagsledamoter import data
"""
HEMUPPGIFT:
1) Öppna och loopa filen riksdagsledamoter.csv
2) Kolla om personen har ett "son"-namn
3) Räkna hur stor andel av alla riksdagsledamöter som har son-namn.

Bonus: Räkna hur många personer i varje parti som har son-namn. 

Tips: Funktionen .split() kan vara användbar för att lista ut vilket parti
en ledamot tillhör.
.split() delar upp en textsträng vid att givet skiljetecken till en lista.
"""

total_mps=len(data)

total_sons=0.0

counter_mp=0.0
counter_m=0.0
counter_s=0.0
counter_sd=0.0
counter_fp=0.0
counter_v=0.0
counter_c=0.0
counter_kd=0.0

sons_mp=0.0
sons_m=0.0
sons_s=0.0
sons_sd=0.0
sons_fp=0.0
sons_v=0.0
sons_c=0.0
sons_kd=0.0

for rad in data:
	if "son," in rad["name"] or "son " in rad["name"]:
		total_sons=(total_sons+1)
	
	partier=(rad["party"])
	delade_partinamn=(partier.split())

	for parti in delade_partinamn:
		if parti==("MP"):
			counter_mp=(counter_mp+1)
			if "son, " in rad["name"] or "son " in rad["name"]:
				sons_mp=(sons_mp+1)
		elif parti==("M"):
			counter_m=(counter_m+1)
			if "son, " in rad["name"] or "son " in rad["name"]:
				sons_m=(sons_m+1)
		elif parti==("S"):
			counter_s=(counter_s+1)
			if "son, " in rad["name"] or "son " in rad["name"]:
				sons_s=(sons_s+1)
		elif parti==("SD"):
			counter_sd=(counter_sd+1)
			if "son, " in rad["name"] or "son " in rad["name"]:
				sons_sd=(sons_sd+1)
		elif parti==("FP"):
			counter_fp=(counter_fp+1)
			if "son, " in rad["name"] or "son " in rad["name"]:
				sons_fp=(sons_fp+1)
		elif parti==("V"):
			counter_v=(counter_v+1)
			if "son, " in rad["name"] or "son " in rad["name"]:
				sons_v=(sons_v+1)
		elif parti==("C"):
			counter_c=(counter_c+1)
			if "son, " in rad["name"] or "son " in rad["name"]:
				sons_c=(sons_c+1)
		elif parti==("KD"):
			counter_kd=(counter_kd+1)
			if "son, " in rad["name"] or "son " in rad["name"]:
				sons_kd=(sons_kd+1)


perc_sons_of_total=(int(round(100*(total_sons/total_mps))))

perc_sons_mp=(int(round(100*(sons_mp/counter_mp))))
perc_sons_m=(int(round(100*(sons_m/counter_m))))
perc_sons_s=(int(round(100*(sons_s/counter_s))))
perc_sons_sd=(int(round(100*(sons_sd/counter_sd))))
perc_sons_fp=(int(round(100*(sons_fp/counter_fp))))
perc_sons_v=(int(round(100*(sons_v/counter_v))))
perc_sons_c=(int(round(100*(sons_c/counter_c))))
perc_sons_kd=(int(round(100*(sons_kd/counter_kd))))

print(
	"Av totalt %s ledamoter i riksdagen har %s ett son-namn. Det motsvarar %s procent.\n \n"
	"I Miljopartiet har %s procent ett son-namn (%s/%s). \n"
	"I Moderaterna har %s procent ett son-namn (%s/%s). \n"
	"I Socialdemokraterna har %s procent ett son-namn (%s/%s). \n"
	"I Sverigedemokraterna har %s procent ett son-namn (%s/%s). \n"
	"I Folkpartiet har %s procent ett son-namn (%s/%s). \n"
	"I Vansterpartiet har %s procent ett son-namn (%s/%s). \n"
	"I Centerpartiet har %s procent ett son-namn (%s/%s). \n"
	"I Kristdemokraterna har %s procent ett son-namn (%s/%s). \n"
	% (
		#total
		total_mps, 
		total_sons,
		perc_sons_of_total, 
		#MP
		perc_sons_mp, 
		sons_mp, 
		counter_mp, 
		#M
		perc_sons_m, 
		sons_m, 
		counter_m, 
		#S
		perc_sons_s, 
		sons_s, 
		counter_s,
		#SD
		perc_sons_sd, 
		sons_sd, 
		counter_sd,  
		#FP
		perc_sons_fp, 
		sons_fp, 
		counter_fp,
		#V
		perc_sons_v, 
		sons_v, 
		counter_v,
		#C
		perc_sons_c, 
		sons_c, 
		counter_c, 
		#KD
		perc_sons_kd, 
		sons_kd, 
		counter_kd,   
		)
	)


