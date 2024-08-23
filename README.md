# Sistema de Gestión de Inventario

Este proyecto es un sistema de gestión de inventario diseñado para registrar productos, categorías, proveedores y bodegas, y gestionar el stock de los productos de manera eficiente.

## Características

### Registro de Entidades

- **Producto**: 
  - Atributos: nombre, descripción, precio, stock, categoría.
  - Métodos: agregarStock, retirarStock, calcularValorTotal, consultarDisponibilidad.

- **Categoría**: 
  - Atributos: nombre, descripción.
  - Métodos: agregarProducto, eliminarProducto, consultarProductos.

- **Proveedor**: 
  - Atributos: nombre, dirección, teléfono, lista de productos.
  - Métodos: agregarProducto, eliminarProducto, consultarProductos.

- **Bodega**: 
  - Atributos: nombre, ubicación, capacidad máxima, lista de productos.
  - Métodos: agregarProducto, retirarProducto, consultarStock.

### Gestión de Stock

- Agregar o retirar stock de un producto.
- Calcular el valor total del inventario.
- Consultar la disponibilidad de un producto en una bodega específica.

### Relaciones entre Entidades

- Asociar productos con categorías, proveedores y bodegas.
- Administrar la lista de productos en cada entidad, incluyendo la verificación de capacidad y stock.

### Consultas y Reportes

- Consultar información detallada de productos, categorías, proveedores y bodegas.
- Generar informes de stock por categoría, proveedor y bodega.

## Estructura del Proyecto

inventario/

-.idea/ # Archivos de configuración del proyecto en PyCharm

-.venv/ # Entorno virtual de Python

-src/ # Código fuente del proyecto

--modelos/ # Módulos que definen las clases del modelo de datos

---producto.py # Definición de la clase Producto

---categoria.py # Definición de la clase Categoría

---proveedor.py # Definición de la clase Proveedor

---bodega.py # Definición de la clase Bodega

---main.py # Punto de entrada del programa

 -README.md # Este archivo

