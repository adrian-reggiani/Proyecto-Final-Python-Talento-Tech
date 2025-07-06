Requerimientos:

Base de datos: Crear una base de datos llamada 'inventario.db' para almacenar los datos de los productos. La tabla 'productos'
debe contener las siguientes columnas:

• 'id': Identificador único del producto (clave primaria,autoincremental).
• 'nombre': Nombre del producto (texto, no nulo).
• 'descripcion': Breve descripción del producto (texto).
• 'cantidad': Cantidad disponible del producto (entero, no nulo).
• 'precio': Precio del producto (real, no nulo).
• 'categoria': Categoría a la que pertenece el producto (texto).

La aplicacion debe permitir:

• Registrar nuevos productos. ✔
• Visualizar datos de los productos registrados. ✔
• Actualizar datos de productos, mediante su ID.
• Eliminación de productos, mediante su ID.
• Búsqueda de productos, mediante su ID. De manera opcional, se puede implementar la búsqueda por los campos nombre o categoría.
• Reporte de productos que tengan una cantidad igual o inferior a un límite especificado por el usuario o usuaria.

La interfaz del usuariio:

Implementar una interfaz de usuario básica, para interactuar con la base de datos a través de la terminal. La interfaz debe incluir un
con las opciones necesarias para acceder a cada funcionalidad descrita anteriormente.

Requisitos Tecnicos:

• El código debe estar bien estructurado, utilizando funciones para modularizar la lógica de la aplicación.
• Los comentarios deben estar presentes en el código, explicando las partes clave del mismo.