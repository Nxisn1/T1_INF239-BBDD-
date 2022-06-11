from email import header
import Conexion
import Header

#llenar la biblioteca con 10 juegos aleatorios con calificaciones aleatorias

for i in range(0,10):
    rank = Header.random.randint(1,16600)
    rating = Header.random.randint(1,5)

    Conexion.cursor.execute( #el ID es automático
            f"""
                INSERT INTO BIBLIOTECA(Rank, Name, Platform, Year, Genre, Publisher, Rating) 
                VALUES(
                    {rank}, 
                    (SELECT NAME FROM TIENDA WHERE RANK={rank}),  
                    (SELECT Platform FROM TIENDA WHERE RANK={rank}), 
                    (SELECT Year FROM TIENDA WHERE RANK={rank}), 
                    (SELECT Genre FROM TIENDA WHERE RANK={rank}), 
                    (SELECT Publisher FROM TIENDA WHERE RANK={rank}), 
                    {rating}
                    )
            """
    )

Conexion.connection.commit()