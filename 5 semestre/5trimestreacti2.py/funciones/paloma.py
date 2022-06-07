from audioop import reverse
def cadenae(cadena):
    for i in lista:
        print(i)
        cadena+=str(i)+coma
    return cadena


def reves(lista):
    lista.sort(reverse=True)
    lista2=lista
    return lista2


def menu(lista):
    menu = int(input("selecione \n 1. Para buscar en la lista \n 2. Para salir\n"))

    while menu> 2:
        print('digite un numero del 1 al 2 SOLAMENTE')
        menu = int(input("selecione \n 1. Para buscar en la lista \n 2. Para salir\n"))

    while menu == 1:
        letra = input("Introdusca lo que va buscar en la lista: ")
        for i in lista:
            if i == letra:
                print('es igual ')
            else:
                print('no es igual')
        menu = int(input("selecione \n 1.buscar \n 2. salir\n"))

    if menu == 2:
        print('Esperamos que vuelvas pronto')

def contar(lista):
    letra = input("Introdusca la palabra que este dentro de la lista para contar sus silabas: ")
    for i in lista:
        if i == letra:
            verdad=len(i)
            print(f'{verdad}')
        else:
            print(f"NULL")


lista=['paloma','sofia','tatiana','fernanda','maria','camila','jacinto','mily','clara','cruz']
cadena=""
coma=","

print("\n El programa mostrara la lista \n")

cadena =cadenae(cadena)
print(f"{cadena}")

print("\n Se imprimira la lista desendentemente segun abecedario\n")

lista0 =reves(lista)
print(f"{lista0}")
print("\n El programa validara si se encuentr en la lista \n")

menu(lista)

print("\n se contara las silabas \n")
contar(lista)

print("fin")


 

