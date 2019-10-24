import xlsxwriter

#pip install xlsxwriter



# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
# worksheet.set_column('A:A', 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.
# A1 means column = 0 & row = 0.
worksheet.write('A1', 'name',bold)

# Text with formatting.
worksheet.write('B1', 'id', bold)

# Write some numbers, with row/column notation.
# worksheet.write(2, 0, 123)
# worksheet.write(3, 0, 123.456)

# Insert an image.
# worksheet.insert_image('B5', 'logo.png')
data={
    'name':['ANKIT','RAI','RAI3'],
    'id':['63','65','5']
}
col=0
for key in data.keys():
    row=1
    for value in data[key]:
        worksheet.write(row, col, value)
        row+=1
    col+=1

workbook.close()