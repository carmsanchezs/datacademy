menu = """
Bienvenido al conversor de monedas
1. Pesos colombianos
2. Pesos argentinos
3. Pesos mexicanos
"""

def conversor(tipo_pesos, valor_dolar):
    pesos = int(input("Cuántos pesos {} tienes?: ".format(tipo_pesos)))
    dolares = round(pesos / valor_dolar, 2)
    print("Tienes {} dolares".format(dolares))

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("Elige la opción correcta")