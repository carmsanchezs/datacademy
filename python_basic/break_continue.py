def imprime_pares():
    for i in range(1000):
        if i % 2 == 0:
            print(i)
        continue

def imprime_hasta(num):
    for i in range(1000):
        print(i)
        if i == num:
            break


def recorre_hasta_o():
    cadena = input('Escribe una frase: ')
    for letra in cadena:
        if (letra.lower() == 'o'):
            break
        print(letra)


if __name__ == '__main__':
    imprime_pares()
    imprime_hasta(23)
    recorre_hasta_o()
