import re

def palabras_minusculas(texto):
    patron = re.compile(r'\b[a-z]+\b')
    palabras_encontradas = patron.findall(texto)

    return palabras_encontradas

texto_ejemplo = "Hola Bienvenido a la Programacion. Si te gusta la tecnologia has venido al Lugar Indicado"
resultado = palabras_minusculas(texto_ejemplo)
print(resultado)
