# Working with Expresione Regulares
# Fine Tuning String Extraction

import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+',x) # \S es un caracter que no es espacio en blanco, el + indica uno o mas caracteres
print(y)

y = re.findall('^From (\S+@\S+)',x) #Los () indican que esa es la parte a extraer 
print(y)

# The Regex Version
# Los [] buscan un caracter que no sea espacio en blanco, ^ -->Todo lo que no sea, en este caso un espacio
# en blanco.
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)',lin)
print(y)

# Refinando un poco esto
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From.*@([^ ]*)',lin)
print(y)
