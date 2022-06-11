import Conexion

flag =  True
aux = []

cons = input("¿Ingrese plataforma?\n") 
Conexion.cursor.execute(f"""
    SELECT NAME FROM TIENDA WHERE PLATFORM = '{cons}'
    """) 
aux = Conexion.cursor.fetchall()

while(aux == []): #control excepción: plataforma válida
    print("Ingresa una plataforma válida\n0. Salir\n")
    cons = input("¿Ingrese plataforma?\n")
    Conexion.cursor.execute(f"""
        SELECT NAME FROM TIENDA WHERE PLATFORM = '{cons}' 
        """) 
    aux = Conexion.cursor.fetchall()
    if cons == '0':
        exit()

while flag: #control de que se ingrese un número válido
    num = input("¿Cuántos juegos quieres buscar?\n") 
    try:
        int(num)
        flag = False
    except ValueError:
        print("Tiene que ser un número entero")
        

Conexion.cursor.execute(
    f"""
    SELECT NAME FROM TIENDA WHERE PLATFORM='{cons}' 
    FETCH FIRST {int(num)} ROWS ONLY 
    """
)
platform_juegos = Conexion.cursor.fetchall()

print("\n",num, "juegos para", cons, ": ")
for i in range(len(platform_juegos)):
    print("- ",  platform_juegos[i][0])