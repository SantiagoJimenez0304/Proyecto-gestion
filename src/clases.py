class Producto:
    def __init__(self, nombre: str, descripcion: str, precio: float, stock: int, categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def agregarStock(self, cantidad: int) -> None:
        self.stock += cantidad

    def retirarStock(self, cantidad: int) -> None:
        if cantidad <= self.stock:
            self.stock -= cantidad
        else:
            raise ValueError("No hay suficiente stock para retirar la cantidad solicitada")

    def calcularValorTotal(self) -> float:
        return self.precio * self.stock

    def consultarDisponibilidad(self, bodega) -> int:
        if self in bodega.productos:
            return bodega.consultarStock()[self]
        else:
            return 0

class Categoria:
    def __init__(self, nombre: str, descripcion: str):
        self.nombre = nombre
        self.descripcion = descripcion
        self.productos = []

    def agregarProducto(self, producto) -> None:
        self.productos.append(producto)

    def eliminarProducto(self, producto) -> None:
        if producto in self.productos:
            self.productos.remove(producto)

    def consultarProductos(self) -> list:
        return self.productos

class Proveedor:
    def __init__(self, nombre: str, direccion: str, telefono: str):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos = []

    def agregarProducto(self, producto) -> None:
        self.productos.append(producto)

    def eliminarProducto(self, producto) -> None:
        if producto in self.productos:
            self.productos.remove(producto)

    def consultarProductos(self) -> list:
        return self.productos

class Bodega:
    def __init__(self, nombre: str, ubicacion: str, capacidadMaxima: int):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidadMaxima = capacidadMaxima
        self.productos = {}

    def agregarProducto(self, producto, cantidad: int) -> None:
        if sum(self.productos.values()) + cantidad <= self.capacidadMaxima:
            if producto in self.productos:
                self.productos[producto] += cantidad
            else:
                self.productos[producto] = cantidad
        else:
            raise ValueError("No hay suficiente espacio en la bodega para agregar la cantidad solicitada")

    def retirarProducto(self, producto, cantidad: int) -> None:
        if producto in self.productos and self.productos[producto] >= cantidad:
            self.productos[producto] -= cantidad
            if self.productos[producto] == 0:
                del self.productos[producto]
        else:
            raise ValueError("No hay suficiente stock del producto en la bodega para retirar la cantidad solicitada")

    def consultarStock(self) -> dict:
        return self.productos


categoria_lacteos = Categoria("Lácteos", "Productos derivados de la leche")


producto_leche = Producto("Leche", "Leche entera pasteurizada", 3000.0, 100, categoria_lacteos)


categoria_lacteos.agregarProducto(producto_leche)


proveedor = Proveedor("Proveedor 1", "Calle 123", "555-1234")
proveedor.agregarProducto(producto_leche)


bodega = Bodega("Bodega Central", "Ciudad", 1000)
bodega.agregarProducto(producto_leche, 50)

print(bodega.consultarStock())

print(producto_leche.calcularValorTotal())
