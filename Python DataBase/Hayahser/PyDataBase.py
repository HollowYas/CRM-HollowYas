import psycopg2

conexion1 = psycopg2.connect(database = "PyDataBase1", user = "postgres", password = "Hayahser15")
cursor1 = conexion1.cursor()

#sql = "insert into articulos(codigo, nombre, tipo, precio) values(%s, %s, %s, %s)"
#datos = (2, "Pera", "Fruta", 11)
#cursor1.execute(sql, datos)

#sql = "insert into articulos(codigo, nombre, tipo, precio) values(%s, %s, %s, %s)"
#datos = (3,"Banano", "Fruta", 12)
#cursor1.execute(sql, datos)

sql = "insert into articulos(codigo, nombre, tipo, precio) values(%s, %s, %s, %s)"
datos = (1,"Sandia", "Fruta", 20)
cursor1.execute(sql, datos)


cursor1.execute("select * from articulos")

for fila in cursor1:
    print(fila)

conexion1.commit()
conexion1.close()
