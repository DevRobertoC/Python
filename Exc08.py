# EXPRESIONES REGULARES
# Cuando necesitamos identificar un caracter especial dentro de la cadena
# se usa el prefijo \
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)
