# Working Expresione Regulares
# Non Greedy Matching

import re
x = 'From: Using the : character'
y = re.findall('^F.+:',x) # De esta forma devuelve la expresión mas larga.
print(y)                 # Tambien se puede usar * en vez de +

y = re.findall('F.+?:',x) # Con el ? devuelve la mas corta
print(y)
