import xlsxwriter
import insert

def llenar(lista_consumo, lista_total):
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

    print(lista)
    wb.close()
    #insert.insert(lista)