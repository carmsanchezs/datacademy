def main():
    in_range = False
    print("RANGOS CAMBIANTES")
    lower_limit = int(input("Límite inferior: "))
    upper_limit = int(input("Límite superior: "))
    comparison_number = int(input("Número de comparación: "))

    while not in_range:
        if comparison_number >= lower_limit and comparison_number <= upper_limit:
            print(
                "El número {} está dentro del rago [{} , {}]".format(
                    comparison_number, lower_limit, upper_limit
                )
            )
            in_range = True
            break
        comparison_number = int(input("Elige un nuevo número de comparación: "))


if __name__ == "__main__":
    main()
