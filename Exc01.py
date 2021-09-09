# Curse Using Python to access Web Data
#Busqueda de lineas en archivo que tengan "From:"
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)


#Este codigo tambien se puede hacer con startswith
print("")
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
