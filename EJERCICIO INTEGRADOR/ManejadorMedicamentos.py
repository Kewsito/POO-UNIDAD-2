from claseMedicamentos import Medicamento
import numpy as np
from numpy import array
import csv
class manejadorMedicamentos:
    __arreglo: array
    
    def __init__(self):
        self.__arreglo=self.CrearMedicamento()
        
    def CrearMedicamento(self):
        lista=[]
        archivo= open("medicamentos.csv")
        reader=csv.reader(archivo,delimiter=";")
        next(reader,None)
        for fila in reader:
            c=Medicamento(fila[0], fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
            lista.append(c)
        archivo.close()
        arr=np.array(lista)
        return arr
    
    def show(self):
        for i in range(len(self.__arreglo)):
            print(self.__arreglo[i])
            print("-"*30)