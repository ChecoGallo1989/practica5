print("Determinar si una palabra es un palindromo")
palabra = input("introduce una palabra \n")

palabra = palabra.lower() 

palabra_original = palabra

def invertir (palabra):
    return palabra[::-1]

if(palabra_original == invertir(palabra)):
    print(palabra_original + " es un apalindromo")
else:
    print(palabra_original + " no es un apalindromo")    



