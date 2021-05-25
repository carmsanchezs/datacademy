def imprimir_mensaje():
    print('Mensaje especial')
    print('Estoy aprendiento a usar funciones!')

imprimir_mensaje()

def conversacion(opcion):
    print('Hola')
    print('Cómo estás?')
    print('Elegiste la opción {}'.format(opcion))
    print('Adiós')


opcion = int(input('Elige una opción (1, 2, 3): '))
if opcion == 1:
    conversacion(opcion)
elif opcion == 2:
    conversacion(opcion)
elif opcion == 3:
    conversacion(opcion)
else:
    print('Elige la opción correcta')