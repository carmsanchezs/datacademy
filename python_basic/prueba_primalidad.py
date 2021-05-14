def es_primo(numero):
    if numero == 1:
        return False
    elif numero > 1:
        for i in range(2, numero):
            if numero % i == 0:
                return False
    return True


def main():
    numero = int(input('Escribe un número: '))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    main()
    