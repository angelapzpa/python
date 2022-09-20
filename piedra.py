#Script que juega Piedra papel y Tijera con el Usuario

import random 

#Leer elección del Usuario

user = input("Elige: Piedra, Papel o Tijera \n")

#Generar elección de la Maquina 

aleatorio = random.randint(1, 3)
if aleatorio ==1:
    machine = "piedra"
elif aleatorio == 2:
    machine ='papel'
else:
    aleatorio = 'tijera'

#Comparar para determinar quien gana
print(f"El usuario eligió {user} y la máquina eligió {machine}")
if machine=='piedra' and 'papel':
    print("Gana el usuario")
elif machine=='papel'and 'tijera':
    print("Gana e usuario")
elif machine=='tijera' and 'piedra':
    print("Gana el usuario")
    
elif machine=='papel'and 'piedra':
    print("Perdio")
elif machine=='tijera' and 'papel':
    print("Perdio")
elif machine=='tijera'and 'piedra':
    print("Perdio")

else:
    print("Empate")
