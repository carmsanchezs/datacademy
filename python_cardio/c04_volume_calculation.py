import math


def cube_volume():
    print("VOLUMEN DEL CUBO")
    side = float(input("Largo del cubo: "))
    volume = side ** 3
    print("El volumen del cubo es: {}".format(volume))


def rectangular_prism_volume():
    print("VOLUMEN DEL PRISMA RECTANGULAR")
    length = float(input("Largo del prisma rectangular: "))
    width = float(input("Ancho del prisma rectangular: "))
    height = float(input("Altura del prisma rectangular: "))
    volume = length * width * height
    print("El volumen del prisma es: {}".format(volume))


def cylinder_volume():
    print("VOLUMEN DEL CILINDRO")
    radius = float(input("Radio del cilindro: "))
    height = float(input("Altura del cilindro: "))
    volume = math.pi * (radius ** 2) * height
    print("El volumen del cilindro es: {}".format(volume))


def cone_volume():
    print("VOLUMEN DEL CONO")
    radius = float(input("Radio del cono: "))
    height = float(input("Altura del cono: "))
    volume = 1 / 3 * math.pi * (radius ** 2) * height
    print("El volumen del cono es: {}".format(volume))


def sphere_volume():
    print("VOLUMEN DE LA ESFERA")
    radius = float(input("Radio de la esfera: "))
    volume = 1 / 3 * math.pi * (radius ** 3)
    print("El volumen de la esfera es: {}".format(volume))


def main():
    MENU = """
    Calculo de volúmenes de figuras geométricas
    [1] Cubo
    [2] Prisma rectangular
    [3] Cilindro
    [4] Cono
    [5] Esfera
    """

    option = int(input(MENU))

    if option == 1:
        cube_volume()
    elif option == 2:
        rectangular_prism_volume()
    elif option == 3:
        cylinder_volume()
    elif option == 4:
        cone_volume()
    elif option == 5:
        sphere_volume()
    else:
        print("Elige una opción correcta")


if __name__ == "__main__":
    main()
