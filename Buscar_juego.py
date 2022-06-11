import Conexion

flag_table =  True
flag_biblio = True
aux = []
games = []
#para tener los juegos de la biblioteca
Conexion.cursor.execute(
    """
    SELECT NAME FROM BIBLIOTECA
    """
    )
res = Conexion.cursor.fetchall()
 
for i in res:
    games.append(i[0])


while flag_table: #control excepción: ingreso válido de tabla 
    table = input("¿Dónde quieres buscar el juego?\n1. Tienda\n2. Biblioteca\n3. Salir\n(1,2,3): ")
    if(table == '1'):
        table = 'Tienda'
        flag_table = False
    elif(table == '2'):
        table = 'Biblioteca'
        flag_table = False
    elif(table == '3'):
        exit()

if table == 'Tienda':
    name = input("¿Nombre del juego que quieres buscar? \n") 
    Conexion.cursor.execute(f"""
        SELECT NAME FROM TIENDA WHERE NAME = '{name}' 
        """) 
    aux = Conexion.cursor.fetchall()
    while(aux == []): #control excepción: juego válido
        print("Ingresa el nombre de un juego válido\n0. Salir\n")
        name = input("¿Nombre del juego que quieres buscar? \n")
        Conexion.cursor.execute(f"""
            SELECT NAME FROM TIENDA WHERE NAME = '{name}' 
            """) 
        aux = Conexion.cursor.fetchall()
        if name == '0':
            exit()

    if(len(aux)>1):
        consola = input("El juego está en diferentes plataformas\n¿Para cuál plataforma? \n")
        Conexion.cursor.execute(
        f"""
        SELECT * FROM {table} WHERE NAME='{name}' AND PLATFORM = '{consola}'
        """
        )
        info = Conexion.cursor.fetchall()
        while(info == []): #control excepción consola válida
            print("No se ha encontrado el juego en esa plataforma\n0. Salir\n")
            consola = input("¿Para cuál plataforma?\n")
            Conexion.cursor.execute(
            f"""
            SELECT * FROM {table} WHERE NAME='{name}' AND PLATFORM = '{consola}'
            """
            )
            info = Conexion.cursor.fetchall()
            if consola == '0':
                exit()
        
        print("Rank:", info[0][0])
        print("Nombre:", info[0][1])
        print("Plataforma:", info[0][2])
        print("Año:", info[0][3])
        print("Genero:", info[0][4])
        print("Publisher:", info[0][5])
        print("NA_SALES:", info[0][6], "Millones")
        print("EU_SALES:", info[0][7], "Millones")
        print("JP_SALES:", info[0][8], "Millones")
        print("OTHER_SALES:", info[0][9], "Millones")
        print("GLOBAL_SALES:", info[0][10], "Millones")

    else:
        Conexion.cursor.execute(
        f"""
        SELECT * FROM {table} WHERE NAME='{name}'
        """
        )
        info = Conexion.cursor.fetchall()


        print("Rank:", info[0][0])
        print("Nombre:", info[0][1])
        print("Plataforma:", info[0][2])
        print("Año:", info[0][3])
        print("Genero:", info[0][4])
        print("Publisher:", info[0][5])
        print("NA_SALES:", info[0][6], "Millones")
        print("EU_SALES:", info[0][7], "Millones")
        print("JP_SALES:", info[0][8], "Millones")
        print("OTHER_SALES:", info[0][9], "Millones")
        print("GLOBAL_SALES:", info[0][10], "Millones")
else: #table = Biblioteca
    name = input("¿Nombre del juego que quieres buscar? \n") 
    Conexion.cursor.execute(f"""
        SELECT NAME FROM BIBLIOTECA WHERE NAME = '{name}' 
        """) 
    aux = Conexion.cursor.fetchall()
    while(aux == []): #control excepción: juego válido
        print("No tienes este juego\n0. Salir\n")
        name = input("¿Nombre del juego que quieres buscar? \n")
        Conexion.cursor.execute(f"""
            SELECT NAME FROM BIBLIOTECA WHERE NAME = '{name}' 
            """) 
        aux = Conexion.cursor.fetchall()
        if name == '0':
            exit()
    Conexion.cursor.execute(
    f"""
    SELECT * FROM {table} WHERE NAME='{name}'
    """
    )
    info = Conexion.cursor.fetchall()

    print("ID:", info[0][0])
    print("Rank:", info[0][1])
    print("Nombre:", info[0][2])
    print("Plataforma:", info[0][3])
    print("Año:", info[0][4])
    print("Genero:", info[0][5])
    print("Publisher:", info[0][6])
    print("Rating:", info[0][7])
            
