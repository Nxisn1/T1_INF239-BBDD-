import Header
import Conexion

flag = True

while flag:
    print("MENU: ")
    print("1. Mostrar bibllioteca")
    print("2. Comprar Juego")
    print("3. Mostrar Top 5 Juegos más vendidos")
    print("4. Mostrar Top 5 Juegos más vendidos por categoria")
    print("5. Borrar Juego")
    print("6. Actualizar Calificación")
    print("7. Buscar Juego")
    print("8. Buscar juegos según plataforma")
    print("9. Borrar toda la biblioteca")
    print("10. Juegos de Pokemon")
    print("11. Salir")

    opcion = input("Elige una opción: ") 

    if opcion == '1':
        Header.os.system('Show_biblio.py')
        print("\n")
        
    elif opcion == '2':
        Header.os.system('Comprar_juego.py')
        print("\n")

    elif opcion == '3':
        Header.os.system('Top_5_VT.py')
        print("\n")
    
    elif opcion == '4':
        Header.os.system('Top5_VGenero.py')
        print("\n")
    
    elif opcion == '5':
        Header.os.system('Delete.py')
        print("\n")

    elif opcion == '6':
        Header.os.system('Update_rating.py')
        print("\n")
    
    elif opcion == '7':
        Header.os.system('Buscar_juego.py')
        print("\n")
    
    elif opcion == '8':
        Header.os.system('Platform_juegos.py')
        print("\n")

    elif opcion == '9':
        Header.os.system('Delete_all_biblio.py')
        print("\n")

    elif opcion == '10':
        Header.os.system('View_View.py')
        print("\n")

    elif opcion == '11':
        flag = False
    
    else:
        print("Ingresa una opción válida")

Conexion.connection.close()