import pandas as pd
import csv

dr= pd.read_csv('booked_regular.csv',skipinitialspace=True)
db= pd.read_csv('booked_business.csv',skipinitialspace=True)

print(db)
print(dr)
#para crear el dibujtio del avion
print('       A B C      D E F  ')
print('==========================')

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