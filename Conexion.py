import Header

#conexión
dsn_tns = Header.cx_Oracle.makedsn('localhost', 1521, "xe") #version oracle 18c XE, si no se ocupa una Express Edition, tirará error. Se cambia 'xe' por 'orcl'
connection = Header.cx_Oracle.connect("JOTA", "12345", dsn_tns) #credenciales que se ocuparon para conectar la base de datos, modificar con las suyas
cursor = connection.cursor()  