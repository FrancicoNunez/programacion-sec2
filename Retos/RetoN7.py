Frase = str(input("\n Ingrese su frase: "))

def contar_palabras(frase):
    palabras = frase.split()
    diccionario = {}

    for palabra in palabras:
        diccionario[palabra] = len(palabra)

    return diccionario
    
resultado = contar_palabras(Frase)
print(resultado)