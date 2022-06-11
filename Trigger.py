import Conexion

Conexion.cursor.execute(
    """
    CREATE OR REPLACE TRIGGER CONTROL 
    AFTER INSERT OR DELETE OR UPDATE ON TIENDA 
    BEGIN
        ROLLBACK TRANSACTION;
    END;

    """
)

Conexion.connection.commit()


