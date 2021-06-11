# Validar entrada de cuenta de correo
import re
w=False
while(w==False):
    print("Ingresar correo electronico")
    correo = input('Digite correo: ')
    y = re.findall('\S+@\S+',correo)
    if y:
        print("Email: ", correo)
        w=True
    else:
        print("Correo invalido")
