# Se importa modulo SQL
import sqlite3

# Archivo BD
db = 'data.db'

# Funciones

def verificar_tabla():
    # Conexion a la base de datos
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

def registrar_producto(pause):
    print(' Acontinuacion se le solicitara datos del nuevo producto...')
    
    try: 
        # Conexion a la base de datos
        conexion = sqlite3.connect(db)
        cursor = conexion.cursor()
        
        # Ingreso de datos del producto
        nombre = input(' Ingresa nombre del producto: ')
        descripcion = input(' Ingrese descripcion del producto (Opcional): ')
        
        try:
            cantidad = int(input( ' Ingresa la cantidad del producto: '))
            precio = int(input( ' Ingresa el precio del producto: '))
        except Exception as e:
            print ('Error en el ingreso de datos, tiene que ser un numero entero... ', e)
            return 0
            
        categoria = input( ' Ingresa la categoria del producto: ')
        
        # Insercion de datos en la tabla
        cursor.execute('''
                    INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
                    VALUES (? , ? , ? ,? ,?) ''', 
                    (nombre, descripcion, cantidad, precio, categoria)
                    )
        
        # Confirmar cambios
        conexion.commit()
        print('Se ingresaro el producto correctamente \n')
           
    except Exception as e:
        print(' Error al agregar producto: ', e)
        
        
    finally:
        # Cierre de conexion y volviendo al menu
        conexion.close()
        print('\n')
        print( 'Volviendo al Menu... \n')
        pause()
        return  0    
        
def mostrar_producto(pause):
    try: 
        # Conexion a la base de datos
        conexion = sqlite3.connect(db)
        cursor = conexion.cursor()
        
        # Mostrar producto de la base de datos
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        
        # Impresion de los productos
        if (productos):
            print(' Se visualiza los siguientes productos: \n')
            print ( "id |    nombre      |  descripcion    |  cantidad   |    precio    |     categoria      |")
            print( '-' * 75)
            for id, nombre, descripcion, cantidad, precio, categoria  in productos:
                print ( f"{id:^3}|{nombre:^16}|{descripcion:^17}|{cantidad:^13}|{precio:^14}|{categoria:^20}|") 
        else: 
            print(' No hay productos para visualizar....')
        
    except Exception as e:
        print(' Hay un problema en la DB')
        
    finally:
        # Cierre de conexion y retorno al menu
        conexion.close()
        print('\n')
        print( ' \n Volviendo al Menu... \n')
        pause()
        return  0   
    
def actualizar_producto(pause) :
    print(' Es necesario conocer el ID del producto para actualizar. Puede obtenerlo a traves de la opcion 2) Visualizar productos registrados')
    print(' Ingresando ID = 0, podra volver al menu \n')
    
    # Diccionario con los datos que se actualizaran
    datos_actualizados = {}
    
    try:
        datos_actualizados['id'] = int(input( ' Ingrese el ID del producto: '))
    except Exception as e:
        print('Se ingreso un dato que no es numerico. Se vuelve al menu....')
        pause()
        return 0       
        
    # Opcion para que usuario vuelva al menu si desconoce la ID
    if (datos_actualizados['id'] == 0):
        print( '\n Volviendo al Menu... \n')
        pause()
        return  0 
        
    
    # Funcion para validar la opcion del usuario
    def validar_opcion(campo):
        while True :
            opcion = input( f' Desea actualizar {campo} del producto? (S/N): ').strip().lower()
            if (opcion == 's'):
                return 's'
            elif (opcion == 'n'):
                return 'n'
            else:
                print( 'Se ingreso un valor erroneo')
                
    # Ingreso de datos para actualizar con validador de opciones           
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
    
    # Visualizacion de los datos ingresados
    print('\nEstos son los datos que se actualizarán:\n')
    print("id |    nombre      |  descripcion    |  cantidad   |    precio    |     categoria      |")
    print('-' * 75)
    print(f"{datos_actualizados.get('id', ''):^3}|"
            f"{datos_actualizados.get('nombre', ''):^16}|"
            f"{datos_actualizados.get('descripcion', ''):^17}|"
            f"{str(datos_actualizados.get('cantidad', '')):^13}|"
            f"{str(datos_actualizados.get('precio', '')):^14}|"
            f"{datos_actualizados.get('categoria', ''):^20}|")
    
    # Consulta al usuario para continuar con la actualizacion
    actualizar = input('Deseas actualizar los datos (S/N): ')
    if (actualizar == 's'):
        print('Actualizando productos....')
        try: 
            # Conexion a la base de datos
            conexion = sqlite3.connect(db)
            cursor = conexion.cursor()
            
            # Separo el id para preparar el SET
            id_producto = datos_actualizados.pop('id')
            
            # Despues de "clave = ?" se agrega una ,
            claves =  ", ".join([f"{clave} = ?" for clave in datos_actualizados])
            
            # Almacena los valores y por ultimo el ID para el WHERE
            valores = list(datos_actualizados.values())
            valores.append(id_producto)
            
            # Se actualizan los productos
            cursor.execute(f"UPDATE productos SET {claves} WHERE id = ?", valores)
            
            # Confirmamos cambios 
            conexion.commit()
            
            
        except Exception as e:
            print(' Hay un problema en la consulta que actualiza los productos')
        
        finally:
            # Cerramos conexion y volvemos al menu
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
          
def eliminar_producto(pause):
    print(' Es necesario conocer el ID del producto para eliminarlo. Puede obtenerlo a traves de la opcion 2) Visualizar productos registrados')
    print(' Ingresando ID = 0, podra volver al menu \n')
    
    # Conexion a la base de datos
    conexion = sqlite3.connect(db)
    cursor = conexion.cursor()
    
    try:
        # Solicitud de ID
        id_producto = int(input('Ingrese el ID del producto: \n')) 
        
        # Opcion para que usuario vuelva al menu si desconoce la ID
        if (id_producto == 0):
            return  0 
    
        # Consulta para traer productos segun ID
        cursor.execute('SELECT * FROM productos WHERE id = ?', (id_producto,))
        producto = cursor.fetchone()
        
        # Visualizar de datos
        if producto:
           id, nombre, descripcion, cantidad, precio, categoria = producto
           print('\n')
           print("id |    nombre      |  descripcion    |  cantidad   |    precio    |     categoria      |")
           print ( f"{id:^3}|{nombre:^16}|{descripcion:^17}|{cantidad:^13}|{precio:^14}|{categoria:^20}|\n") 
           
        else:
         print("\n Producto no encontrado...")
         return  0 
        
        # Se da la opcion de eliminar o volver al menu
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
        # Cierre de conexion y volviendo al menu
        conexion.close()
        print('\n')
        print( 'Volviendo al Menu... \n')
        pause()
        return  0 
             
def buscar_producto(pause):
    print(' Es necesario conocer el ID del producto para visualizarlo. Puede obtenerlo a traves de la opcion 2) Visualizar productos registrados')
    print(' Ingresando ID = 0, podra volver al menu \n')
    
    # Conexion a la base de datos
    conexion = sqlite3.connect(db)
    cursor = conexion.cursor()
    
    try:
        # Solicitud de ID
        id_producto = int(input(' Ingrese el ID del producto: ')) 
        
        #  Opcion para que usuario vuelva al menu si desconoce la ID
        if (id_producto == 0):
            return  0 
        
        # Consulta para traer productos segun ID
        cursor.execute('SELECT * FROM productos WHERE id = ?', (id_producto,))
        producto = cursor.fetchone()
        
        # Visualizar de datos
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
        # Cierre de conexion y volviendo al menu
        conexion.close()
        print('\n')
        print( 'Volviendo al Menu... \n')
        pause()
        return  0 
 
def reporte_producto(pause): 
    # Conexion a la base de datos
    conexion = sqlite3.connect(db)
    cursor = conexion.cursor()
    
    print(' Se realizara un reporte de producto con respecto a las cantidades de los items. El reporte sera de cantidades iguales o menores al numero ingresado \n')
    cantidad = int(input('Ingresar el numero de la cantidades deseadas: \n'))
    
    try:
        # Consulta para traer productos segun cantidad
        cursor.execute('SELECT * FROM productos WHERE cantidad <= ? ORDER BY  cantidad DESC', (cantidad,))
        productos = cursor.fetchall()
        
        # Visualiza datos que son mayores a 1
        if (len(productos) > 1):
            print('\n')
            print ( "id |    nombre      |  descripcion    |  cantidad   |    precio    |     categoria      |")
            for id, nombre, descripcion, cantidad, precio, categoria  in productos:
                print ( f"{id:^3}|{nombre:^16}|{descripcion:^17}|{cantidad:^13}|{precio:^14}|{categoria:^20}|")
        
        # Visualiza un dato        
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
        # Cierre de conexion y volviendo al menu
        conexion.close()
        print('\n')
        print( ' \n Volviendo al Menu... \n')
        pause()
        return  0 
        
        
