def main():
    menu = """
    Elige un numero
    1. Calculo de la suma de 10 números
       si el usuario mete un número negativo, el loop termina
    2. Calculo de la suma de 10 números 
       si el usuario mete un número negativo, este número no se agrega a la suma
    """
    opcion = int(input(menu))

    if opcion == 1:
        programa1()
    elif opcion == 2:
        programa2()
    else:
        print("Choose a correct opcion")


def programa1():
    total = 0
    for num in range(1, 11):
        cantidad = float(input('n{}: '.format(num)))
        if cantidad < 0:
            break
        else:
            total = total + cantidad
    print('total: {}'.format(total))


def programa2():
    total = 0
    for num in range(1, 11):
        cantidad = float(input('n{}: '.format(num)))
        if cantidad < 0:
            continue
        total = total + cantidad
    print('total: {}'.format(total))


if __name__ == '__main__':
    main()
    