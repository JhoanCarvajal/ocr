import xlsxwriter
import insert
import datetime
import os
from subprocess import call
import datetime

def llenar(lista_consumo, lista_total, lista_fecha):
    wb = xlsxwriter.Workbook('excel/xlsxWrite.xlsx')
    ws = wb.add_worksheet()

    row = 0
    col = 0
    texto = ""
    lista = []

    for i in lista_consumo:
        if i.isdigit():
            ws.write(row, col, texto)
            texto = ""
            row+=1
            ws.write(row, col, int(i))
            lista.append(int(i))
            row-=1
            col+=1
        else:
            texto += " " + i

    for i in lista_total:
        if i.isalnum() == False:
            boolean = False
            num = ""
            for o in i:
                if o.isdigit():
                    boolean = True
                    num+= o
            if boolean:
                ws.write(row, col, "Total a pagar")
                row+=1
                ws.write(row, col, int(num))
                lista.append(int(num))
                row-=1
                col+=1
    
    for dato in lista_fecha:
        datos_fecha = dato.split("/")
        meses = ["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic"]
        mes=datos_fecha[1]
        temp = len(mes)
        mes = mes[:temp - 1]
        for m in meses:
            if m == mes:
                mes = meses.index(m) + 1
        fecha = str(datos_fecha[2]) + "-" + str(mes) + "-" + str(datos_fecha[0])
        fecha = datetime.datetime.strptime(fecha,"%Y-%m-%d")
        lista.append(fecha)

    print(lista)
    wb.close()
    insert.insert(lista)

def cosulta(resultado):
    wb = xlsxwriter.Workbook('excel/resultado_consulta.xlsx')
    ws = wb.add_worksheet()

    row = 0
    col = 0

    titulos = ["#","Cod restaurante","Lectura actual","Lectura anterior","Consumo","Vertimiento","Total a pagar","fecha"]
    for titulo in titulos:
        ws.write(row, col, titulo)
        col +=1
    col = 0
    for restaurante in resultado:
        row +=1
        for dato in restaurante:
            if isinstance(dato, datetime.date):
                dato = dato.strftime("%Y-%m-%d")
                ws.write(row, col, dato)
            else:
                ws.write(row, col, dato)
            col +=1
        col = 0
            
    wb.close()
    os.system("C:/Users/Jhoan/Documents/tecnoparque/ocr/excel/resultado_consulta.xlsx")

