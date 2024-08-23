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