def area_of_triangle():
    base = float(input('Base: '))
    height = float(input('Altura: '))
    print('Área: {}'.format((base * height) / 2))

def kind_of_triangle():
    side1 = float(input('Cuánto mide el lado 1: '))
    side2 = float(input('Cuánto mide el lado 2: '))
    side3 = float(input('Cuánto mide el lado 3: '))

    if side1 == side2 == side3:
        print('Triángulo Equilátero')
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print('Triangulo Isósceles')
    else:
        print('Triángulo Escaleno')


def main():
    MENU = """
    Elige una opción
        1. Área del triangulo
        2. Determina el tipo de triángulo
    """

    option = int(input(MENU))

    if option == 1:
        area_of_triangle()
    elif option == 2:
        kind_of_triangle()
    else:
        print('Elige una opción correcta')


if __name__ == '__main__':
    main()
    