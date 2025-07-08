import sqlite3
import os

db = 'data.db'

def clean():
    os.system("cls" if os.name == "nt" else "clear")
    
def pause():
    input("Presiona Enter para continuar... \n")
    


# Funciones

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
    print(' Acontinuacion se le solicitara datos del nuevo producto...')
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
        print( 'Volviendo al Menu... \n')
        pause()
        return  0    
        
def mostrar_producto():
    try: 
        # Conexion
        conexion = sqlite3.connect(db)
        cursor = conexion.cursor()
        
        # Mostrar producto
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        
        if (productos):
            print(' Se visualiza los siguientes productos: \n')
            print ( "id |    nombre      |  descripcion    |  cantidad   |    precio    |     categoria      |")
            print( '-' * 75)
            for id, nombre, descripcion, cantidad, precio, categoria  in productos:
                print ( f"{id:^3}|{nombre:^16}|{descripcion:^17}|{cantidad:^13}|{precio:^14}|{categoria:^20}|") 
            # el :>3 al lado de la variable determina la alineacion del texto y los espacios
        else: 
            print(' No hay productos para visualizar....')
        
    except Exception as e:
        print(' Hay un problema en la DB')
        
    finally:
        conexion.close()
        print('\n')
        print( ' \n Volviendo al Menu... \n')
        pause()
        return  0   
    
def actualizar_producto() :
    print(' Es necesario conocer el ID del producto para actualizar. Puede obtenerlo a traves de la opcion 2) Visualizar productos registrados')
    print(' Ingresando ID = 0, podra volver al menu \n')
    datos_actualizados = {}
    
    datos_actualizados['id'] = int(input( ' Ingrese el ID del producto: '))
    
    if (datos_actualizados['id'] == 0):
        print( '\n Volviendo al Menu... \n')
        pause()
        return  0 
    
    def validar_opcion(campo):
        
        while True :
            opcion = input( f' Desea actualizar {campo} del producto? (S/N): ').strip().lower()
            if (opcion == 's'):
                return 's'
            elif (opcion == 'n'):
                return 'n'
            else:
                print( 'Se ingreso un valor erroneo')
           
    opcion = validar_opcion('nombre')
    if(opcion == 's'):
       datos_actualizados['nombre'] = input(' Ingrese nuevo nombre del producto: ')
       print('\n')
        
    opcion = validar_opcion('descripcion')
    if(opcion == 's'):
        datos_actualizados['descripcion'] = input(' Ingrese nueva descripcion del producto: ')
        print('\n')
        
    opcion = validar_opcion('cantidad')
    if(opcion == 's'):
        try: 
            cantidad = int(input(' Ingrese nueva cantidad del producto (Entero y positvo): '))
            datos_actualizados['cantidad'] = cantidad
            print('\n')
        except Exception as e:
            print(f'No es un numero entero o no es positivo. {cantidad}')
        
    opcion = validar_opcion('precio')
    if(opcion == 's'):
        try: 
            precio = int(input(' Ingrese nueva cantidad del producto (Entero y positvo): '))
            datos_actualizados['precio'] = precio
            print('\n')
        except Exception as e:
            print(f'No es un numero entero o no es positivo. {precio}')
        
    opcion = validar_opcion('categoria')
    if(opcion == 's'):
        datos_actualizados['categoria'] = input(' Ingrese nueva categoria del producto: ')
        print('\n')
    
    print('\nEstos son los datos que se actualizarán:\n')
    print("id |    nombre      |  descripcion    |  cantidad   |    precio    |     categoria      |")
    print('-' * 75)
    print(f"{datos_actualizados.get('id', ''):^3}|"
            f"{datos_actualizados.get('nombre', ''):^16}|"
            f"{datos_actualizados.get('descripcion', ''):^17}|"
            f"{str(datos_actualizados.get('cantidad', '')):^13}|"
            f"{str(datos_actualizados.get('precio', '')):^14}|"
            f"{datos_actualizados.get('categoria', ''):^20}|")
    
    actualizar = input('Deseas actualizar los datos (S/N): ')
    if (actualizar == 's'):
        print('Actualizando productos....')
        try: 
            # Conexion
            conexion = sqlite3.connect(db)
            cursor = conexion.cursor()
            
            # Separo el id para el SET
            id_producto = datos_actualizados.pop('id')
            
            # Separo las clave para el SET
            claves =  ", ".join([f"{clave} = ?" for clave in datos_actualizados])
            
            # Guardo los valores con el ID
            valores = list(datos_actualizados.values())
            valores.append(id_producto)
            
            # Mostrar producto
            cursor.execute(f"UPDATE productos SET {claves} WHERE id = ?", valores)
            
            # Guardamos 
            conexion.commit()
            
            
        except Exception as e:
            print(' Hay un problema en la consulta que actualiza los productos')
        
        finally:
            conexion.close()
            print('\n')
            print( ' \n Volviendo al Menu... \n')
            pause()
            return  0   
            
        
    elif (actualizar == 'n'):
        print('Volviendo al menu...\n')
        pause()
        return 0
    
    else:
        print( 'Se ingreso un valor erroneo. Volviendo al menu... \n')
        pause()
        return 0
          
def eliminar_producto():
    print(' Es necesario conocer el ID del producto para eliminarlo. Puede obtenerlo a traves de la opcion 2) Visualizar productos registrados')
    print(' Ingresando ID = 0, podra volver al menu \n')
    # Conexion
    conexion = sqlite3.connect(db)
    cursor = conexion.cursor()
    
    try:
        id_producto = int(input('Ingrese el ID del producto: \n')) 
        
        if (id_producto == 0):
            return  0 
    
        cursor.execute('SELECT * FROM productos WHERE id = ?', (id_producto,))
        producto = cursor.fetchone()
        
        if producto:
           id, nombre, descripcion, cantidad, precio, categoria = producto
           print('\n')
           print("id |    nombre      |  descripcion    |  cantidad   |    precio    |     categoria      |")
           print ( f"{id:^3}|{nombre:^16}|{descripcion:^17}|{cantidad:^13}|{precio:^14}|{categoria:^20}|\n") 
           
        else:
         print("\n Producto no encontrado...")
         return  0 
         
        opcion = input( f' Desea elimnar el producto? (S/N): ').strip().lower()
        
        if (opcion == 's'):
            cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
            conexion.commit()
            print('\n Se elimino producto')
        elif (opcion == 'n'):
            print(' No se elimino producto')
            
        else:
            print( 'Se ingreso un valor erroneo')
        
        
    except Exception as e:
        print(' Error con la consulta: ', e)
    
    finally:
        conexion.close()
        print('\n')
        print( 'Volviendo al Menu... \n')
        pause()
        return  0 
             
def buscar_producto():
    print(' Es necesario conocer el ID del producto para visualizarlo. Puede obtenerlo a traves de la opcion 2) Visualizar productos registrados')
    print(' Ingresando ID = 0, podra volver al menu \n')
    
    # Conexion
    conexion = sqlite3.connect(db)
    cursor = conexion.cursor()
    
    try:
        id_producto = int(input(' Ingrese el ID del producto: ')) 
        
        if (id_producto == 0):
            return  0 
        
        cursor.execute('SELECT * FROM productos WHERE id = ?', (id_producto,))
        producto = cursor.fetchone()
        
        
        print(producto)
        
        if producto:
           id, nombre, descripcion, cantidad, precio, categoria = producto
           print('\n')
           print("id |    nombre      |  descripcion    |  cantidad   |    precio    |     categoria      |")
           print ( f"{id:^3}|{nombre:^16}|{descripcion:^17}|{cantidad:^13}|{precio:^14}|{categoria:^20}|\n") 
        else:
         print("Producto no encontrado.")
        
    except Exception as e:
        print(' Error con la consulta: ', e)
        
    finally:
        conexion.close()
        print('\n')
        print( 'Volviendo al Menu... \n')
        pause()
        return  0 
 
def reporte_producto(): 
    # Conexion
    conexion = sqlite3.connect(db)
    cursor = conexion.cursor()
    
    print(' Se realizara un reporte de producto con respecto a las cantidades de los items. El reporte sera de cantidades iguales o menores al numero ingresado \n')
    cantidad = int(input('Ingresar el numero de la cantidades deseadas: \n'))
    
    try:
        cursor.execute('SELECT * FROM productos WHERE cantidad <= ? ORDER BY  cantidad DESC', (cantidad,))
        productos = cursor.fetchall()
        
        
        if (len(productos) > 1):
            print('\n')
            print ( "id |    nombre      |  descripcion    |  cantidad   |    precio    |     categoria      |")
            for id, nombre, descripcion, cantidad, precio, categoria  in productos:
                print ( f"{id:^3}|{nombre:^16}|{descripcion:^17}|{cantidad:^13}|{precio:^14}|{categoria:^20}|")
                
        elif (len(productos) == 1): 
            producto = productos[0]
            id, nombre, descripcion, cantidad, precio, categoria = producto
            print('\n')
            print("id |    nombre      |  descripcion    |  cantidad   |    precio    |     categoria      |")
            print ( f"{id:^3}|{nombre:^16}|{descripcion:^17}|{cantidad:^13}|{precio:^14}|{categoria:^20}|\n") 
            
        else:
            print(' Error numero ingresado...')
            
    except Exception as e:
        print('Hubo un error: ', e)
        
    finally:
        conexion.close()
        print('\n')
        print( ' \n Volviendo al Menu... \n')
        pause()
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
            opcion = mostrar_producto()
        case 3:
            opcion = actualizar_producto()
        case 4:
           opcion = eliminar_producto()
        case 5:
           opcion = buscar_producto()
        case 6:
           opcion = reporte_producto()
        case 0:
            print ( 'Saliendo del programa...')
            break
            