from claseCama import Cama
import numpy as np
from numpy import array
import csv
class ManejadorCamas:
    __arreglo: array
    def __init__(self):
        self.__arreglo=self.CrearCamas()
    
    def CrearCamas(self):
        l=[]
        archivo= open("camas.csv")
        reader = csv.reader(archivo,delimiter=";")
        next(reader, None)
        for fila in reader:
            c=Cama(fila[0], fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
            l.append(c)
        archivo.close()
        arreglo=np.array(l)
        return arreglo
   # def __str__(self):
    #    return str(self.__arreglo)
    
    def show(self):
        for i in range(len(self.__arreglo)):
            print (self.__arreglo[i])
            print("-"*30)
        
    