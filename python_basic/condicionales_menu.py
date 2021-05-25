menu = """
Bienvenido al conversor de monedas
1. Pesos colombianos
2. Pesos argentinos
3. Pesos mexicanos
"""

opcion = int(input(menu))

if opcion == 1:
    pesos = int(input("Cuántos pesos colombianos tienes?: "))
    valor_dolar = 3875
    dolares = round(pesos / valor_dolar, 2)
    print("Tienes {} dolares".format(dolares))
elif opcion == 2:
    pesos = int(input("Cuántos pesos argentinos tienes?: "))
    valor_dolar = 65
    dolares = round(pesos / valor_dolar, 2)
    print("Tienes {} dolares".format(dolares))
elif opcion == 3:
    pesos = int(input("Cuántos pesos mexicanos tienes?: "))
    valor_dolar = 24
    dolares = round(pesos / valor_dolar, 2)
    print("Tienes {} dolares".format(dolares))
else:
    print("Elige la opción correcta")