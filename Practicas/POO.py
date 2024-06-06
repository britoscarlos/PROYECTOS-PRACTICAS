TIPO_DESC_FIJO = 'Fijo'
TIPO_DESC_PORC = 'Porcentaje'

class Descuento:

    def __init__(self, tipo, valor):
        if not isinstance (valor, int):
            raise ValueError ('Constructor descuento debe ser un número')
        if not isinstance (tipo, str):
            raise ValueError ('Costructor debe ser un string')
        if tipo != TIPO_DESC_PORC and tipo != TIPO_DESC_FIJO:
            raise ValueError ('Costructor descuento: el tipo debe ser fijo o porcentaje')
        if tipo == TIPO_DESC_FIJO and valor<=0:
            raise ValueError ('Costructor descuento: el valor en el tipo fijo debe ser mayor a 0')
        if tipo == TIPO_DESC_PORC and (valor<=0 or valor>100) :
            raise ValueError ('Costructor descuento: el valor en el tipo porcentaje debe estar entre 0 y 100')
        self.__tipo = tipo
        self.__valor = valor
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, valor):
        self.__tipo == tipo
    
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    
    def aplicar_descuento (self, precio):
        if self.__tipo == TIPO_DESC_FIJO:
            if precio > self.__valor:
                return precio - self.__valor
            else:
                return 0
        else:
            return precio - precio*(self.__valor/100)
            
class Producto:
    def __init__(self, codigo, nombre, precio, descuento=None):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__descuento = descuento

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def precio(self):
        if self.__descuento == None:
            return self.__precio
        else:
            return self.__descuento.aplicar_descuento(self.__precio)
    
    @precio.setter
    def precio(self, valor):
        self.__precio = valor
    
    def calcular_total(self, unidades):
        return self.precio * unidades

    def __str__(self):
        return f'codigo: {self.__codigo}, nombre: {self.__nombre}, precio: {self.__precio}'

class Pedido:
    def __init__(self):
        self.__productos = []
        self.__cantidades = []

    def añadir_producto(self, producto, cantidad):
        if not isinstance(producto, Producto):
            raise Exception('añadir_producto: Producto debe ser de la clase Producto')
        
        if not isinstance(cantidad, int):
            raise Exception('añadir_producto: cantidad debe ser un número')
        
        if cantidad <= 0:
            raise Exception('añadir_producto: cantidad debe ser mayor que 0')

        if producto in self.__productos:
            indice = self.__productos.index(producto)
            self.__cantidades[indice] += cantidad
        
        else:
            self.__productos.append(producto)
            self.__cantidades.append(cantidad)
    
    def eliminar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise Exception('eliminar_producto: Producto debe ser de la clase Producto')
        
        if producto in self.__productos:
            indice = self.__productos.index(producto)
            del self.__productos[indice]
            del self.__cantidades[indice]
        
        else:
            raise Exception('eliminar_producto: Producto no existe')
    
    def total_pedido(self):
        total = 0
        for producto, cantidad in zip(self.__productos, self.__cantidades):
            total += producto.calcular_total(cantidad)
        return total
    
    def mostrar_pedido(self):
        for producto, cantidad in zip(self.__productos, self.__cantidades):
            print(f'producto > ({producto})  cantidad: {cantidad}')

desc1= Descuento (TIPO_DESC_FIJO, 5)
desc2= Descuento (TIPO_DESC_PORC, 50)


p1 = Producto(1, "producto1", 5)
p2 = Producto(2, "producto2", 10, desc1)
p3 = Producto(3, "producto3", 15, desc2)

print(p1)
print(p2)
print(p3)

print(p1.calcular_total(5))
print(p2.calcular_total(5))
print(p3.calcular_total(5))

pedido = Pedido()

try:
    pedido.añadir_producto(p1, 5)
    pedido.añadir_producto(p2, 5)
    pedido.añadir_producto(p3, 5)

    print('Total pedido: ' + str(pedido.total_pedido()))
    pedido.mostrar_pedido()

    pedido.eliminar_producto(p1)

    print('Total pedido: ' + str(pedido.total_pedido()))
    pedido.mostrar_pedido()    

except Exception as e:
    print(e)

print('Total pedido: ' + str(pedido.total_pedido()))
pedido.mostrar_pedido()

