import pandas as pd
import csv

db= pd.read_csv('booked_business.csv',skipinitialspace=True)
dr= pd.read_csv('booked_regular.csv',skipinitialspace=True)
dt=pd.concat([db,dr],ignore_index=True) 
sitios=[f"{fila}{asientos}"for fila in range(1,21) for asientos in 'ABCDEF']
asientos_reservados=dt['Asiento'].tolist()
 
print(' ')
print('    A B C    D E F  ')
print('==========================')
for fila in range(1,21):
    print(f'{fila:02d} ', end='') #end=' ' hace que se añada un espacio en blanco al final de la linea
    for asiento in 'ABC':
        if f'{fila}{asiento}' in asientos_reservados:
            print('R', end=' ')
        else:
            print('L', end=' ')
    print('   ', end='')
    for asiento in 'DEF':
        if f'{fila}{asiento}' in asientos_reservados:
            print('R', end=' ')
        else:
            print('L', end=' ')
    print()

print(' ')

#Porcentaje de ocupación
def porcent_ocupacion(dt):
    filas_t=dt.shape[0]
    div=filas_t/120
    pocnt=div*100
    return print('El vuelo esta un',round(pocnt,2),'% ocupado')
porcent_ocupacion(dt)

#Pasajeros de cada clase
def pasajeros_clase(db,dr):
    filas_b=db.shape[0]
    filas_r=dr.shape[0]
    return print(filas_b, 'Pasajeros alojados en business y ',filas_r,' pasajeros alojados en turista')
pasajeros_clase(db,dr)

#Calculo numero pasajeros facturan maleta
def  numero_fact(dt):
    facturacion=dt['Facturacion']
    contador=0
    for i in facturacion: #.strip elimina espacios en blanco
        if str(i).strip().lower().startswith('s'): #.lower hace que las letras esten todas las letras en minuscula
            contador+=1
    return print(contador,'Pasajeros facturan maletas')
numero_fact(dt)

#Función que imprime en pantalla opciones del menu
def print_menu():
    print()
    print('\033[1mMENU:\033[0m')
    print('1.Mostrar información de reservas')
    print('2.Mostrar pasajeros\n')
    print('3.Añadir reserva')
    print('4.Modificar reserva')
    print('5.Eliminar reserva')
    print('6.Salir\n')
#Función que imprime los tipos de posibles orden para ordenar la info de los pasajeros
def print_orden():
    print()
    print('Opciones para ordenar la información:')
    print('1.Alfabeticamente segun el apellido')
    print('2.Por número de asiento')

#Funcion pide selección clase 
def op_clases():
    while True:
        clase=input('Introduzca una clase (BUSINESS/REGULAR):\n')
        if clase in ['BUSINESS', 'REGULAR']: #el input debe ser una de estas dos opciones
            return clase
        else:
            print('Por favor, introduzca una clase válida (BUSINESS/REGULAR)')
#Función de selección de opción del menu
def op_menu(): 
    while True:
        print_menu()
        opcion=input(str('Introduzca una opcion (1,2,3,4,5,6)\n'))
        if opcion in ['1','2','3','4','5','6']:
            return opcion
        else:
            print('Por favor, introduzca una opcion valida(1,2,3,4,5,6)')

#Función que pide opciones de orden
def op_orden():
    while True:
        print_orden()
        orden=input('Elija una opcion de orden para mostrar la informacion de los pasajeros:\n')
        if orden in ['1','2']:
            return orden
        else:
            print('Por favor, introduzca una opcion valida (1 o 2)')
#Función que  muestra informacion de reservas
def info_reservas(db,dr):
    eleccion=op_clases()
    print(f'A continuación se le mostrará la información de la reserva en la clase {eleccion}')
    if eleccion=='BUSINESS':
        print(db)
    elif eleccion=='REGULAR':
        print(dr)
#Función que muestra informacion pasajeros
#acabarla, queda que imprima como se especifica la info, y ordenar los asientos.
def info_pasajeros(db,dr):
    eleccion=op_orden()
    if eleccion=='1':
        clase=op_clases()
        if clase=='BUSINESS':
            ordenado=db.sort_values(by="Apellidos")
        
            print(ordenado)
        elif clase=='REGULAR':
             ordenado=dr.sort_values(by="Apellidos")
             print(ordenado)
    elif eleccion=='2':
        clase=op_clases()
        if clase=='BUSINESS':
             
    

def menu():
    seleccion=selec_menu()
    if seleccion=='1':
        info_reservas(db,dr)


