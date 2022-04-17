"""
Defina una clase “Email” con los siguientes atributos: idCuenta, dominio, tipo de dominio y contraseña (todos estos datos se ingresan por teclado). Y los siguientes métodos:
a- El constructor.
b- Método “retornaEmail()” que construye una dirección e-mail con los valores de los atributos de Email. Por ejemplo:

idCuenta.: alumnopoo
dominio: gmail
tipoDominio: com
Resultado devuelto por retornaEmail: alumnopoo@gmail.com

c- Método “getDominio()”, que retorna el dominio.

d- Método “crearCuenta(), crea una cuenta a partir de una dirección de correo que recibe como parámetro.

Implemente un programa que permita:

1- Ingresar el nombre de una persona y de su cuenta de correo, el identificador de cuenta, dominio y tipo de dominio (crear una instancia de la clase Email) y luego imprima el siguiente mensaje:

Estimado <nombre> te enviaremos tus mensajes a la dirección <dirección de correo>.

2- Para la instancia creada en el ítem anterior, modificar la contraseña, teniendo en cuenta que se debe ingresar la contraseña actual, y ésta debe ser igual a la registrada en la instancia. Luego se debe ingresar la nueva contraseña y realizar la modificación correspondiente.

3- Crear un objeto de clase Email, a partir de una dirección de correo, por ejemplo: informatica.fcefn@gmail.com, juanLiendro1957@yahoo.com, etc.

4- Leer de un archivo separado por comas 10 direcciones de e-mail, crear instancias de la clase Email; luego ingresar un identificador de cuenta e indicar si está repetido o no."""



class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __contraseña = ''

    def __init__(self,idCuenta,dominio,tipoDominio,contraseña):
        self.__idCuenta=idCuenta
        self.__dominio=dominio
        self.__tipoDomionio=tipoDominio
        self.__contraseña=contraseña
    
    def getDominio(self):
        return print(self.__dominio)

    def retornaEmail(self,name):
        return print("Estimado",name.upper(), "te enviaremos tus mensajes a la dirección: ",self.__idCuenta+"@"+self.__dominio+"."+self.__tipoDomionio+"\n")
        #variable + . + upper = CONVIERTE AL STRING EN MAYUSCULA
        
    def crearCuenta(self,correo):
        id=correo.split("@")
        dom=id[1].split(".")
        self.idCuenta=id[0]
        self.dominio=dom[0]
        self.tipoDomionio=dom[1]
        print("Email generado \n")

def changepass(self,actual,vieja):
    if actual==vieja:
        nueva=input("Ingrese su nueva contraseña \n")
        print("Contraseña guardada correctamente \n Su nueva contraseña es:",nueva)
        return nueva
    else:
        print("Contraseña incorrecta \n")

def funciona(self, adrr):
    lista=[]
    for i in range(len(adrr)):
        adrr=Email("","", "", "")
        adrr.crearCuenta(adrr[i])
        lista.append(adrr)
    busca = input("INGRESE CORREO A BUSCAR")
    b=0
    for adrr in lista:
        if adrr.idCuenta == busca:
            b=1
    if b==1:
        print("El id ya se encuentra ingresado")
    else:
        print("El id no se encuentra ingresado")
        
        
if __name__=='__main__':
   # p = Email() #CREACION DE OBJETO EMAIL
   # 1
   nombre = input("NOMBRE \n")
   p = Email (input ("Ingrese identificador de cuenta \n"),input ("Ingrese el dominio de la cuenta \n"),input ("Ingrese tipo de dominio de la cuenta \n"),input("Ingrese la contraseña \n")) #INGRESO DE DATOS
   p.retornaEmail(nombre)
   
   # 2
   p.contraseña = changepass(input("INGRESE CONTRASEÑA"), p.contraseña)
   
   # 3
   p.crearCuenta(input ("Ingrese cuenta de correo de la persona \n"))
   
   # 4
   archivo = open('texto1.csv')
   direc = archivo.read().split(";")
   with open("texto1.csv","r") as archivo:
       direc = archivo.read().split(',')
       funciona(direc)
       archivo.close()
    
'''
Kevin Salinas -- Registro : 21448
'''
