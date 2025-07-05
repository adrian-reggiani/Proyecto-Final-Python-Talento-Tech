# Proyecto integrado

# 1) Agregar Registro ( ID = autoincremet | nombre | descripcion | cantidad | precio | categoria)

# 2) Visualizar Registros

# 3) Actualizar Registros (mediante su ID)
# 4) Eliminar Registros (mediante su ID)
# 5) Busqueda de Productos
# 6) Reporte de productos con bajo stock
# 0) Salir


# Funciones

def ingresar_Producto():
    # nombre = input(' Ingresa nombre del producto: ')
    # categoria = input( ' Ingresa la categoria del producto: ')
    # precio = int(input( ' Ingresa el precio del producto:'))
    
    # print( 
    #       f'Se ha ingresado el siguiente producto:\n' 
    #       f'- Nombre del Producto: {nombre} \n'
    #       f'- Categoria del Producto: {categoria} \n'
    #       f'- Precio del Producto: {precio}\n'
    #       )
    
    # print( 'Volviendo al Menu... \n')
    return  
    

# Visualizar Menu

def menu():
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

while opcion != 5: 

    menu()
   
    opcion = int(input(' Ingrese la opcion deseada luego presione la tecla Enter: '))

    match opcion:
        case 1:
            opcion = ingresar_Producto()
       # case 2:
           # opcion = mostrar_Producto()
       # case 3:
           # opcion = buscar_Producto()
       # case 4:
           # opcion = eliminar_Producto()
        case 5:
            print ( 'Saliendo del programa...')
            