#from excel2json import convert_from_file


#EXCEL_FILE = 'file_example_XLSX_10.xlsx'  # or '../example.xlsx'
#convert_from_file(EXCEL_FILE)


import json
with open('Sheet1.json') as f:
	with open('Sheet1.json') as jsonfile:
		data=json.load(jsonfile)
		for p in data:
			print(p["First Name"])
