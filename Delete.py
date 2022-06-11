import Conexion

d_game = input("¿Qué juego quieres borrar?\n")
Conexion.cursor.execute(
    f"""
    SELECT NAME FROM BIBLIOTECA WHERE NAME = '{d_game}'
    """
)
aux = Conexion.cursor.fetchall()

while(aux == []): #control excepción: borrar juego que no tiene
    print("No tienes este juego\n0. salir")
    d_game = input("¿Qué juego quieres borrar?\n")
    Conexion.cursor.execute(
        f"""
        SELECT NAME FROM BIBLIOTECA WHERE NAME = '{d_game}'
        """
    )
    aux = Conexion.cursor.fetchall()
    if d_game == '0':
        exit()

Conexion.cursor.execute(
    f"""
    DELETE FROM BIBLIOTECA WHERE NAME = '{d_game}'
    """
)

Conexion.connection.commit()