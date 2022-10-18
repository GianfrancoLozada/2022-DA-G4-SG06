class Producto():
    def __init__ (self, codigoBarras, nombre, fechaVencimiento, precio):
        self.codigoBarras = codigoBarras 
        self.nombre - nombre 
        self.fechavencimiento = fechavencimiento 
        self.precio = precio

    def mostrarProducto (self):
        show = "IIIIIIII|||PRODUCTO|||IIIIIIII\nNo Código: [ \nNombre: {}\nFecha de vencimiento: {} \nPrecio: S/.{}\n" 
        print(show. format (self.codigoBarras, self.nombre, self. fechaVencimiento, self.precio))

class Venta(): 
    def __init__ (self, nVenta, comprobante, total):
        self.nVenta = nVenta 
        self.comprobante = comprobante 
        self. total = total

    def mostrarVenta (self):
        showV = "IIIIIIII||VENTA|||||II||||\nN Venta: {}\nComprobante: {} \nTotal: S/. {]\n" 
        print (showv.format (self.nVenta, self.comprobante, self.total))

class Cliente(): 
    def __init__(self, dni, nombreCompleto, metodoPago, saldo, deuda):
        self. dni = dni 
        self.nombreCompleto = nombreCompleto 
        self.metodoPago = metodoPago 
        self. saldo = saldo 
        self.deuda = deuda

def mostrarcliente (self):
    sh = "11111111111CLIENTE 111111111\nDNI: {}\nNombre completo: {}\nMetodo pago: {}\nSaldo: S/.{}\nDeuda: {}" 
    print(sh.format(self.dni, self.nombreCompleto, self.metodoPago, self.saldo, self.deuda))

opc = input ("Desea ingresar al programa? S/N: ") 
while (opc == 's' or opc == 'S'):
    print("") 
    print("IIIIIIIIIIIIIIIIIIIIIIIIIII") 
    print("II Bienvenido III") 
    print("IIIIIIIIIIIIIIIIIIIIIIIIIII") 
    print("") 
    print("------------Menu-----------") 
    print("") 

opcp = int(input ("Cuantos productos ingresará? ")) 
nProd = 1 
while (opcP >= 1 and nProd >= 1):
    print("***Ingresar datos del producto ", nProd, ": ") 
    codeBar = int (input ("Ingresar codigo: ")) 
    nameProd = input ("Ingresar nombre: ") 
    exDate = input ("Ingresar fecha de vencimiento: ") 
    price = int(input ("Ingresar precio: ")) 
    Productol = Producto (codeBar, nameProd, exDate, price) 
    Productol.mostrarProducto () 
    nProd = nprod + 1 
    opcP = opce - 1
opcC = int (input ("Cuantos clientes ingresará? ")) 
ncli = 1 
while (opcC >= 1 and ncli >= 1):
    print("***Ingresar datos del cliente: ***\n") 
    idCode = int (input ("Ingresar DNI: ")) 
    compName = input ("Ingresar nombre: ") 
    methPay = input ("Ingreasar metodo de pago: ") 
    balance = int(input("Ingresar saldo disponible: ")) 
    debt = input ("¿Es deudor?:") 
    Clientel = Cliente(idCode, compName, methPay, balance, debt) 
    Clientel.mostrarCliente() 
    ncli = ncli + 1 
    opcC = opcC - 1

opcV = int (input ("Cuantas ventas ingresará? ")) 
nveni = 1
while (opeV >= 1 and nVen >= 1):
    print("***Ingresar datos de la venta: ***\n") 
    nSell = int (input ("Ingresar N° de venta: ")) 
    purchase = input ("Ingresar tipo de comprobante: ") 
    tot = int (input ("Ingresar total: ")) 
    Vental = Venta (nSell, purchase, tot) 
    Vental.mostrarVenta () 
    nVen = nVen + 1 
    opet = opeV - 1