#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Skriv en funktion som tar ett namn och en domän.
Gör namnet mejlkompatibelt och skriv ut en fullständig e-postadress.
"""
import unicodedata as ud

def emailify(name, domain):
	print(name.lower().replace(" ,å,ä,ö", ".,a,a,o")+"@"+domain)

emailify("Annie Lööf", "riksdagen.se")
emailify("David Lång", "riksdagen.se")
emailify("Emma Nohrén", "riksdagen.se")
emailify("阿部慎太郎", "asahi.co.jp")
emailify("Östen Rubin", "dn.se")


name=(u"Martin Jönsson")

print(name.lower().replace(" ", "."))

test=(u"Jönsson")

print(test)

