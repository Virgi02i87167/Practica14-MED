import re

def es_codigo_empleado_valido(cadena):
    patron = re.compile(r'^EMP\d{3}$')

    coincidencia = patron.match(cadena)
    return coincidencia is not None

print(es_codigo_empleado_valido("EMP123"))
print(es_codigo_empleado_valido("EMP456"))
print(es_codigo_empleado_valido("EMP7890"))
print(es_codigo_empleado_valido("ABC123"))