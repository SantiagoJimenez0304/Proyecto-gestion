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