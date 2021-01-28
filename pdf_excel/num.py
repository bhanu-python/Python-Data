import openpyxl
from openpyxl import Workbook
wb=Workbook()
ws=wb.active

for i in range(1,100):

    ws['A'+str(i)]=i

wb.save('test.xlsx')
