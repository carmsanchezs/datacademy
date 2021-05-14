import random
import string

def generar_contrasena():

    CARACTERES = string.ascii_letters + string.digits + string.punctuation

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(CARACTERES)
        contrasena.append(caracter_random)
    
    contrasena = ''.join(contrasena)
    return contrasena


def main():
    contrasena = generar_contrasena()
    print('Tu nueva contrasena es: {}'.format(contrasena))


if __name__ == '__main__':
    main()