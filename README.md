
# Sistema de Gestión de Inventario

Este proyecto es un sistema de gestión de inventario desarrollado en Python. El sistema permite la administración eficiente de productos, categorías, proveedores y bodegas, facilitando la gestión de stock y la generación de informes detallados.

## Descripción General

El sistema está diseñado para empresas que necesitan controlar su inventario de manera precisa. Permite registrar y gestionar productos, organizar productos en categorías, asociar productos con proveedores y manejar la distribución y almacenamiento en bodegas. Además, incluye funciones para calcular el valor total del stock disponible y generar reportes informativos.

## Características Principales

### Registro de Entidades

- **Productos**: Permite registrar productos con nombre, descripción, precio, stock inicial y categoría.
- **Categorías**: Permite organizar productos en categorías con un nombre y una descripción.
- **Proveedores**: Gestiona proveedores con información de contacto y la lista de productos que suministran.
- **Bodegas**: Maneja bodegas con nombre, ubicación, capacidad máxima y lista de productos almacenados.

### Gestión de Stock

- **Agregar Stock**: Permite incrementar el stock de productos existentes.
- **Retirar Stock**: Permite disminuir el stock de productos disponibles.
- **Cálculo del Valor Total del Stock**: Calcula el valor total del inventario basado en el precio y la cantidad disponible de cada producto.
- **Consulta de Disponibilidad**: Verifica la disponibilidad de productos en una bodega específica.

### Consultas y Reportes

- **Consulta de Productos**: Permite consultar detalles de los productos, incluyendo su categoría y proveedor.
- **Consulta de Categorías**: Muestra la lista de productos asociados a una categoría específica.
- **Consulta de Proveedores**: Proporciona información sobre los productos suministrados por cada proveedor.
- **Consulta de Bodegas**: Permite revisar los productos almacenados en una bodega y su capacidad.
- **Generación de Reportes de Stock**: Ofrece reportes de stock por categoría, proveedor y bodega.

## Requisitos del Sistema

- Python 3.8 o superior
- Flask (opcional, si se implementa una API REST)

## Instalación

Para instalar y configurar el proyecto en su entorno local, siga los siguientes pasos:

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/tu_usuario/gestion-inventario.git
   cd gestion-inventario
## Crear y activar un entorno virtual (opcional pero recomendado):

En Windows:
```bash
- python -m venv .venv
- .venv\Scripts\activate.

## Instalar las dependencias del proyecto:

- pip install -r requirements.txt
  pip install flask
  pip freeze > requirements.txt
  ````

  ## Ejecución del Proyecto
Para ejecutar la aplicación, sigue estos pasos:

```bash
cd src
```
Ejecuta el script principal main.py:
```bash
python main.py
```
Este comando iniciará la aplicación, permitiéndote gestionar el inventario ya sea a través de la línea de comandos o de una API REST si se ha implementado.

##
## Uso del proyecto

La aplicación permite interactuar con el sistema a través de una interfaz de línea de comandos o una API REST. Puedes realizar acciones como:

Registrar nuevos productos, categorías, proveedores y bodegas.
Actualizar y consultar el stock de productos.
Generar y revisar reportes detallados sobre el estado del inventario.
## Licencia
MIT
