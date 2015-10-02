# coding: utf-8
from riksdagsledamoter import data

"""
HEMUPPGIFT 1
============
Hur många riksdagsledamöter har ett son-namn?

1) Loopa listan med riksdagsledamöter
2) Kolla om personen har ett "son"-namn
3) Räkna många riksdagsledamöter som har son-namn.

Bonus:
 Räkna hur stor andel av ledamöterna i varje parti som har son-namn.

Den översta raden (from ... import ...) hämtar en lista med riksdagsledamöter
från riksdagsledamoter.py.

"""
counter_sd=0.0
counter_s=0.0
counter_fp=0.0
counter_mp=0.0
counter_m=0.0
counter_c=0.0
counter_v=0.0
counter_kd=0.0

total_sd=0.0
total_s=0.0
total_fp=0.0
total_mp=0.0
total_m=0.0
total_c=0.0
total_v=0.0
total_kd=0.0

counter_son_names = 0.0
total_number_of_mps = len(data)

for row in data:
	if "son," in row["name"] or "son " in row["name"]:
		counter_son_names=(counter_son_names+1)
    #total_party
    
	if "S" in row["party"]:
		if "SD" in row["party"]:
			total_sd=(total_sd+1)
		else:
			total_s=(total_s+1)
	if "FP" in row["party"]:
		total_fp=(total_fp+1)
	if "M" in row["party"]:
		if "MP" in row["party"]:
			total_mp=(total_mp+1)
		else:
			total_m=(total_m+1)
	if "C" in row["party"]:
		total_c=(total_c+1)
	if "V" in row["party"]:
		total_v=(total_v+1)
	if "KD" in row["party"]:
		total_kd=(total_kd+1)
    #counter_party
	if "son," in row["name"] or "son " in row["name"]:
		if "S" in row["party"]:
			if "SD" in row["party"]:
				counter_sd=(counter_sd+1)
			else:
				counter_s=(counter_s+1)
		if "FP" in row["party"]:
			counter_fp=(counter_fp+1)
		if "M" in row["party"]:
			if "MP" in row["party"]:
				counter_mp=(counter_mp+1)
			else:
				counter_m=(counter_m+1)
		if "C" in row["party"]:
			counter_c=(counter_c+1)
		if "V" in row["party"]:
			counter_v=(counter_v+1)
		if "KD" in row["party"]:
			counter_kd=(counter_kd+1)

perc_sd=(int(round(100*(counter_sd/total_sd))))
perc_s=(int(round(100*(counter_s/total_s))))
perc_fp=(int(round(100*(counter_fp/total_fp))))
perc_mp=(int(round(100*(counter_mp/total_mp))))
perc_m=(int(round(100*(counter_m/total_m))))
perc_c=(int(round(100*(counter_c/total_c))))
perc_v=(int(round(100*(counter_v/total_v))))
perc_kd=(int(round(100*(counter_kd/total_kd))))

perc_total_names=(int(round(100*(counter_son_names/total_number_of_mps))))

print("Av %s ledamöter har %s son-namn. Det motsvarar %s procent." 
	%(total_number_of_mps, int(counter_son_names), perc_total_names))
print("\n")
print("I Sverigedemokraterna har %s procent av ledamöterna ett son-namn (%s/%s)." 
	%(perc_sd, int(counter_sd), int(total_sd)))
print("I Socialdemokraterna har %s procent av ledamöterna ett son-namn (%s/%s)." 
	%(perc_s, int(counter_s), int(total_s)))
print("I Folkpartiet har %s procent av ledamöterna ett son-namn (%s/%s)." 
	%(perc_fp, int(counter_fp), int(total_fp)))
print("I Miljöpartiet har %s procent av ledamöterna ett son-namn (%s/%s)." 
	%(perc_mp, int(counter_mp), int(total_mp)))
print("I Moderaterna har %s procent av ledamöterna ett son-namn (%s/%s)." 
	%(perc_m, int(counter_m), int(total_m)))
print("I Centerpartiet har %s procent av ledamöterna ett son-namn (%s/%s)." 
	%(perc_c, int(counter_c), int(total_c)))
print("I Vänsterpartiet har %s procent av ledamöterna ett son-namn (%s/%s)." 
	%(perc_v, int(counter_v), int(total_v)))
print("I Kristdemokraterna har %s procent av ledamöterna ett son-namn (%s/%s)." 
	%(perc_kd, int(counter_kd), int(total_kd)))













