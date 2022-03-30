print("1.piedra")
print("2.papel")
print("3.tijera")
opcion = int(input("¿que elijes persona 1?: "))
opcion2 = int(input("¿que elijes persona 2?: "))

if opcion == 1:
    elijepersona = "piedra"
elif opcion == 2:
    elijepersona ="papel"
elif opcion == 3:
    elijepersona = "tijera"
print("Elije: ", elijepersona)

if opcion2 == 1:
    elijepc = "piedra"
elif opcion2 == 2:
    elijepc ="papel"
elif opcion2 == 3:
    elijepc = "tijera"


if elijepc == "papel" and elijepersona == "piedra":
    print("ganas persona 2, papel envuelve la piedra")
elif elijepc == "papel" and elijepersona == "tijera":
    print("ganaste, tijera corta papel")
elif elijepc == "tijera" and elijepersona == "piedra":
    print("ganaste, piedra pisa tijera")
if elijepc == "papel" and elijepersona == "piedra":
    print("perdiste. papel envuelve piedra")
elif elijepc == "tijera" and elijepersona == "papel":
    print("perdiste, tijera corta papel")
elif elijepc == "piedra" and elijepersona == "tijera":
    print("perdiste, piedra pisa tijera")
elif elijepc == elijepersona :
    print("empate")



