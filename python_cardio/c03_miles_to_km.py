MILE = 1.6093

def miles_to_km():
    miles = float(input("Ingresa las millas: "))
    return round(miles * MILE, 2)


def km_to_miles():
    km = float(input("Ingresa los kilometros: "))
    return round(km / MILE, 2)


def main():
    MENU = """
    Elige la opción correcta
    [1] Millas a Kilometros.
    [2] Kilometros a millas.
    """

    opcion = int(input(MENU))

    if opcion == 1:
        km = miles_to_km()
        print("Tienes {} km".format(km))
    elif opcion == 2:
        miles = km_to_miles()
        print("Tienes {} millas".format(miles))


if __name__ == '__main__':
    main()
    