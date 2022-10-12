lista_elements = [
    {
        "id" : 1,
        "name": "Angela",
        "last_name": "Perez"
    },
    {
        "id" : 2,
        "name": "Arturo",
        "last_name": "Sanchez"
    }
]

def add_element():
    id = int(input('Ingresa el Id de la persona: '))
    name = input("Ingresa el nombre de la persona: ")
    last_name = input('Ingresa el apellido de la persona: ')
    person = {
        "id" : id,
        "name" :name,
        "last_name": last_name
    }
    lista_elements.append(person)

def remove_element():
    id = int(input('Ingresa el Id del elemento a eliminar: '))
    found = find_element(id)
    print(found)
    aceptar = input("Estás seguro? (S/N) ")
    if aceptar == "S":
        lista_elements.remove(found)
        print("Elemento Eliminado")

def find_element(id):
    found=()
    for element in lista_elements:
        if element['id'] == id:
            found =element
        return found
        
def show_elements():
    #for para iterar y mostrar
    for element in lista_elements:
        for key, value in element.items():
            print(f"{key}->{value}")

def edit_element():
    id = int(input('Ingresa el Id del elemento a editar: '))
    found = find_element(id)
    print(found)

if __name__ == '__main__':
    menu = '''
    Implementación de CRUD de Elementos: 
    1 - Insertar
    2 - Mostrar todos
    3 - Buscar por Id
    4 - Editar
    5 - Eliminar
    6 - Salir
    '''
    while True:
        opcion = input(menu)
        if opcion == '1':
            print("Insertar Elemento")
            add_element()
            
        elif opcion == '2':
            print("Mostrar todos los elementos")
            show_elements()
            
        elif opcion == '3':
            print("Buscar por ID")
            id = int(input("Ingresa Id a buscar"))
            found=find_element(id)
            print(found)
            
        elif opcion == '4':
            print("Editar Elemento")
            edit_element()
            
        elif opcion == '5':
            print("Eliminar Elemento")
            remove_element()
            
        if opcion =='6':
            print('Bye!')
            break
        
        else:
            print("Opción incorrecta!")
