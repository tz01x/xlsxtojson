import xlrd
#pip install xtrl 

loc=('test.xlsx')
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
# print(dir(sheet))
# sheet.cell_value(0, 0) 
# print((sheet.nrows)) sheet.ncols
for i in range(sheet.nrows):
    
    # for j in range(sheet.ncols):
    #     a=sheet.cell_value(i, j)
    #     print(a,end=' ')
    # print('')
    print(sheet.row_values(i)) #return a list for each row 
