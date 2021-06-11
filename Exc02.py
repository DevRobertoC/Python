#Busqueda de lineas que tengan "From:" con expresiones regulares
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)