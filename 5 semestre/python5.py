c=input("Ingrese cadena de texto: ")
cp= c.split()
cd=list(map(str.upper,cp))
print(cp)
sinduplicado=set(cp)
print(sinduplicado)