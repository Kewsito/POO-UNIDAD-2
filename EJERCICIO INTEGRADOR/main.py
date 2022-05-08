from ManejadorCamas import ManejadorCamas
from ManejadorMedicamentos import manejadorMedicamentos
if __name__=='__main__':
    camas=ManejadorCamas()
    camas.CrearCamas()
    medicamento=manejadorMedicamentos()
    medicamento.CrearMedicamento()
    medicamento.show()
    op=int(input("Ingrese una opcion \n 0 - Salir"))
    while op!=0:
        if op==1:
            camas.show()
        
        
        op=int(input("Ingrese una opcion\n 1 - Mostrar pacientes 2- Mostrar Medicamentos \n 0 - Salir"))
        
