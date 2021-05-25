# transforma de pesos a dolares
pesos = input("¿Cuántos pesos mexicanos tienes?: ")
pesos = float(pesos)
valor_dolar = 19.90
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
print("Tienes {} dólares".format(dolares))

# transforma de dolares a pesos
dolares = int(input("Cuántos dolares tienes?: "))
valor_peso = 0.05
pesos = round(dolares / valor_peso, 2)
print("Tienes {} pesos".format(pesos))