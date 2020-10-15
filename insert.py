import psycopg2

con = psycopg2.connect(database="bd", user="postgres", password="12345678", port=5433)
cursor=con.cursor()


def insert(lista):
    lectura_actual = lista[0]
    lectura_anterior = lista[1]
    consumo = lista[2]
    vertimiento = lista[3]
    total_pagar = lista[4]
    fecha = lista[5]

    sql = "select MAX(id) from facturas"
    cursor.execute(sql)
    max_id = cursor.fetchall()
    max_id = max_id[0][0]
    max_id += 1

    sql="insert into facturas(id, id_restaurante, lectura_actual, lectura_anterior,consumo,vertimiento,total_pagar,fecha) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    datos=(max_id, 1, lectura_actual, lectura_anterior, consumo, vertimiento, total_pagar, fecha)
    cursor.execute(sql, datos)
    con.commit()
    con.close()