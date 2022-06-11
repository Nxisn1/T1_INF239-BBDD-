import Conexion

Conexion.cursor.execute(
    """
    CREATE OR REPLACE VIEW POKEMONES AS
    SELECT NAME FROM TIENDA WHERE NAME LIKE '%Pokemon%' 
    """
)

Conexion.connection.commit()