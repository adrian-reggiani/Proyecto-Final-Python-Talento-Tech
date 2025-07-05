# Proyecto integrado

# 2) Visualizar Registros

# 3) Actualizar Registros (mediante su ID)
# 4) Eliminar Registros (mediante su ID)
# 5) Busqueda de Productos
# 6) Reporte de productos con bajo stock
# 0) Salir

# Mover el create table al principio

import sqlite3
import os

db = 'data.db'



def clean():
    os.system("cls" if os.name == "nt" else "clear")
    
def pause():
    input("Presiona Enter para continuar... \n")


# Funciones

# Agregar Producto ----------------------------------------------------------------------------------------------
def agregar_producto():
    try: 
        # Conexion
        conexion = sqlite3.connect(db)
        cursor = conexion.cursor()
        
        # Creacion de tabla por si no existe
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS productos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        descripcion TEXT,
                        cantidad INTEGER NOT NULL,
                        precio INTEGER NOT NULL,
                        categoria TEXT NOT NULL
                        );
                    ''')
        # Datos Almacenados
        nombre = input(' Ingresa nombre del producto: ')
        descripcion = input(' Ingrese descripcion del producto (Opcional): ')
        try:
            cantidad = int(input( ' Ingresa la cantidad del producto: '))
            precio = int(input( ' Ingresa el precio del producto: '))
        except Exception as e:
            print ('Error en el ingreso de datos', e)
        categoria = input( ' Ingresa la categoria del producto: ')
        
        # Ingreso de Datos
        cursor.execute('''
                    INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
                    VALUES (? , ? , ? ,? ,?) ''', 
                    (nombre, descripcion, cantidad, precio, categoria)
                    )
        
        # Guardar y Cerrar
        conexion.commit()
        print('\n Se ingresaro el producto correctamente \n')
           
    except Exception as e:
        print(' Error al agregar producto: ', e)
        
        
    finally:
        conexion.close()
        pause()
        print( 'Volviendo al Menu... \n')
        return  0
# Agregar Producto ----------------------------------------------------------------------------------------------        
        
        
# Visualizar Menu

def menu():
    clean()
    print ('----------------------------------------------------------------------------------------------')
    print ( '1) Agregar Registro' )
    print ( '2) Actualizar Registros' )
    print ( '3) Eliminar Registros' )
    print ( '4) Busqueda de Productos' )
    print ( '5) Busqueda de Productos' )
    print ( '6) Reporte de productos con bajo stock' )
    print ( '0) Salir' )
    print ('----------------------------------------------------------------------------------------------')
    
    
    
# Programa
opcion = ''

while opcion != 10: 

    menu()
   
    opcion = int(input(' Ingrese la opcion deseada luego presione la tecla Enter: '))

    match opcion:
        case 1:
            opcion = agregar_producto()
       # case 2:
           # opcion = mostrar_Producto()
       # case 3:
           # opcion = buscar_Producto()
       # case 4:
           # opcion = eliminar_Producto()
       # case 5:
           # opcion = buscar_Producto()
       # case 6:
           # opcion = eliminar_Producto()
        case 0:
            print ( 'Saliendo del programa...')
            break
            