# Imprimir la suma de todos los números que se encuentren en el archivo de texto

import re
hand = open('regex_sum_1167749.txt')
numlist = list()
for line in hand:    
    numstr = re.findall('([0-9]+)', line)
    if len(numstr) == 0: continue
    for i in range(len(numstr)):
        numlist.append(int(numstr[i]))    
print('Suma: ',sum(numlist))