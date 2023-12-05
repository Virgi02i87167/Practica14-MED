import re

def encontrar_ocurrencias(texto, palabra_a_buscar):
    patron = re.compile(r'\b' + re.escape(palabra_a_buscar) + r'\b', re.IGNORECASE)
    coincidencias = patron.finditer(texto)

    for coincidencia in coincidencias:
        inicio = coincidencia.start()
        fin = coincidencia.end()
        print(f"Encontrada '{palabra_a_buscar}' en posición {inicio}-{fin}: '{texto[inicio:fin]}'")

texto_ejemplo = "Este es un ejemplo de texto. Un texto corto para mostrar cómo funciona la función."
palabra_a_buscar = "texto"

encontrar_ocurrencias(texto_ejemplo, palabra_a_buscar)
