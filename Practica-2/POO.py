class producto:
    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    @property
    def codigo (self):
        return self.__codigo
    
    @codigo.setter
    def codigo (self, valor):
        self.__codigo = valor
    
    @property
    def nombre (self):
        return self.__nombre
    
    @nombre.setter
    def nombre (self, valor):
        self.__nombre = valor

    @property
    def precio (self):
        return self.__precio
    
    @precio.setter
    def precio (self, valor):
        self.__precio = valor
    
    def calcular_total (self, unidades):
        return self.__precio*unidades

    def __str__(self):
        return 'codigo: ' + str (self.__codigo) + ', nombre: ' + str (self.__nombre) + ', precio: ' + str (self.__precio)

class pedido:
    def __init__(self, productos, cantidades):
        self.__productos = productos
        self.__cantidades = cantidades
    
    def total_pedido (self):
        total = 0

        for (a,b) in zip (self.__productos, self.__cantidades):
            total += a.calcular_total(b)
        return total
    
    def mostrar_pedido (self):
        for (a,b) in zip (self.__productos, self.__cantidades):
            print('producto > (', a, ')  cantidad: ', str(b))

p1=producto(1,"producto1",5)
p2=producto(2,"producto2",10)
p3=producto(3,"producto3",15)

print (p1)
print (p2)
print (p3)

print (p1.calcular_total(5))
print (p2.calcular_total(5))
print (p3.calcular_total(5))

productos = [p1, p2, p3]
cantidades = [2, 10, 3]
pedido = pedido (productos, cantidades)

print('Total pedido: ' + str(pedido.total_pedido()))
pedido.mostrar_pedido()