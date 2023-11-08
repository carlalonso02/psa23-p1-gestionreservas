import pandas as pd
import csv
cols=['DNI','Nombre', 'Apellidos', 'Asiento', 'Edad', 'Facturacion']
db= pd.read_csv('booked_business.csv',names=cols,skipinitialspace=True)
dr= pd.read_csv('booked_regular.csv',names=cols,skipinitialspace=True)
print(db)
print(dr)

#Dibujito del avion
sitios = [f"{fila}{sitio}" for fila in range(1, 21) for sitio in 'ABCDEF']
asientos_reservados = db['Asiento'].tolist() + dr['Asiento'].tolist()
print(' ')
print('    A B C    D E F  ')
print('==========================')
for fila in range(1, 21):                        
    print(f'{fila:02d}  ', end='')               
    for sitio in 'ABC':                          
        if f'{fila}{sitio}' in asientos_reservados:    
            print('R', end=' ')
        else:
            print('L', end=' ')                 
    print('   ', end='')
    for sitio in 'DEF':                           
        if f'{fila}{sitio}' in asientos_reservados:
            print('R', end=' ')
        else:
            print('L', end=' ')
    print()

print(' ')

#Pasajeros en cada clase
filas_b=db.shape[0]
filas_r=dr.shape[0]

#Porcentaje de ocupación
def porcent_ocupacion(db,dr):
    pasajeros=filas_b + filas_r
    div=pasajeros/120
    pocnt=div*100
    return round(pocnt,2)

#Calculo numero de pasajeros facturan maleta
columna_b=db['Facturacion']
columna_r=dr['Facturacion']
def num_facturas_b(db,columna_b):
    contador=0
    for i in columna_b:
        if str(i).strip().lower().startswith('s'):
            contador+=1
    return contador
def num_facturas_r(dr,columna_r):
    contador2=0
    for i in columna_r:
        if str(i).strip().lower().startswith('s'):
            contador2+=1
    return contador2
def facturacion_tot(num_facturas_b,num_facturas_r):
    contador=num_facturas_b(db,columna_b)
    contador2=num_facturas_r(dr,columna_r)
    total=contador + contador2
    return total

print('El vuelo está un ',porcent_ocupacion(db,dr), '% ocupado' )
print(filas_b, ' pasajeros alojados en business y ', filas_r, 'pasajeros alojados en turista')
print(facturacion_tot(num_facturas_b,num_facturas_r),' pasajeros facturan maletas')

#Menu
def print_menu():
    print()
    print('MENU:\n')
    print('1.Mostrar informacion de reservas\n')
    print('2.Mostrar pasajeros\n')
    print('3.Añadir reserva\n')
    print('4.Modificar reserva\n')
    print('5.Eliminar reserva\n')
    print('6.Salir\n')

def print_clases():
    print()
    print('Tipos de clases:')
    print('Clase 1: Business')
    print('Clase 2: Turista\n')
    nuevo_pb=pb
    
def añadir_reserva(db,dr):
    print_clases()
    clase=input(str('Eliga una clase\n'))
    print(F'Clase elgida: {clase}\n')
    
    datos={'DNI':[input('Introduzca su DNI con el ultimo caracter en mayuscula\n')],
           'Nombre':[input('Introduzca su nombre\n')],
           'Apellidos':[input('Introduzca sus apellidos\n')],
           'Asiento':[input('Introduzca su asiento deseado\n')],
           'Edad':[input('Introduzca su edad\n')],
           'Facturacion':[input('¿Desea facturar su maleta? introudzco si o no\n')]}
    
    agregar=pd.DataFrame(datos)
    
    if clase=='1':
        nuevo_B=pd.concat([db,agregar],ignore_index=True)
        nuevo_B.to_csv('booked_business.csv', index=False)
        print('Reserva en clase Business agregada correctamente')
    elif clase=='2':
        nuevo_R=dr.concat([dr,agregar],ignore_index=True)
        nuevo_R.to_csv('booked_regular.csv', index=False)
        print('Reserva en clase turista agregada correctamente')
    else:
        print('Introduzca una clase valida')
    
def info_reservas():
    
def info_pasajeros():
    

def modificar_reserva():
    
    
def eliminar_reserva(db,dr):
    clase=input(str('Eliga una clase\n'))
    print(F'Clase elgida: {clase}\n')
    condicion=input(str('Introduzca DNI del pasajero con la ultima letra en mayuscula:\n'))
    if clase=='1':
        db=db[db['DNI']!=condicion]
        db.to_csv('booked_business.csv',index=False)
        print('Reserva eliminada correctamente\n')
    elif clase=='2':
        dr=dr[dr['DNI']!=condicion]
        dr.to_csv('booked_regular.csv')
        print(F'Reserva del pasajero con DNI: {condicion} ,eliminada correctamente\n')

    else:
        print('Introduzca una clase valida')
    
def menu_complex():
    print_menu()
    salir=False
    while not salir:
        print_menu00()
        opcion=input('Introduce una opcion: \n')
        print(F'Opcion seleccionada:{opcion}\n')
        if opcion =="1":
            info_reservas()
        elif opcion =="2":
            info_pasajeros()
        elif opcion=="3":
            añadir_reserva(db,dr)
        elif opcion=="4":
            modificar_reserva()
        elif opcion=="5":
            eliminar_reserva(db,dr)
        elif opcion=="6":
            salir=True
        else:
            print('Introduzca una opcion valida')

