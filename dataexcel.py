from xlsxwriter.workbook import Workbook
import cx_Oracle
from queries import sql1


con = cx_Oracle.connect('read/read@192.168.84.20/sitep')
cur = con.cursor()

cur.execute(sql1)

workbook = Workbook('outfile.xlsx')
sheet = workbook.add_worksheet()
for r, row in enumerate(cur.fetchall()):
    for c, col in enumerate(row):
        sheet.write(r, c, col)
print "done :)"
workbook.close()