import 'load_workbook' module
from 'openpyxl'
# from openpyxl import load_workbook
# from openpyxl.utils import get_column_letter,column_index_from_string
# ##load in the workbook
# wb=load_workbook('test.xlsx')
# ##get sheet names
# print(wb.sheetnames)
# ##check tyypes
# print(type(wb))
# print(type(wb.sheetnames))
# ##get a sheet by name
# sheet=wb["Sheet1"]
# ##print the sheet title
# print(sheet.title)
# ##get currently active sheet
# anotherSheet=wb.active
# ##check 'anotherSheet'
# print(anotherSheet)
# ##retrieve the value of a certain cell
# print(sheet['A1'].value)
# print(type(sheet['A1']))
# ##select element 'B2' of your sheet
# c=sheet['B2']
# print(c)
# ##retrieve the row number of your element
# print(c.row)
# print(type(c.row))
# ##retrieve the column letter of your letter
# print(c.column)
# print(type(c.column))
# ##retrieve the coordinates of the cell
# print(c.coordinate)
# print(type(c.coordinate))
# ##retrieve the cell value
# print(sheet.cell(row=1,column=2).value)
##print out values in column 2
for i in range(1,4):
    print(i,sheet.cell(row=i,column=2).value)
# ##
# print(sheet.cell(row=1,column=2))
# print(type(sheet.cell(row=1,column=2)))
# ##
# print(sheet.cell(row=1,column=2).value)
# print(type(sheet.cell(row=1,column=2).value))

# ##return 'A'
# print(get_column_letter(1))
# ##return '1'
# print(column_index_from_string('A'))
# ##print row per row
# for cellObj in sheet['A1':'C3']:
    # for cell in cellObj:
        # print(cell.coordinate,cell.value)
    # print('---END---')
# ##retrieve the max amount of rows
# print(sheet.max_row)
# ##retrieve the max amount of columns
# print(sheet.max_column)

# ##changing title of sheet
# sheet.title='Test Sheet 1'
# print(wb.sheetnames)

# ##saving the changes made in file title
# wb.save('text.xlsx')

# ##creating new sheet
# wb.create_sheet()
# print(wb.sheetnames)

# ##creating new sheet with a diferent name
# wb.create_sheet(index=0,title="first sheet")
# print(wb.sheetnames)

# print(sheet)
# ##deleting a sheet
# wb.remove(sheet) #or del wb[sheetname]
# print(wb.sheetnames)

# ##writing in excel sheet
# sheet['A5']="Hello World"
# print(sheet['A5'].value)

# ##changing value in a cell
# sheet.cell(row=6,column=1).value="Bye Bye"
# print(sheet['A6'].value)
# wb.save('txt.xlsx')
