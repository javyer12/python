opcion = int(input('elige una opcion (1,2,3): '))

def conversacion(msj):
        print('hola')
        print(msj)
        print('besitos besitos chao chao')

if opcion == 1:
       conversacion('elegiste la 1')
elif opcion == 2:
       conversacion('elegiste la 2')
elif opcion == 3:
       conversacion('elegiste la 3')
else:
        print('elige una opcion valida')