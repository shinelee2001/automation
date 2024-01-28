import openpyxl as excel

book = excel.load_workbook("py_excel01.xlsx")

sheet = book.worksheets[0]

cell = sheet['A1']
print(cell.value)