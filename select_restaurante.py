import psycopg2

con = psycopg2.connect(database="bd", user="postgres", password="12345678", port=5433)
cursor=con.cursor()


def info_restaurante(mes,nombre,año):
    sql = "SELECT * FROM facturas WHERE id_restaurante = (SELECT id FROM restaurantes WHERE nombre = %s)ORDER BY id ASC "
    datos=(nombre,)
    cursor.execute(sql,datos)
    restaurantes = cursor.fetchall()
    return restaurantes