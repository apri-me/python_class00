import openpyxl # pip install openpyxl 
# link: https://realpython.com/openpyxl-excel-spreadsheets-python/

wb = openpyxl.Workbook()
active_sheet = wb.active
active_sheet['A1'] = 'ali'
active_sheet['B2'] = 'afroozi'
active_sheet.cell(row=2, column=3).value = 'ronaldo'
wb.save("test.xlsx")
