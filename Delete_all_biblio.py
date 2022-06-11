import Conexion

flag = True

choice = input("¿Seguro que quieres borrar todo de tu biblioteca de forma permanente?\n1.Si\n2.No\n(1-2): ")
while flag:
    if choice == '1':
        print("1")
        Conexion.cursor.execute(
            """
            TRUNCATE TABLE BIBLIOTECA
            """
        )
        Conexion.connection.commit()
        print("Todos los juegos de tu biblioteca han sido borrados\n")
        flag = False
    elif choice == '2':
        exit()
    else:
        print("\nElige una opción válida")
        choice = input("\n1.Si\n2.No\n(1-2): ")

