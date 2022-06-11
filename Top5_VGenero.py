from http.client import RESET_CONTENT
import Conexion

list_juegos = []
list_All_Sales = []

genero = input("Top 5 Juegos más vendidos del genero: ")
Conexion.cursor.execute(
    f"""
    SELECT DISTINCT NAME FROM TIENDA WHERE GENRE = '{genero}' ORDER BY GLOBAL_SALES DESC FETCH FIRST 10 ROWS ONLY
    """
)
res = Conexion.cursor.fetchall() #el número de filas es pequeño y cabe en la memoria por eso el fetchall

while(res == []): #control excepción: ingreso genero no válido
    print("Ingresa un genero válido\n0. salir")
    genero = input("Top 5 Juegos más vendidos del genero: ")
    Conexion.cursor.execute(
        f"""
        SELECT DISTINCT NAME FROM TIENDA WHERE GENRE = '{genero}' ORDER BY GLOBAL_SALES DESC FETCH FIRST 10 ROWS ONLY
        """
    )
    res = Conexion.cursor.fetchall() #el número de filas es pequeño y cabe en la memoria por eso el fetchall0
    if genero == '0':
        exit()

#para tener los 5 juegos mas vendidos por categoria sin repetirse
for i in range(len(res)):
    if res[i][0] in list_juegos:
        continue
    elif(len(list_juegos)==5):
        break
    else:
        list_juegos.append(res[i][0]) #lista con los nombres de los juegos más vendidos por categoria sin repetirse
    
#el sig. for es para tener en cuenta TODAS las ventas del juego, incluyendo todas sus plataformas. suma todas las ventas globales del juego en sus diferentes plataformas 
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

print("\nTop 5 juegos de", genero,"con mayor ranking de ventas totales: ")
for i in range(0,5):     
    print(i+1, "-", list_juegos[i], ":", round(list_All_Sales[i], 2), "Millones de ventas")
print("\n")