from openpyxl import Workbook
import csv

wb = Workbook()
ws = wb.active
with open('libya.csv', 'r') as f:
    for row in csv.reader(f):
        ws.append(row)
wb.save('libya.xlsx')