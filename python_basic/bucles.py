def fun_while():
    LIMITE = 1000
    contador = 0
    potencia2 = 0
    while potencia2 < LIMITE:
        # potencia2 = 2**contador
        print('2 elevado a la {} es igual a: {}'.format(
            contador, potencia2
        ))
        contador += 1
        potencia2 = 2**contador


if __name__ == '__main__':
    fun_while()
    