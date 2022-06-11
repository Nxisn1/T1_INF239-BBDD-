from asyncio.windows_events import NULL
import Header
import Conexion

juegos_data = Header.pd.read_csv('juegos.csv')

insert_juego = """
        INSERT INTO TIENDA(Rank, Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales) 
        VALUES(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11)
        """
#llenar la tabla JUEGOS con los datos de csv
for i, row in juegos_data.iterrows():
        if(str(tuple(row)[3]) == "nan"): #control excepción year = N/A porque tiraba error
            row[3] = NULL
        if(str(tuple(row)[5]) == "nan"): #control excepción publisher = N/A
            row[5] = NULL
        Conexion.cursor.execute(insert_juego, tuple(row))
        Conexion.connection.commit()