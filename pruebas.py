import xlsxwriter

v_items = []
v_costos = []
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
    else:
        band = False


#agregamos a las listas el total y su valor
v_items.append("total")
v_costos.append(total)

work_book = xlsxwriter.Workbook("prueba.xlsx")
work_sheet = work_book.add_worksheet()

work_sheet.write_column("A1", v_items)
work_sheet.write_column("B1", v_costos)

#insertamos graficos de barras
fila = len(v_items)
grafico = work_book.add_chart({"type":"bar"})

grafico.add_series({
    "categories":"=Sheet1!$A$1:$A{fila}",
    "values":"=Sheet1!$B$1:$B${fila}",
    "name" : "COSTOS"
})

work_sheet.insert_chart("C1", grafico)

work_book.close()
