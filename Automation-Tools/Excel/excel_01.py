import openpyxl as excel

book = excel.Workbook()

sheet = book.active
sheet["A1"] = "first excel word"
book.save("py_excel01.xlsx")