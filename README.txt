Version: ORACLE 18c XE

El csv con los datos de los juegos, 'juegos.csv', debe estar en el mismo directorio que los códigos


Librerías necesarias:
	- 'cx_Oracle' para hacer la conexción, instalación -> 'pip install cx_Oracle' en consola de Windows
	- 'pandas' para importar la información del csv, instalación -> 'pip install pandas' en consola de Windows

Conexión: 
	Se debe modificar el archivo 'Conexion.py' con sus credenciales de su base de datos en el campo 'connection = Header.cx.Oracle.connect("name", "pass", dns_tns)'. 
	La conexión esta hecho con la version  de Oracle 18c Express Edition, por lo que si se ocupa otra versión que no sea XE, se debe modificar el tercer parámetro del comando cx_Oracle.makedsn del script 'Conexion.py' por 'orcl'.
Ejecución:
	Primero ejecutar el archivo 'FakeMake.py' este crea dos tablas, 'Tienda' y 'Biblioteca'. También llena la tabla 'Tienda' con los datos del csv e ingresa 10 juegos aleatorios a la tabla 'Biblioteca'.
	Luego ejecutar el archivo 'Console.py', el cual da inicio al programa, a través de consola.
	
Nota: 97. -3 Pts. por el Trigger.
