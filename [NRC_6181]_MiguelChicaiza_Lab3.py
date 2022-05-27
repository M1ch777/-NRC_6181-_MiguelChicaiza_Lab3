'''  Tema: Diseño de clases, atributos y métodos 
     Lab 3
     Nombre: Miguel Chicaiza
     Asignatura: POO 
     Fecha de entrega: 26/05/2022 '''
#----------------------------------------------------------------------------------------------------------------------------------------
'''Guardamos los datos en dos listas para luego acceder a ellas'''
'''Lista Global para Clientes'''
lista=[] #Lista global 1
'''Lista Global para Registro de Tiendas
'''
ListaTienda=[] #Lista global 2

'''Lista de Clores para cambiar de Color los Mensajes en pantalla
EJEMPLO DE USO:
 print(RESET+"En que Tienda quiere Registrarse: ")

'''
BLACK = '\033[30m'   #Color Negro
RED = '\033[31m'     #Color Rojo
GREEN = '\033[32m'   #Color Verde
YELLOW = '\033[33m'  #Color Amarillo
BLUE = '\033[34m'    #Color Azul
MAGENTA = '\033[35m' #Color Magenta
CYAN = '\033[36m'    #Color celeste saturado
WHITE = '\033[37m'   #Color Blanco Claro
RESET = '\033[39m'   #Color Blanco Original
'''
------------------------------------| PRIMERA CLASE CLIENTE|-------------------------------------------------------

'''
#-------------------------------------------------------------------------
#                         CLASE CLIENTE                                  |
#-------------------------------------------------------------------------
class Cliente:
    '''Constructor con sus parametros'''
    def __init__(self,nombre,telefono,estado,usuario,contraseña):
        self.nombre=nombre
        self.telefono=telefono
        self.estado=estado
        self.usuario=usuario
        self.contraseña=contraseña

#-------------------------------------------------------------------------
    '''Funcion para Registrar a los clientes (Obtener datos )'''
    def Registrar():
        '''Llamamos a la clase Cliente para poder guardar los datos en los objetos'''
        C = Cliente
        C.nombre=input("Ingrese su Nombre: ")
        C.telefono=input("Ingrese un número de teléfono: ")
        C.estado=input("Ingrese su estado de COVID (Normal o Caso): ")
        C.usuario=input("Ingrese su usuario: ")
        C.contraseña=input("Ingrese su contraseña: ")
        lista.append(C)
 #-------------------------------------------------------------------------       
    '''Funcion para Iniciar Sesion mediante los datos obtenidos de la Funcion Registrar()'''
    def  IniciarSesion(): 
        contador=0
        i=3
        '''Iniciamos con un menu para iniciar sesion '''
        while contador !=3:
            print("-----------| Iniciar Sesion |-----------")
            usuarios=input("Ingrese su usuario: ")
            contraseñas=input("Ingrese su contraseña: ")
            print("-----------------------------------")
            exixte=False
            '''Con el for vamos a buscar el usuario y la contraseña en la lista'''
            for C in lista: 
                '''Si es corecto ingresamos al sigiente if'''
                if C.usuario == usuarios and C.contraseña==contraseñas: 
                    print("-----------------------------------")
                    print("Gracias por Ingresar")
                    exixte=True
                    break
            if exixte==True: 
                '''Si se encontro el usuario y contraseña nis imprime un mensaje y ingresamos al menu2()'''
                print("-----------------------------------")
                print("Usuario encontrado")
                menu2()
                '''Caso contrario si no se encontro el usuario y la contraseña, el usuario va a tener 3 intentos para ingresar correctamente los datos'''
            else: 
                ''' i inicia en 3 y va restando 1 por cada intento erroneo'''
                i=i-1 
                print("-----------------------------------")
                print("||     Usuario No encontrado     ||")
                print("-----------------------------------")
                '''Mensaje mostrando los intentos que tiene el usuario'''
                print("Le queda ", i, " Intentos") 
                if i==0: 
                    '''Si el contador llega a Cero va a regresar al menu principal llamado menu()'''
                    print("-----------------------------------")
                    print("||     Ya no tienes Intentos     ||")
                    break
#-------------------------------------------------------------------------------------------------------------------------------------
    '''Funcion para Mostrar los Registros de los clientes '''
    def registroClientes():
        for C in lista:
            print("--------------------------------------------------------------------------------------------------------")
            print(" NOMBRE: ",C.nombre," TELEFONO: ",C.telefono," ESTADO: ",C.estado," USUARIO: ",C.usuario," CONTRASEÑA: ",C.contraseña)
            print("--------------------------------------------------------------------------------------------------------")
#-------------------------------------------------------------------------------------------------------------------------------------
    '''Funcion para Mostrar los Estados de los clientes '''
    def Ver_Estado():
        print("Estados")
        for t in ListaTienda:
            print("--------------------------------------------------------------------------------------------------------")
            print(" TIENDA: ",t.tiendat," NOMBRE: ",t.nombret," ESTADO: ",t.estadot)
            print("--------------------------------------------------------------------------------------------------------")
#-------------------------------------------------------------------------------------------------------------------------------------
'''
------------------------------------| SEGUNDA CLASE TIENDAS |-------------------------------------------------------
'''
#-------------------------------------------------------------------------
#                         CLASE TIENDA                                   |
#-------------------------------------------------------------------------
class Tiendas():
    '''Constructor con sus parametros'''
    def __init__(self,tiendat,nombret,telefonot,estadot,fechat,horat):
        self.tiendat=tiendat
        self.nombret=nombret
        self.telefonot=telefonot
        self.estadot=estadot
        self.fechat=fechat
        self.horat=horat
#-------------------------------------------------------------------------------------------------------------------------------------
    '''Funcion de Registro de los clientes que ingresan a una Tienda'''
    def Registro_Tienda(): 
        '''Llamamos a la class Tiendas'''
        t=Tiendas
        print("-------------| Registrar Tienda |---------------")
        t.tiendat=input("Ingrese el nombre de la Tienda: ")
        t.nombret=input("Ingrese su nombre: ")
        t.telefonot=input("Ingrese su numero de telefono: ")
        t.estadot=input("Ingrese su Estado: ")
        t.fechat=input("Ingrese su HORA de registro: ")
        t.horat=input("Ingrese su FECHA de registro: ")
        ListaTienda.append(t)
#-------------------------------------------------------------------------------------------------------------------------------------
    '''Funcion para mostrar la lista de clientes registrados en una tienda'''
    def Historial_Tiendas(): 
        print("Historial de Tiendas")
        for t in ListaTienda:
            print("--------------------------------------------------------------------------------------------------------")
            print(" TIENDA: ",t.tiendat," NOMBRE: ",t.nombret," TELEFONO: ",t.telefonot," ESTADO: ",t.estadot," FECHA ",t.fechat," HORA ",t.horat,)
            print("--------------------------------------------------------------------------------------------------------")
#-------------------------------------------------------------------------------------------------------------------------------------
    '''Funcion Para Modificar el Estado de un Usuario'''
    def Modestadoclientes():
        '''Lee la lista buscando los estados registrados'''
        for t in ListaTienda:
            '''Si el estado es Normal lo cambia a Caso'''
            if t.estadot == 'Normal':
                t.estadot='Caso'
            
            else:
                '''Caso contrario lo cambia a Normal '''
                t.estadot = 'Normal'
#-------------------------------------------------------------------------------------------------------------------------------------
'''
------------------------------------| TERCERA CLASE ADMI |-------------------------------------------------------
'''
#-------------------------------------------------------------------------
#                           CLASE ADMI                                   |
#-------------------------------------------------------------------------
class admi():
    '''Constructor con sus parametros'''
    def __init__(self):
        ''' Usuario Master '''
        self.usu_Master=("123456")
        ''' Contraseña Master '''
        self.contr_Master=("Admi") 
    def InicioAdmi():
        A=admi()
        contador=0
        i=3
        while contador !=3:
            print(YELLOW+"-------------| Iniciar Sesion |-------------")
            print(RESET+"---------------------------------------------")
            usuarios=input("Ingrese su usuario (Admi): ")
            contraseñas=input("Ingrese su contraseña (123456): ")
            if A.contr_Master == usuarios and A.usu_Master==contraseñas:
                print("-----------------------------------")
                print(YELLOW+"------| MODO ADMI ACTIVADO ;) |------")
                menuAdmi()
            else:
                i=i-1
                print("---------------------------------------------")
                print(YELLOW+"-----| Usuario o Contraseña Incorrecta |-----")
                print(YELLOW+"-----|    Le queda  ",i," Intentos       |-----")
                print("---------------------------------------------")
                if i==0:
                    print("---------------------------------------------")
                    print(YELLOW+"|          Ya no tienes Intentos            |")
                    print(RESET+"---------------------------------------------")
                    break
    '''Funcion Salir'''
    def Salir():
        print("Salir")
        exit()
'''---------------------------------------------------------------------------------------------------------------------------------'''
'''                                Instanciar desde menus                                                                        '''
'''--------------------------------------Menu Principal-----------------------------------------------------------------------------'''
def menu():
    seleccion=0
    while seleccion != 4: 
        print(GREEN+"-----------------------------------------------------------------------")
        print(RESET+"||      Rastreo de Contactos simplificado para COVID-19(MENU 1)      ||")
        print(GREEN+"-----------------------------------------------------------------------")
        print(RESET+"||                           MENU 1                                  ||")
        print(GREEN+"-----------------------------------------------------------------------")
        print(RESET+"||  1) Registrar una cuenta en el sistema                            ||")
        print(RESET+"||  2) Iniciar sesion en el sistema                                  ||")
        print(RESET+"||  3) Admi                                                          ||")
        print(RESET+"||  4) Salir                                                         ||")
        print(GREEN+"-----------------------------------------------------------------------")
        seleccion= int(input(RESET+"Elija una opción: "))
        if seleccion ==1:
            Cliente.Registrar()
        if seleccion==2:
            Cliente.IniciarSesion()
        if seleccion==3:
            admi.InicioAdmi()
        if seleccion==4:
            admi.Salir()

'''------------------------------------------Menu Secundario--------------------------------------------------------------------------         
'''
def menu2():
    seleccion=0
    while seleccion != 4:    
        print(GREEN+"-----------------------------------------------------------------------")
        print(RESET+"||    Rastreo de Contactos simplificado para COVID-19(MENU 2)        ||")
        print(GREEN+"-----------------------------------------------------------------------")
        print(RESET+"||                           MENU 2                                  ||")
        print(GREEN+"-----------------------------------------------------------------------")
        print(RESET+"||  1) Registrarse a una tienda                                      ||")
        print(RESET+"||  2) Ver el historial de las tiendas que visito                    ||")
        print(RESET+"||  3) Ver su estado                                                 ||")
        print(RESET+"||  4) Salir                                                         ||")
        print(GREEN+"-----------------------------------------------------------------------")
        seleccion= int(input(RESET+"Elija una opción: "))
        if seleccion==1:
            menuTiendas()
        if seleccion==2:
            Tiendas.Historial_Tiendas()
        if seleccion==3:
            Cliente.Ver_Estado()
        if seleccion==4:
            menu()

'''----------------------------------------------Menu Tiendas----------------------------------------------------------------------
'''
def menuTiendas():
    seleccion=0
    while seleccion != 4:  
        print(GREEN+"-----------------------------------------------------------------------")
        print(RESET+"||                           Menu Tiendas                            ||")
        print(GREEN+"-----------------------------------------------------------------------")
        print(RESET+"||  En que Tienda quiere Registrarse:                                ||")
        print(RESET+"||  1) Tesco                                                         ||")
        print(RESET+"||  2) SuperMaxi                                                     ||")
        print(RESET+"||  3) TIA                                                           ||")
        print(RESET+"||  4) Salir                                                         ||")
        print(GREEN+"-----------------------------------------------------------------------")
        seleccion= int(input(RESET+"Elija una opción: "))
        if seleccion==1:
            print("Bienvenido a Tesco")
            gerente="Manuel"
            Tiendas.Registro_Tienda()
        if seleccion==2:
            print("Bienvenido a SuperMaxi")
            gerente="Raul"
            Tiendas.Registro_Tienda()
        if seleccion==3:
            print("Bienvenido a TIA")
            gerente="Marco"
            Tiendas.Registro_Tienda()
        if seleccion==4:
            menu2()

'''-------------------------------------------------Menu Admi-------------------------------------------------------------------------
'''
def menuAdmi():
    seleccion=0
    while seleccion != 5:  
        print(GREEN+"-----------------------------------------------------------------------")
        print(RESET+"||                           MODO ADMI                               ||")
        print(GREEN+"-----------------------------------------------------------------------")
        print(RESET+"||  1) Ver Clientes Registrados                                      ||")
        print(RESET+"||  2) Ver Historial Tienda                                          ||")
        print(RESET+"||  3) Ver Estado de Clientes                                        ||")
        print(RESET+"||  4) Modificar Estado de clientes                                  ||")
        print(RESET+"||  5) Salir                                                         ||")
        print(GREEN+"-----------------------------------------------------------------------")
        seleccion= int(input(RESET+"Elija una opción: "))
        if seleccion==1:
            print("Ver Clientes Registrados")
            Cliente.registroClientes()
        if seleccion==2:
            print()
            Tiendas.Historial_Tiendas()
        if seleccion==3:
            print("Ver Estado de Clientes")
            Cliente.Ver_Estado()
        if seleccion==4:
            print("Modificar Estado de clientes")
            Tiendas.Modestadoclientes()
        if seleccion==5:
            menu()
'''
------------------------------------| FIN DE MENUS |-------------------------------------------------------
'''

'''Ejecucion del Primer Menu'''

menu()