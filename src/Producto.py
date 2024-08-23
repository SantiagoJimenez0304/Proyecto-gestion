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




