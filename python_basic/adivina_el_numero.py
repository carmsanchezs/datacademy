import random

def main():
    vidas = 7
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un número entre 1 y 100: '))
    while numero_elegido != numero_aleatorio:
        vidas -= 1
        if numero_elegido > numero_aleatorio:
            print('El número es más pequeño')
        else:
            print('El número es más grande')
        if vidas == 0:
            print('GAME OVER')
            return
        else:
            print('Tienes {} vidas'.format(vidas))
            numero_elegido = int(input('Elige un número entre 1 y 100: '))

    print('Ganaste!')


if __name__ == '__main__':
    main()
    