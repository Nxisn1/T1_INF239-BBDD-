from http.client import RESET_CONTENT
import Conexion

#para tener los nombres de los 5 juegos más vendidos
Conexion.cursor.execute(
    """
    SELECT NAME FROM TIENDA ORDER BY GLOBAL_SALES DESC 
    FETCH FIRST 5 ROWS ONLY 
    """
)
res = Conexion.cursor.fetchall() #el número de filas es pequeño y cabe en la memoria por eso el fetchall

list_juegos = [res[0][0], res[1][0], res[2][0], res[3][0], res[4][0]] #lista con los nombres de los juegos más vendidos
list_All_Sales = [] #lista que tendrá las ventas totales

#el sig. for es para tener en cuenta TODAS las ventas del juego, incluyendo todas sus plataformas. Suma todas las ventas globales del juego en sus diferentes plataformas 
for i in list_juegos:
    sales = 0
    Conexion.cursor.execute(
        f"""
        SELECT GLOBAL_SALES FROM TIENDA WHERE NAME = '{i}'
        """
    )
    aux = Conexion.cursor.fetchall()
    for j in range(len(aux)):
        sales += aux[j][0]
    list_All_Sales.append(sales)

print("\nTop 5 juegos con mayor ranking de ventas totales: ")
for i in range(0,5):     
    print(i+1, "-", list_juegos[i], ":", list_All_Sales[i], "Millones de ventas")
print("\n")