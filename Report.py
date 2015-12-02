from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
from xlwt import easyxf # http://pypi.python.org/pypi/xlwt

START_ROW = 297 # 0 based (subtract 1 from excel row number)
col_age_november = 1
col_summer1 = 2
col_fall1 = 3

rb = open_workbook(file_path,formatting_info=True)
r_sheet = rb.sheet_by_index(0) # read only copy to introspect the file
wb = copy(rb) # a writable copy (I can't read values out of this, only write to it)
w_sheet = wb.get_sheet(0) # the sheet to write to within the writable copy

for row_index in range(START_ROW, r_sheet.nrows):
    age_nov = r_sheet.cell(row_index, col_age_november).value
    if age_nov == 3:
        #If 3, then Combo I 3-4 year old  for both summer1 and fall1
        w_sheet.write(row_index, col_summer1, 'Combo I 3-4 year old')
        w_sheet.write(row_index, col_fall1, 'Combo I 3-4 year old')

wb.save(file_path + '.out' + os.path.splitext(file_path)[-1])