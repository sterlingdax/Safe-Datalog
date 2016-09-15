# Scans: The final frontier. These are the voyages of the missing scans
# The five year mission? To ferret out these bastards and make them pay
# for their insolence! Or, to point out the error of their ways, you pick
import openpyxl

# Open file, one for now, figure out how to open multiple
wb = openpyxl.load_workbook('1-14-2016.xlsx')

# Open the sheet
sheet = wb.active
print(sheet['A2'].value)
# Can't name this variable same as function name, rename it
high = sheet.get_highest_column()
# How to make a range variable that varies, maybe count over the sheet row, use that variable?
for i in range(high):
	print(i, sheet.cell(row=i, column=2).value)
