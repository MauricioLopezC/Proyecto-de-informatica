import xlsxwriter
from filemove import file_move

v_items = []
v_costos = []
v_categ = []
v_categ_costo = []
total = 0

band = True
print("ingrese cerrar en item para terminar de ingresar datos")
while band:
    item = input("ingrese el item: ").lower()
    if item != "cerrar":
        costo = int(input("ingrese el costo: "))
        v_items.append(item)
        v_costos.append(costo)
        total += costo
        #categories
        categoria = input("ingrese la categoría: ")
        if categoria not in v_categ:
            v_categ.append(categoria)
            v_categ_costo.append(costo)
        else:
            index = v_categ.index(categoria)
            v_categ_costo[index] = v_categ_costo[index] + costo
    else:
        band = False


#agregamos a las listas el total y su valor
v_items.append("total")
v_costos.append(total)

work_book = xlsxwriter.Workbook("prueba.xlsx")
work_sheet = work_book.add_worksheet()

work_sheet.write_column("A1", v_items)
work_sheet.write_column("B1", v_costos)
work_sheet.write_column("L1", v_categ)
work_sheet.write_column("M1", v_categ_costo)

#insertamos graficos de barras
fila = len(v_items)
grafico = work_book.add_chart({"type":"bar"})

grafico.add_series({
    "categories":f"=Sheet1!$A$1:$A{fila}",
    "values":f"=Sheet1!$B$1:$B${fila}",
    "name" : "COSTOS",
})

work_sheet.insert_chart("C1", grafico)

#nuevo gráfico con los costos por categoría
grafico_categ = work_book.add_chart({"type":"bar"})

fila_catg = len(v_categ)
grafico_categ.add_series({
    "categories":f"=Sheet1!$L$1:$L{fila_catg}",
    "values":f"=Sheet1!$M$1:$M${fila_catg}",
    "name" : "COSTOS POR CATEGORÍA",
})

work_sheet.insert_chart("N1", grafico_categ)

work_book.close()

file_move()
