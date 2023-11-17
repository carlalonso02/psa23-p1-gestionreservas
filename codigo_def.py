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
        if str(i).strip().startswith('S'): #.strip elimina espacios en blanco 
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

#Funcion que imprime preferencias de asiento
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

#Funcion que le pregunta al usuario que asiento prefiere
def op_preferencia():
    print_preferencias()
    preferencia = input("Elija una opcion (1,2 o 3):\n")
    return preferencia

#Funcion para ordenar segun numero asientos
def orden_num(asiento):
    '''con esta funcion busco separar el numero de la letra de la letra de los asientos y asi ordenarlos segun el numero'''
    numero=re.findall(r'\d+',asiento)
    return int(numero[0])

#Función que  muestra informacion de reservas
def info_reservas(db,dr):
    '''muestra informacion de reservas de cada clase'''
    eleccion=op_clases()
    print(f'A continuación se le mostrará la información de la reserva en la clase {eleccion}')
    if eleccion=='BUSINESS':
        print(db)
    elif eleccion=='REGULAR':
        print(dr)
    
#Función que muestra informacion pasajeros
#por mejorar: intentar aparte de ordenar segun el numero que ademas en orden de letras, 1A,1B,1C etc.
def info_pasajeros(db,dr):
    '''muestra la informacion de los pasajeros de determinada clase en un orden especifico'''
    eleccion=op_orden()
    if eleccion=='1':
        clase=op_clases()
        if clase=='BUSINESS':
            ordenado=db.sort_values(by="Apellidos")
            columnas=['Asiento','Apellidos','Nombre'] #para imprimir la informacion especificada
            print(ordenado[columnas])
        elif clase=='REGULAR':
             ordenado=dr.sort_values(by="Apellidos")
             columnas=['Asiento','Apellidos','Nombre']
             print(ordenado[columnas])
    elif eleccion=='2':
        clase=op_clases()
        if clase=='BUSINESS':
            db['Numeros']=db['Asiento'].apply(orden_num) #aplico la funcion solo en la columna 'Asiento'
            ordenado=db.sort_values(by='Numeros')#creo la columna con los numeros de los asientos y lo ordeno en funcion de ello
            columnas=['Asiento','Apellidos','Nombre']
            print(ordenado[columnas])
            ordenado=ordenado.drop(columns=['Numeros']) #elimino la columna de numeros
        elif clase=='REGULAR':
            dr['Numeros']=dr['Asiento'].apply(orden_num)
            ordenado=dr.sort_values(by='Numeros')
            columnas=['Asiento','Apellidos','Nombre']
            print(ordenado[columnas])
            ordenado=ordenado.drop(columns=['Numeros']) 

#Función que busca asientos disponibles
def buscar_sitio(preferencia, sitios, asientos_reservados, eleccion):
    '''con esta funcion busco los sitios disponibles para cada clase en funcion de la preferencia'''
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

#Función que pide informacion al usuario para crear una nueva reserva
def info_usuario(dt):
    '''comprueba si el dni ya esta en uso y si no lo esta continua ejecuatando la funcion y pidiendo informacion al usuario'''
    print('Introduzca la información pedida en mayusculas')
    dni=input("Por favor, introduzca su DNI: \n")
    #Compruebo si el dni ya esta asociado a una reserva
    if dni in dt['DNI'].values:
        print('Este DNI ya esta en uso, por favor, introduzca un DNI válido')
        menu()
    elif dni not in dt['DNI'].values:
        nombre=input("Por favor, introduzca su nombre: \n")
        apellidos = input("Por favor, introduzca sus apellidos:\n ")
        edad = input("Por favor, introduzca su edad:\n ")
        facturacion = input("¿Desea facturar maletas? (SI/NO): \n")
        return dni, nombre, apellidos, edad, facturacion
    
#Función para asignar el sitio y añadir la reserva 
def add_reserva(asiento,asientos_reservados):
    '''añade una nueva reserva'''
    if asiento is not None:
        eleccion=op_clases() 
        preferencia=op_preferencia()
        asiento=buscar_sitio(preferencia, sitios, asientos_reservados, eleccion)
        asientos_reservados.append(asiento)
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
        dni,nombre,apellidos,edad,facturacion=info_usuario(dt)
        nueva_fila=[dni,nombre,apellidos,asiento,edad,facturacion]
        #Añade la fila al DataFrame
        dt.loc[len(dt)]=nueva_fila
        #Guarda el DataFrame actaulizado en el archivo csv correspondiente
        dt.to_csv(csv_file,index=False)
        #imprime en pantalla la nueva reserva
        print('Reserva añadida con exito')
        print(dt[dt['DNI']==dni])
    else:
        print('No hay asientos disponibles con sus preferencias')

#Función que comprueba si el dni esta en uso o no
def busca_dni(dt):
    '''con esta funcion busco el dni al que esta asociado la reserva que se quiere modficiar, si no lo encuntra no devuelve nada y no continua ejecutando'''
    dni=input("Por favor, introduzca su DNI: \n")
    #Convierte el DNI a la misma forma que en el DataFrame
    buscar=str(dni)
    encontrar=dt[dt['DNI']==buscar]
    if encontrar.empty:
        print(f'No se encontro el dni: {dni}')
        return None
    else:
        print('DNI en el sistema')
        return encontrar 
    
#Función para modificar el asiento
def mod_reserva(sitios,asientos_reservados):
    '''modifica la reserva'''
    dni=input("Por favor, introduzca su DNI: \n")
    print('Introduzca la clase en la que se encuentra su reserva, en caso de que quiera cambiar de reserva debera eliminar la actual y crear una nueva.')
    eleccion=op_clases() #hacer lo mismo en añadir
    preferencia=op_preferencia()
    asiento=buscar_sitio(preferencia,sitios,asientos_reservados,eleccion)
    if sitios is not None:
        numero_sitio=orden_num(asiento)
        if numero_sitio:
            db_1=pd.read_csv('booked_business.csv',dtype={'DNI':str})
            dr_1=pd.read_csv('booked_regular.csv',dtype={'DNI':str})

            buscar_db=busca_dni(db_1)
            buscar_dr=busca_dni(dr_1)

            if buscar_db is not None:
                db_1.loc[db_1['DNI']==str(dni),'Asiento'] = asiento
                db_1.to_csv('booked_business.csv',index=False)
                print('Asiento modificado correctamente')
            elif buscar_dr is not None:
                dr_1.loc[dr_1['DNI']==str(dni),'Asiento']= asiento
                dr_1.to_csv('booked_regular.csv',index=False)
                print('Asiento modificado correctamente')
            else:
                print(f'El DNI: {dni}, no se encuentra en el sistema')
    else:
        print('No hay asientos disponibles con sus preferencias')

#Como la funcion anterior provoca un fallo en los csv, crea una columna de mas, añado la siguiente funcion.
#Funcion correctora
def corregir():
    '''con esta funcion se corrigen efectos colaterales de la de añadir reserva y la de modificar asiento'''
    #Lee los dos archivos csv
    db_b=pd.read_csv('booked_business.csv', dtype={'DNI': str})
    dr_r=pd.read_csv('booked_regular.csv', dtype={'DNI': str})
    #Verficia cada fila en el DataFrame business
    for index, fila in db_b.iterrows():
        numero_asiento=int(re.findall(r'\d+',fila['Asiento'])[0])
        if numero_asiento>8:
            #Mueve la fila al DataFrame regular
            dr_r=pd.concat([dr_r,db_b.loc[index:index]])
            db_b=db_b.drop(index)
    #lo mismo pero en el dataframe regular
    for index, fila in dr_r.iterrows():
        numero_asiento=int(re.findall(r'\d+',fila['Asiento'])[0])
        if numero_asiento<=8:
            db_b = pd.concat([db_b, dr_r.loc[index:index]])
            dr_r = dr_r.drop(index)
    #guarda los dataframes corregidos en los csv
    db_b.to_csv('booked_business.csv',index=False)
    dr_r.to_csv('booked_regular.csv',index=False)

#Funcion para eliminar una reserva
def elim_reserva(db,dr):
    '''elimina una reserva'''
    clase=op_clases()
    dni=input(str("Por favor, introduzca su DNI:\n"))
    if clase=='BUSINESS':
        db=db[db['DNI']!=dni]
        db.to_csv('booked_business.csv',index=False)
        print(f'Reserva del pasajero con DNI: {dni} ,eliminada correctamente\n')
    elif clase=='REGULAR':
        dr=dr[dr['DNI']!=dni]
        dr.to_csv('booked_regular.csv',index=False)
        print(f'Reserva del pasajero con DNI: {dni} ,eliminada correctamente\n')

def menu():
    '''crea el menu que involura todas las funciones establecidas'''
    salir=False
    while not salir:
        seleccion=op_menu() 
        if seleccion=='1':
            info_reservas(db,dr) 
        elif seleccion=='2':
            info_pasajeros(db,dr) 
        elif seleccion=='3':
            add_reserva(asiento,asientos_reservados) 
            corregir()
        elif seleccion=='4':
            mod_reserva(sitios,asientos_reservados) 
            corregir()
        elif seleccion=='5':
            elim_reserva(dr,db) 
        elif seleccion=='6':
            salir=True
            print('Hasta la vista :)')
menu()