class Producto():
    def _init_(self, codigoBarras, nombre, fechaVencimiento, precio):
        self.codigoBarras = codigoBarras 
        self.nombre = nombre 
        self.fechaVencimiento = fechaVencimiento 
        self.precio = precio

    def mostrarProducto (self):
        show = "1111111111 PRODUCTO 1111111111\nNo Código: {}\nNombre: {}\nFecha de vencimiento: {}\nPrecio: S/.{}\n" 
        print (show. format (self.codigoBarras, self.nombre, self. fechaVencimiento, self.precio))
codeBar = int(input ("Ingresar codigo: ")) 
nameProd = input ("Ingresar nombre: ") 
exDate = input ("Ingresar fecha de vencimiento: ") 
price = int(input ("Ingresar precio: "))

Productol = Producto (codeBar, nameProd, exDate, price) 
Productol.mostrarProducto ()

class Venta(): 
    def _init__(self, nVenta, comprobante, total):
        self.nVenta = nVenta 
        self.comprobante = comprobante 
        self.total = total
def mostrarVenta (self):
    showV = "IIIIIIIIIIIVENTAIIIIIIIIIII\nN° Venta: {} \nComprobante: {}\nTotal: S/.{} \n" 
    print (showV. format (self.nventa, self.comprobante, self.total))
    nSell = int (input("Ingresar N° de venta: ")) 
    purchase = input ("Ingresar tipo de comprobante: ") 
    tot = int (input ("Ingresar total: "))
    Vental = Venta (nSell, purchase, tot) 
    Vental.mostrarVenta ()

class cliente(): 
    def init__(self, dni, nombreCompleto, metodoPago, saldo, deuda):
        self.dni = dni 
        self.nombreCompleto = nombreCompleto 
        self.metodoPago = metodoPago 
        self.saldo = saldo 
        self.deuda = deuda

def mostrarCliente (self):
    sh = "IIIIIIIIII CLIENTE 1111111111\nDNI: {} \nNombre completo: {} \nMetodo pago: {}\nSaldo: S/. {} \nDeuda: {}" 
    print(sh.format (self.dni, self.nombreCompleto, self.metodoPago, self.saldo, self.deuda))

idCode = int(input("Ingresar DNI: ")) 
compName = input ("Ingresar nomore: ") 
methPay = input ("Ingreasar metodo de pago: ") 
balance = int (input("Ingresar saldo disponible: ")) 
debt = input ("¿Es deudor?: ")
Clientel = Cliente(idCode, compName, methPay, balance, debt) 
Clientel.mostrarCliente()

