from abc import ABC, abstractmethod
from funciones import borrarPantalla,gotoxy
from datetime import  date

class Persona(ABC):
    def __init__(self, nombre, estado):
        self.nombre = nombre
        self.estado = estado

    @property
    def mostrar_idCodigo(self):
        return self.__idCodigo

    @abstractmethod
    def mostarDatos(self):
        pass

class Cliente(Persona):
    idCliente = 0
    contadorCliente = 1
    def __init__(self, nombre, cedula, estado):
        super().__init__(nombre, estado)
        Cliente.idCliente += 1
        Cliente.contadorCliente += 1
        self.idCliente = Cliente.idCliente
        self.cedula = cedula

    @property
    def mostrar_idCliente(self):
        return self.idCliente

    def mostarDatos(self):
        print(f"Cliente: {self.idCliente} Nombre: {self.nombre} Cedula: {self.cedula} Estado: {self.estado}" )

class Factura:
    idFactura = 0
    contadorFactura = 1
    def __init__(self, cliente, fecha, total, estado):
        Factura.idFactura += 1
        Factura.contadorFactura += 1 
        self.idFactura = Factura.idFactura
        self.cliente = cliente
        self.fecha = fecha
        self.total = total
        self.estado = estado
    
    @property
    def mostrar_idFactura(self):
        return self.idFactura

    def mostarDatos(self):
        print(f"idFactura_ {self.idFactura} Fecha: {self.fecha} Total: {self.total} Estado: {self.estado}")

class CabCredito:
    idCadCredito = 0
    contadorCredito = 1
    def __init__(self, factura, fecha, deuda, numeroCuotas, cuota, aamminicial, detalleCredito, estado):
        CabCredito.idCadCredito +=1
        CabCredito.contadorCredito +=1
        self.idCadCredito = CabCredito.idCadCredito
        self.factura = factura
        self.fecha = fecha
        self.deuda = deuda
        self.numeroCuotas = numeroCuotas
        self.cuota = cuota
        self.aamminicial = aamminicial
        self.detalleCredito = detalleCredito
        self.estado = estado
    
    @property
    def mostrar_idCabCredito(self):
        return self.idCadCredito

    def mostarDatos(self):
        print(f"Id CadCredito: {self.idCadCredito} Código de Factura: {self.factura} Fecha: {self.fecha} Deuda: {self.deuda}")
        print(f"Numero de Cuotas: {self.numeroCuotas} Cuota: {self.cuota} Aamm Inicial: {self.aamminicial} Detalle Crédito: {self.detalleCredito} Estado: {self.estado}")

class DetCredito:
    idDetCredito = 0
    def __init__(self, aamm, cuota, detPago, estado):
        DetCredito.idDetCredito += 1
        self.idDetCredito = DetCredito.idDetCredito
        self.aamm = aamm
        self.cuota = cuota
        self.detPago = detPago
        self.estado = estado
    
    @property
    def mostrar_idDetCredito(self):
        return self.idDetCredito

    def mostarDatos(self):
        print(f"Id DetCredito: {self.idDetCredito} Aamm: {self.aamm} Cuota: {self.cuota} DetPago: {self.detPago.idPago} Estado: {self.estado}")
    def agregarPago(self):
        self.detPago.realizarPAgo()
        self.estado = True
        print("Pago realizado Correctamente")

    @staticmethod
    def getinteres():
        return 1.0

class Pago:
    idPago = 0
    contadorPago = 1
    def __init__(self, fecha, valor):
        Pago.idPago += 1
        Pago.contadorPago += 1
        self.idPago = Pago.idPago
        self.fechaPago = fecha
        self.valor = valor

    @property
    def mostrar_idPago(self):
        return self.idPago

    def mostarDatos(self):
        print(f"Id Pago: {self.idPago} Fecha Pago: {self.fechaPago} Valor: {self.valor}")

    def realizarPAgo(self):
        self.valor = CabCredito.deuda - self.valor
        print("Realizado exitosamente:", self.valor)

class Calculo(ABC):
    @abstractmethod
    def realizarPago(self, int, float):
        pass

def menu():
    borrarPantalla()
    while True:
        gotoxy(65,2);print("\x1b[1;34m" + "----------------------------------------------------------------""\033[0m")
        gotoxy(65,3);print("\x1b[1;44m" +"                       Menú Cuentas Por Cobrar                  ""\x1b[0m")
        gotoxy(65,4);print("\x1b[1;34m" + "----------------------------------------------------------------""\033[0m")
        gotoxy(65,5);print("\x1b[1;35m" + "1. Clientes""\x1b[0m")
        gotoxy(65,6);print("\x1b[1;33m" + "2. Facturas""\x1b[0m")
        gotoxy(65,7);print("\x1b[1;32m" +"3. Créditos""\x1b[0m")
        gotoxy(65,8);print("\x1b[1;36m" +"4. Pagos""\x1b[0m")
        gotoxy(65,9);print("\x1b[1;34m" +"5. Consulta General""\x1b[0m")
        gotoxy(65,10);print("\x1b[1;31m" +"6. Salir""\x1b[0m")
        print("""""")
        opc= int(input("\x1b[1;37m" +"                                                                Seleccione una opción [1...6]:""\033[0m"))
        if opc == 1:
            borrarPantalla()
            while True:
                gotoxy(65,2);print("\x1b[1;34m" + "===== BIENVENIDO AL SISTEMA DE REGISTRO CLIENTES =========""\033[0m")
                gotoxy(65,3);print("\x1b[1;35m" + "1. Ingresar datos del Cliente""\x1b[0m")
                gotoxy(65,4);print("\x1b[1;33m" + "2. Mostrar Datos""\x1b[0m")
                gotoxy(65,5);print("\x1b[1;31m" +"3. Menu Principal""\x1b[0m")
                opc= int(input("\x1b[1;37m" +"                                                                Seleccione una opción [1...3]:""\033[0m"))
                print("""""")
                if opc ==1:
                    borrarPantalla()
                    gotoxy(65,2);print("\x1b[1;34m" + "====== INGRESO DE CLIENTE ========""\033[0m")
                    print("\x1b[1;34m" +"idCliente: ""\033[0m", Cliente.contadorCliente)
                    Persona.nombre = input("\x1b[1;34m" +"Nombre: ""\033[0m")
                    Persona.cedula = int(input("\x1b[1;34m" +"Cedula: ""\033[0m"))
                    Persona.estado = bool(True)
                    cli = Cliente(Persona.nombre, Persona.cedula, Persona.estado)
                    txtCliente.append(cli)
                    with open("./archivos_txt/clientes.txt", "a") as w:
                        for cliente in txtCliente:
                            w.write("idCliente: "+ str(cliente.idCliente) + "\n")
                            w.write("Nombre: "+ cliente.nombre + "\n")
                            w.write("Cedula: "+ str(cliente.cedula) + "\n")
                            w.write("Estado:" + str(cliente.estado) + "\n")
                    print("\x1b[1;31m" +"|================================|""\033[0m")        
                    print("\x1b[1;31m" +"| Cliente agregado correctamente |""\033[0m")
                    print("\x1b[1;31m" +"|================================|""\033[0m")
   
                elif opc ==2:
                    borrarPantalla()
                    try:
                        with open("./archivos_txt/clientes.txt", "r") as archivo:
                            print(archivo.read())
                    except ValueError:
                        print("\x1b[1;31m" +"No hay datos de clientes guardados en el archivo clientes.txt""\033[0m")
                elif opc==3:
                    borrarPantalla()        
                    break
                else:
                    borrarPantalla()
                    print("\x1b[1;31m" +"Opción inválida""\033[0m")

        elif opc == 2:
            borrarPantalla()
            while True:
                gotoxy(65,2);print("\x1b[1;34m" + "====== BIENVENIDO AL SISTEMA DE FACTURACION ========""\033[0m")
                gotoxy(65,3);print("\x1b[1;35m" + "1. Crear Factura""\x1b[0m")
                gotoxy(65,4);print("\x1b[1;33m" + "2. Mostrar Datos""\x1b[0m")
                gotoxy(65,5);print("\x1b[1;31m" +"3. Menu Principal""\x1b[0m")
                opc= int(input("\x1b[1;37m" +"                                                              Seleccione una opción [1...3]:""\033[0m"))
                if opc ==1:
                    borrarPantalla()
                    gotoxy(65,2);print("\x1b[1;34m" + "====== DATOS FACTURA ========""\033[0m")
                    Factura.cliente= input("\x1b[1;33m" +"Cliente: ""\033[0m")
                    Factura.fecha= input("\x1b[1;33m" +"Fecha [DD/MM/AAAA]: ""\033[0m")
                    Factura.total = input("\x1b[1;33m" +"Total $: ""\033[0m")
                    fac1 = Factura(Factura.cliente, Factura.fecha, Factura.total, estado = True)
                    txtFactura.append(fac1)
                    with open("./archivos_txt/facturas.txt", "a") as dato:
                        for factura in txtFactura:
                            dato.write("idFactura: "+str(factura.idFactura) + "\n")
                            dato.write("Cliente: "+factura.cliente + "\n")
                            dato.write("Fecha: " +factura.fecha + "\n")
                            dato.write("Total: " +str(factura.total) + "\n")
                            dato.write("Estado: "+str(factura.estado)+ "\n")
                    print("\x1b[1;31m" +"|================================|""\033[0m")        
                    print("\x1b[1;31m" +"| Factura agregada correctamente |""\033[0m")
                    print("\x1b[1;31m" +"|================================|""\033[0m")
                elif opc == 2:
                    borrarPantalla()
                    try:
                        with open("./archivos_txt/facturas.txt", "r") as archivo:
                            print(archivo.read())
                    except ValueError:
                        print("\x1b[1;31m" +"No hay datos de facturas guardados en el archivo facturas.txt""\033[0m")        
                elif opc == 3:
                    borrarPantalla()
                    break
                else:
                    borrarPantalla()
                    print("\x1b[1;31m" +"Opción inválida""\033[0m")

        elif opc == 3:
            borrarPantalla()
            while True:
                gotoxy(68,2);print("\x1b[1;34m" + "====== BIENVENIDO AL SISTEMA DE CREDITOS ========""\033[0m")
                gotoxy(68,3);print("\x1b[1;35m" + "1. Ingresar Credito ""\x1b[0m")
                gotoxy(68,4);print("\x1b[1;33m" + "2. Mostrar Datos""\x1b[0m")
                gotoxy(68,5);print("\x1b[1;31m" +"3. Menu Principal""\x1b[0m")
                opc= int(input("\x1b[1;37m" +"                                                                    Seleccione una opción [1...3]:""\033[0m"))
                print("""""")
                if opc ==1:
                    borrarPantalla()
                    gotoxy(65,2);print("\x1b[1;34m" + "====== INGRESO DE CREDITO ========""\033[0m")
                    print("\x1b[1;37m" +"idCredito: ""\x1b[0m", CabCredito.contadorCredito)
                    CabCredito.factura = input("\x1b[1;32m" +"N# Factura: ""\033[0m")
                    CabCredito.fecha = input("\x1b[1;32m" +"Escriba la Fecha del Credito [Dias/Mes/Anio]: ""\033[0m")
                    CabCredito.deuda = float(input("\x1b[1;32m" +"Deuda $: ""\033[0m"))
                    CabCredito.numeroCuotas = int(input("\x1b[1;32m" +"N# Cuotas Difiere a Meses: ""\033[0m"))
                    CabCredito.cuota = int(input("\x1b[1;32m" +"Cuota a Pagar: ""\033[0m"))
                    CabCredito.aamminicial = input("\x1b[1;32m" +"AAAA-MM inicial: ""\033[0m")
                    CabCredito.detalleCredito= input("\x1b[1;32m" +"Detalle de Crédito: ""\033[0m")
                    cab= CabCredito(CabCredito.factura, CabCredito.fecha, CabCredito.deuda, CabCredito.numeroCuotas, CabCredito.cuota, CabCredito.aamminicial,CabCredito.detalleCredito, estado = True)
                    txtcabCredito.append(cab)
                    with open("./archivos_txt/creditos.txt", "a") as w:
                        for credito in txtcabCredito:
                            w.write("\n"+" Credito: " + str(credito.idCadCredito) + "\n")
                            w.write("Número de Factura: " + credito.factura + "\n")
                            w.write("Fecha: " + credito.fecha + "\n")
                            w.write("Deuda: " + str(credito.deuda) + "\n")
                            w.write("Numero de Cuotas: " + str(credito.numeroCuotas) + "\n")
                            w.write("Numero de Cuota: " + str(credito.cuota) + "\n")
                            w.write("Año y Mes Inicial: " + str(credito.aamminicial) + "\n")
                            w.write("Detalles de Crédito: " + str(credito.detalleCredito) + "\n")
                            w.write("Estado de Crédito: " + str(credito.estado) + "\n")
                    print("\x1b[1;31m" +"|================================|""\033[0m") 
                    print("\x1b[1;31m" +"Credito agregado correctamente.""\033[0m")
                    print("\x1b[1;31m" +"|================================|""\033[0m") 
                elif opc ==2:
                    borrarPantalla()
                    try:
                        with open("./archivos_txt/creditos.txt", "r") as archivo:
                            print(archivo.read())
                    except:
                        print("\x1b[1;31m" +"No hay datos de créditos guardados en el archivo creditos.txt""\033[0m")
                elif opc ==3:  
                    borrarPantalla()      
                    break 

                else:
                    borrarPantalla()
                    print("\x1b[1;31m" +"Opción inválida""\033[0m")

        elif opc == 4:
            borrarPantalla()
            while True:
                gotoxy(65,1);print("\x1b[1;34m" + "====== BIENVENIDO AL SISTEMA DE PAGOS ========""\033[0m")
                gotoxy(65,2);print("\x1b[1;35m" + "1. Ingresar Credito ""\x1b[0m")
                gotoxy(65,3);print("\x1b[1;33m" + "2. Mostrar Datos""\x1b[0m")
                gotoxy(65,4);print("\x1b[1;31m" +"3. Principal""\x1b[0m")
                opc= int(input("\x1b[1;37m" +"                                                                Seleccione una opción [1...3]:""\033[0m"))
                print("""""")
                if opc ==1:
                    borrarPantalla()
                    gotoxy(65,2);print("\x1b[1;34m" + "====== PAGO ========""\033[0m")
                    print("ID Credito: ", Pago.contadorPago)
                    print(f"Fecha ACtual: {date.today()}")
                    print("\x1b[1;31m" +"|================================|""\033[0m") 
                    Pago.fecha = input("\x1b[1;36m" +"Registre la fecha actual de pago -DD/MM/AAAA- : ""\033[0m")
                    Pago.valor = float(input("\x1b[1;36m" +"Ingrese el Valor a Pagar: ""\033[0m"))
                    pag = Pago(Pago.fecha, Pago.valor)
                    txtPago.append(pag)
                    with open("./archivos_txt/pagos.txt", "a") as w:
                        for pago in txtPago:
                            w.write("ID Pago: "+ str(pago.idPago) + "\n")
                            w.write("Fecha de Pago: " + pago.fecha + "\n")
                            w.write("Valor a Pagar: " + str(pago.valor) + "\n")
                    print("\x1b[1;31m" +"|================================|""\033[0m") 
                    print("\x1b[1;34m" +"Pago agregado correctamente.""\033[0m")
                    print("\x1b[1;31m" +"|================================|""\033[0m") 
                elif opc ==2:
                    borrarPantalla()
                    try:
                        with open("./archivos_txt/pagos.txt", "r") as file:
                            print(file.read())
                    except FileNotFoundError:
                        print("\x1b[1;31m" +"No hay datos de pagos guardados en el archivo pagos.txt""\033[0m")
                elif opc ==3:
                    borrarPantalla()        
                    break  
                else:
                    borrarPantalla()
                    print("\x1b[1;31m" +"Opción inválida""\033[0m")

        elif opc == 5:
            borrarPantalla()
            while True:
                print("\x1b[1;34m" + "======BIENVENIDO AL SISTEMA DE CONSULTA GENERAL========""\033[0m")
                print("\x1b[1;35m" + "1. Mostrar Clientes""\x1b[0m")
                print("\x1b[1;33m" + "2. Mostar Facturas""\x1b[0m")
                print("\x1b[1;32m" +"3. Mostar Créditos""\x1b[0m")
                print("\x1b[1;36m" +"4. Mostar Pagos""\x1b[0m")
                print("\x1b[1;31m" +"5. Menu Principal""\x1b[0m")
                opc = int(input("\x1b[1;37m" +"Seleccione una opción [1...5]:""\033[0m"))
                if opc == 1:
                    borrarPantalla()
                    try:
                        with open("./archivos_txt/clientes.txt", "r") as archivo:
                            print(archivo.read())
                    except FileNotFoundError:
                        print("\x1b[1;31m" +"No hay datos de clientes guardados en el archivo clientes.txt""\033[0m")
                
                elif opc == 2:
                    borrarPantalla()
                    try:
                        with open("./archivos_txt/facturas.txt", "r") as archivo:
                            print(archivo.read())
                    except FileNotFoundError:
                        print("\x1b[1;31m" +"\x1b[1;31m" +"No hay datos de facturas guardados en el archivo facturas.txt""\033[0m")
                elif opc == 3:
                    borrarPantalla()
                    try:
                        with open("./archivos_txt/creditos.txt", "r") as archivo:
                            print(archivo.read())

                    except FileNotFoundError:
                        print("\x1b[1;31m" +"No hay datos de créditos guardados en el archivo creditos.txt""\033[0m")
                elif opc == 4:
                    borrarPantalla()
                    try:
                        with open("./archivos_txt/pagos.txt", "r") as archivo:
                            print(archivo.read())
                    except FileNotFoundError:
                        print("\x1b[1;31m" +"No hay datos de pagos guardados en el archivo pagos.txt""\033[0m")
                elif opc == 5:
                    borrarPantalla()
                    break
                else:
                    borrarPantalla()
                    print("\x1b[1;31m" +"Opción inválida.""\033[0m")    

        elif opc == 6:
            borrarPantalla()
            while True:
                print("\x1b[1;34m" + "=============== DESEAS SALIR ================""\033[0m")
                print("\x1b[1;35m" + "1. Si""\x1b[0m")
                print("\x1b[1;33m" + "2. Menu Principal""\x1b[0m")
                opcion = int(input("\x1b[1;36m" +"Digite el numero de la opcion a ejecutar: ""\033[0m"))
                if opcion == 1:
                    print("\x1b[1;31m" + "Gracias por usar nuestro programa xD""\033[0m")
                    exit()
                elif opcion == 2:
                    menu()
                else:
                    borrarPantalla()
                    print("\x1b[1;31m" +"Opción inválida""\033[0m")
        else:
            borrarPantalla()
            print("\x1b[1;31m" +"Opción inválida""\033[0m")
txtCliente=[]
txtFactura=[]
txtcabCredito=[]
txtPago=[]
menu()
