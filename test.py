import openpyxl

from myexperiencepackage.simplefile import *


read('D:\\pyprojects\\ITI-day4\\file.txt','readline')


write('D:\\pyprojects\\ITI-day4\\file.txt','''
hi my name is islam
''')


# read the excel file
file_path = "D:\\pyprojects\\ITI-day4\\Book1.xlsx"
workbook = openpyxl.load_workbook(filename=file_path)
sheet = workbook["Sheet1"]
cell_value = sheet["A1"].value
print(cell_value)
workbook.close()


##############
#############
#write to the excel file

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet["A1"] = "Hello"
sheet["B1"] = "World"
file_path = "D:\\pyprojects\\ITI-day4\\Book1.xlsx"
workbook.save(filename=file_path)
workbook.close()



