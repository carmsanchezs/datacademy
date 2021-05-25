def main():

    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }

    print(poblacion_paises['Argentina'])  # imprime 44938712
    #print(poblacion_paises['Mexico'])  # KeyError

    for pais in poblacion_paises.keys():
        print(pais)
    
    for valor in poblacion_paises.values():
        print(valor)

    for key, value in poblacion_paises.items():
        print('{} tiene {} habitantes'.format(key, value))


if __name__ == '__main__':
    main()
    