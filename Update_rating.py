import Conexion

game = input("Ingresa el nombre de un juego de tu biblioteca\n")
flag = True
flag1 = True

Conexion.cursor.execute(
    f"""
    SELECT NAME FROM BIBLIOTECA WHERE NAME = '{game}'
    """
)
aux = Conexion.cursor.fetchall()

while(aux == []): #control excepción: ingresa juego que no tiene
    print("No tienes este juego\n0. salir")
    game = input("Ingresa un nombre válido de un juego de tu biblioteca\n")
    Conexion.cursor.execute(
        f"""
        SELECT NAME FROM BIBLIOTECA WHERE NAME = '{game}'
        """
    )
    aux = Conexion.cursor.fetchall()
    if game == '0':
        exit()

Conexion.cursor.execute(
    f"""
    SELECT RATING FROM BIBLIOTECA WHERE NAME='{game}'
    """
)
rat = Conexion.cursor.fetchall()

print("El rating que le pusiste a", game, "es ", rat[0][0])

aux = input("¿Quieres cambiar su puntuación?\n1.Si\n2.No\n(1-2): ")
while flag:
    if aux == '1':
        print("Ingresa una nueva calificación para", game, "(1-5)")
        new_rat = input()
        while flag1: #control excepción ingresa otro valor 
                    print("Debe ser un valor entre 1 y 5")
                    print("¿Valoración del juego? (1-5)")
                    new_rat = input()
                    if new_rat == '1' or new_rat == '2' or new_rat == '3' or new_rat == '4' or new_rat == '5':
                        flag1 = False
        Conexion.cursor.execute(
        f"""
        UPDATE BIBLIOTECA SET RATING={new_rat} WHERE NAME='{game}'
        """
        )
        flag = False
    elif aux == '2':
        exit()
    else:
        print("Ingresa una opción válida")
        aux = input("¿Quieres cambiar su puntuación?\n1.Si\n2.No\n(1-2): ")

Conexion.connection.commit()