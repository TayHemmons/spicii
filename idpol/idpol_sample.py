#!/usr/bin/python3.7

import idpol

biblefile = open('thebible.txt')

bible = biblefile.readlines()

biburr = open('generated/biburr.txt','w')
for line in bible:
    biburr.write((idpol.dumpling(line.lower())))