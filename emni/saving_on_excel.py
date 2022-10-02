import xlsxwriter

workbook = xlsxwriter.Workbook("1.xlsx")
worksheet = workbook.add_worksheet("1sheet")

worksheet.write(0,0,"#")
worksheet.write(0,1,"Soham")
worksheet.write(0,2,"Chaudhuri")

workbook.close()
