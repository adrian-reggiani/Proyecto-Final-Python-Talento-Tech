
import os
import mod_backend as be
import mod_frontend as fe
    
os.chdir(os.path.dirname(__file__))

def clean():
    os.system("cls" if os.name == "nt" else "clear")
    
def pause():
    input("Presiona Enter para continuar... \n")
    
def main():
    
    # Se inicia la variable opcion para el while
    opcion = ''
    
    # Verifica si la tabla productos existe sino la crea
    be.verificar_tabla()
    
    while opcion != 10: 

        fe.menu(clean)
        try:
            opcion = int(input(' Ingrese la opcion deseada luego presione la tecla Enter: '))
        except ValueError:
            print('Opcion invalida... Vuelva a ingresarlo')
            pause()
            continue

        match opcion:
            case 1:
                opcion = be.registrar_producto(pause)
            case 2:
                opcion = be.mostrar_producto(pause)
            case 3:
                opcion = be.actualizar_producto(pause)
            case 4:
                opcion = be.eliminar_producto(pause)
            case 5:
                opcion = be.buscar_producto(pause)
            case 6:
                opcion = be.reporte_producto(pause)
            case 0:
                print ( 'Saliendo del programa...')
                break
            case _:
                print("Opcion invalida. Ingrese alguna de las opciones detalladas \n")
                pause()
            
if __name__ == "__main__":
    main()