import Conexion

Conexion.cursor.execute(
    """
    SELECT * FROM POKEMONES
    """
)
pokimones = Conexion.cursor.fetchall()
print("\nJuegos de Pokemon disponibles: ")
for i in pokimones:
    print("-", i[0])