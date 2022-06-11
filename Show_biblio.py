import Conexion

Conexion.cursor.execute(
    """
    SELECT NAME FROM BIBLIOTECA
    """
)

res = Conexion.cursor.fetchall()
print("\nTus juego son:")
for i in res:
    print("-", i[0])