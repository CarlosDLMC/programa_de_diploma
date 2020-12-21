from openpyxl import Workbook
wb = Workbook()

dest_filename = 'empt.xlsx'
ws1 = wb.active


ws1.append([])
ws1.append(['координаты каждой точки и их высоты'])
ws1.append([])
line = list()
for i in range(182):
    line += ['долгота', 'широта', 'высота', '\t']
ws1.append(line)
wb.save(filename = dest_filename)