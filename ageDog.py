#Lee la edad de alguien
#Resta 2 a esta edad y se llma last_years
# first_years sera igual a los 2 por 10.5
# Multiplicar los años restantes (last_years) por 4
#Sumar los first_years con el resultado anterior
# Imprimir lo siguiente ""

age_human= int (input("Ingresa tu edad: "))
last_years = age_human - 2
first_years = 2 * 10.5
last_years = last_years *4
age_dog = last_years + first_years
print(f"Tienes {age_human} años que equivalen a {age_dog} años perrunos")