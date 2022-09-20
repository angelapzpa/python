#Condicionales if elif else
#Nos permite evaluar expresiones booleanas que de cumplirse realizan
#Una acción y en caso de que no entonces realizan otra

#Evaluar si una persona es mayor de edad
#Nos diga es niño,jove,adulto,bebe,muy mayor

genre = input("Ingresa tu género (H/M): ")
age = int(input('Ingresa tu edad: '))

if genre=='H':
    
    if age < 2:
        print("Eres un bebe!")
    elif age <12:
        print("Eres un niño")
    elif age <18:
        print("Eres un Joven")
    elif age <50:
        print("Eres un adulto")
        
    else:
        print("Eres muy mayor!")

if genre=='M':
    
    if age < 2:
        print("Eres una bebe!")
    elif age <12:
        print("Eres una niña")
    elif age <18:
        print("Eres un señorita")
    elif age <50:
        print("Eres una señora")
        
    else:
        print("Eres muy mayor!")
    
