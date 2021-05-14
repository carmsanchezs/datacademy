def run():
    palabra = input('Escribe una cadena: ')

    palabra = palabra.lower().replace(' ', '') \
                .replace('á','a') \
                .replace('é','e') \
                .replace('í','i') \
                .replace('ó','o') \
                .replace('ú','u') 

    if palabra == palabra[::-1]:
        print('Es palíndromo')
    else:
        print('No es palíndromo')

if __name__ == '__main__':
    run()
    