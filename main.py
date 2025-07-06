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

# Verificar tabla creada

def verificar_tabla():
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

def registrar_producto():
    try: 
        # Conexion
        conexion = sqlite3.connect(db)
        cursor = conexion.cursor()
        
        # Datos Almacenados
        nombre = input(' Ingresa nombre del producto: ')
        descripcion = input(' Ingrese descripcion del producto (Opcional): ')
        
        try: # Este try es por si ingresan un dato no entero
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
        print('Se ingresaro el producto correctamente \n')
           
    except Exception as e:
        print(' Error al agregar producto: ', e)
        
        
    finally:
        conexion.close()
        print('\n')
        pause()
        print( 'Volviendo al Menu... \n')
        return  0    
        
def mostrar_Producto():
    try: 
        # Conexion
        conexion = sqlite3.connect(db)
        cursor = conexion.cursor()
        
        # Mostrar producto
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        
        print ( "id |    nombre      |  descripcion    |    precio    |     categoria      |")
        print( '-' * 75)
        for id, nombre, descripcion, cantidad, precio, categoria  in productos:
            print ( f"{id:^3}|{nombre:^16}|{descripcion:^17}|{precio:^14}|{categoria:^20}|") 
            # el :>3 al lado de la variable determina la alineacion del texto y los espacios
    except Exception as e:
        print(' Hay un problema en la DB')
        
    finally:
        conexion.close()
        print('\n')
        pause()
        print( ' \n Volviendo al Menu... \n')
        return  0   
            

        
# Visualizar Menu

def menu():
    clean()
    print ('----------------------------------------------------------------------------------------------')
    print ( '1) Registrar nuevo producto' )
    print ( '2) Visualizar productos registrados')
    print ( '3) Actualizar producto' )
    print ( '4) Eliminar producto' )
    print ( '5) Busqueda de Producto' )
    print ( '6) Reporte de productos con bajo stock' )
    print ( '0) Salir' )
    print ('----------------------------------------------------------------------------------------------')
    
    
    
# Programa
opcion = ''
verificar_tabla()

while opcion != 10: 

    menu()
    opcion = int(input(' Ingrese la opcion deseada luego presione la tecla Enter: '))

    match opcion:
        case 1:
            opcion = registrar_producto()
        case 2:
           opcion = mostrar_Producto()
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
            