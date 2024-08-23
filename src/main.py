from Producto import Producto
from Bodega import Bodega
from Proovedor import Proveedor
from Categoria import Categoria

def main():

    categoria_alimentos = Categoria("Alimentos", "Productos alimenticios")
    categoria_bebidas = Categoria("Bebidas", "Todo tipo de bebidas")


    pan = Producto("Pan", "Pan integral", 1.50, 100, categoria_alimentos)
    jugo = Producto("Jugo", "Jugo de naranja", 2.00, 50, categoria_bebidas)


    categoria_alimentos.agregarProducto(pan)
    categoria_bebidas.agregarProducto(jugo)


    proveedor = Proveedor("Proveedor ABC", "Calle 123", "123456789")
    proveedor.agregarProducto(pan)
    proveedor.agregarProducto(jugo)


    bodega = Bodega("Bodega Central", "Av. Principal", 500)


    bodega.agregarProducto(pan, 50)
    bodega.agregarProducto(jugo, 30)


    print("Stock en bodega:")
    for producto, cantidad in bodega.consultarStock().items():
        print(f"{producto.nombre}: {cantidad} unidades")


    print(f"Valor total del stock de {pan.nombre}: ${pan.calcularValorTotal()}")

if __name__ == "__main__":
    main()
