import re

def contiene_fecha_valida(cadena):
    patron = re.compile(r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b')

    coincidencia = patron.search(cadena)
    return coincidencia is not None

print(contiene_fecha_valida("La reunión será el 25/12/2023.")) 
print(contiene_fecha_valida("No hay fechas importantes en esta cadena."))
print(contiene_fecha_valida("La fecha de entrega es el 31/01/2022."))
print(contiene_fecha_valida("Formato incorrecto: 2022-01-31."))
