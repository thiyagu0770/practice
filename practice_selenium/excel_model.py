import openpyxl

def read(i, j):
    excel_loc = r"D:\Selenium\Details.xlsx"
    book = openpyxl.load_workbook(excel_loc)
    s = book.active
    x = s.cell(i, j)
    v = x.value
    return v



