import pandas as pd
import csv

dr= pd.read_csv('booked_regular.csv',skipinitialspace=True)
print(dr)
db= pd.read_csv('booked_business.csv',skipinitialspace=True)
print(db)
#para crear el dibujtio del avion
print('       A B C      D E F  ')
print('==========================')

#print(db[['Asiento']])

