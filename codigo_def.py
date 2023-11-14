import pandas as pd
import re #me servira para separar numeros de letras en las funciones relacionadas con los asientos
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
    for i in facturacion: 
        if str(i).strip().startswith('s'): #.strip elimina espacios en blanco
            contador+=1
    return print(contador,'Pasajeros facturan maletas')
numero_fact(dt)

#Función que imprime en pantalla opciones del menu
def print_menu():
    print()
    print('\033[1mMENU:\033[0m')
    print('1.Mostrar información de reservas')
    print('2.Mostrar pasajeros')
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
#Funcion que imprime preferecnias de asiento
def print_preferencias():
    print()
    print('Opciones de asiento:')
    print('1.Ventanilla')
    print('2.Pasillo')
    print('3.Indiferente')
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
#Función que pide informacion al usuario para crear una nueva reserva
#corregir que por ejemplo el dni y las clases me pide introducirla dos veces
def user_info(dt):
    print('Introduzca la información pedida en mayusculas')
    dni=input("Por favor, introduzca su DNI: \n")
    #Compruebo si el dni ya esta asociado a una reserva
    while dni in dt['DNI'].values:
        print('Este DNI ya esta en uso, por favor, introduzca un DNI válido')
       
    dni=input("Por favor, introduzca su DNI: \n")
    nombre=input("Por favor, introduzca su nombre: \n")
    apellidos = input("Por favor, introduzca sus apellidos:\n ")
    edad = input("Por favor, introduzca su edad:\n ")
    facturacion = input("¿Desea facturar maletas? (SI/NO): \n")
    return dni, nombre, apellidos, edad, facturacion

#Funcion que le pregunta al usuario que asiento prefiere
def op_preferencia():
    print_preferencias()
    preferencia = input("Elija una opcion (1,2 o 3):\n")
    return preferencia
 

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
            print('ok')

#Función que busca asientos disponibles
def buscar_sitio(op_preferencia, sitios, asientos_reservados, op_clases):
    eleccion=op_clases()
    preferencia=op_preferencia()
    if eleccion=='BUSINESS':
        sitios=[ asiento for asiento in sitios if int(re.search(r'\d+', asiento).group()) <= 8] #condicion para los asientos de business
    elif eleccion=='REGULAR':
        sitios=[asiento for asiento in sitios if int(re.search(r'\d+', asiento).group()) > 8]#condiciion para los asientos de regular

    if preferencia=='1':
        asiento_pref=[asiento for asiento in sitios if asiento[-1] in 'AF'] #condición de los asientos en ventanilla
    elif preferencia=='2':
        asiento_pref=[asiento for asiento in sitios if asiento[-1] in 'CD']#condición de los asientos en pasillo
    elif preferencia=='3':
        asiento_pref=sitios #no hay condición porque le es indiferente al usuario

    for asiento in asiento_pref:
        if asiento not in asientos_reservados:
            return asiento

    return None
#Función para aisgnar el sitio y añadir la reserva
def add_reserva(asiento,asientos_reservados):
    if asiento is not None:
        eleccion=op_clases()
        asiento=buscar_sitio(op_preferencia, sitios, asientos_reservados, op_clases)
        asientos_reservados.append(asiento)
        print(f'Asiento asigando{asiento}')

        #Extraer el numero de fila del asiento
        numero_asiento=re.findall(r'\d+', asiento)
        if numero_asiento:
            numero_asiento=numero_asiento[0] #re.findall devulve una lista, asi que tomamos el primer elemento
            numero_fila=int(numero_asiento)
        #Dependiendo de la fila, elije el archivo CSV correspondiente
        if 1<=numero_fila<=8:
            csv_file='booked_business.csv'
        elif 9<=numero_fila<=20:
            csv_file='booked_regular.csv'
        
        #Lee el archcivo CSV existente en un DataFrame
        dt=pd.read_csv(csv_file) 
        #Añade los datos introduciods por el usuario a una nueva fila
        dni,nombre,apellidos,edad,facturacion=user_info(dt)
        fila=[dni,nombre,apellidos,asiento,edad,facturacion]
        #Añade la fila al DataFrame
        dt.loc[len(dt)]=fila
        #Guarda el DataFrame actaulizado en el archivo csv correspondiente
        dt.to_csv(csv_file,index=False)
    else:
        print('No hay asientos disponibles con sus preferencias')

#Función para modificar el asiento


def menu():
    seleccion=op_menu()
    if seleccion=='1':
        info_reservas(db,dr)
    elif seleccion=='3':
        add_reserva(asiento,asientos_reservados)
    elif seleccion=='5':
        print('0')

