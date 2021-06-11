# EXPRESIONES REGULARES
# SPAM CONFIDENCE

import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line) # Duvuelve 1 si hay coincidencia o 0 si no la hay   
    if len(stuff) != 1: continue    
    num = float(stuff[0])
    numlist.append(num)
print('Maximun: ', max(numlist))