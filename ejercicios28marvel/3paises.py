print("elija una de las siguientes banderas:")
print("LGBTI, roja, negra y blanca")

paises = input("digite la bandeera que se escogio:")

if paises == "LGBTI":
    banderas = "U0001F3F3"
elif paises == "roja":
    banderas = "U0001F6A9"
elif paises == "negra":
    banderas = "U0001F3F4"
elif paises == "blanca":
    banderas = "U0001F3F3"
else:
    banderas = '🏳'

print(banderas)
print("\U0001F929")