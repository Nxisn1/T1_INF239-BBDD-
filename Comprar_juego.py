import Conexion

games = []
flag = True
flag1 = True

Conexion.cursor.execute(
    """
    SELECT NAME FROM BIBLIOTECA
    """
    )
res = Conexion.cursor.fetchall()
 
for i in res:
    games.append(i[0]) #para tener los juegos de la biblioteca en una lista (menos código) esto para ver si el juego ya está en biblio

while flag:
    juego = input("¿Nombre del juego que quieres comprar? \n")
    Conexion.cursor.execute(f"""
        SELECT NAME FROM TIENDA WHERE NAME = '{juego}'
        """) #este execute es para controlar la excepción de que exista el mismo juego en diferente plataforma
    aux = Conexion.cursor.fetchall()
    if(juego in games):
        print("Ese juego ya lo tienes")
        op = input("¿Quieres seguir comprando?\n 1. Si \n 2. No\n(1-2): ")
        if(op == "2"):
            exit()
    elif(len(aux)>1): #mismos juegos pero diferente consola, se caía cuando había más de uno
        cons = input("Hay más de uno, ¿Para cuál consola?\n")
        #control excepción de que ingrese mal la consola
        Conexion.cursor.execute(f"""
        SELECT PLATFORM FROM TIENDA WHERE NAME = '{juego}' AND PLATFORM = '{cons}'
        """) 
        aux_platform = Conexion.cursor.fetchall()
        if aux_platform == []:
            print("El juego no está para esa consola/consola no encontrada\n")
            op = input("¿Quieres seguir comprando?\n 1. Si \n 2. No\n(1-2): ")
            if(op == "2"):
                exit()
        else:
            while flag1: #control de excepción que el user ingrese un valor distinto al rango de 1-5
                print("Debe ser un valor entre 1 y 5")
                print("¿Valoración del juego? (1-5)")
                valoracion = input()
                if valoracion == '1' or valoracion == '2' or valoracion == '3' or valoracion == '4' or valoracion == '5':
                    flag1 = False
            flag = False  
    elif aux == []: #control excepción de que el juego no esté
        print("Juego no encontrado")
        op = input("¿Quieres seguir comprando?\n 1. Si \n 2. No\n(1-2): ")
        if(op == "2"):
            exit()
    else:
        while flag1:
                print("Debe ser un valor entre 1 y 5")
                print("¿Valoración del juego? (1-5)")
                valoracion = input()
                if valoracion == '1' or valoracion == '2' or valoracion == '3' or valoracion == '4' or valoracion == '5':
                    flag1 = False
        flag = False 

if(len(aux)>1):
    Conexion.cursor.execute(
            f"""
                INSERT INTO BIBLIOTECA(Rank, Name, Platform, Year, Genre, Publisher, Rating) 
                VALUES(
                    (SELECT Rank FROM TIENDA WHERE NAME='{juego}' AND Platform = '{cons}'), 
                    '{juego}',  
                    '{cons}', 
                    (SELECT Year FROM TIENDA WHERE NAME='{juego}' AND Platform = '{cons}'), 
                    (SELECT Genre FROM TIENDA WHERE NAME='{juego}' AND Platform = '{cons}'), 
                    (SELECT Publisher FROM TIENDA WHERE NAME='{juego}' AND Platform = '{cons}'), 
                    {valoracion}
                )
            """
        )
else:
    Conexion.cursor.execute(
            f"""
                INSERT INTO BIBLIOTECA(Rank, Name, Platform, Year, Genre, Publisher, Rating) 
                VALUES(
                    (SELECT Rank FROM TIENDA WHERE NAME='{juego}'), 
                    '{juego}',  
                    (SELECT Platform FROM TIENDA WHERE NAME='{juego}'), 
                    (SELECT Year FROM TIENDA WHERE NAME='{juego}'), 
                    (SELECT Genre FROM TIENDA WHERE NAME='{juego}'), 
                    (SELECT Publisher FROM TIENDA WHERE NAME='{juego}'), 
                    {valoracion}
                )
            """
        )

Conexion.connection.commit()