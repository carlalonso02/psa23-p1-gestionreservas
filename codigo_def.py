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