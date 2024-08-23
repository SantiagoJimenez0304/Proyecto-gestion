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