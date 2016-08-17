import xlrd

import os

cwd = os.getcwd()


# print cwd

def returnDatafromTemplate():
    fname = cwd + "/stats2.xlsx"
    print fname
    bk = xlrd.open_workbook(fname)
    shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name("Sheet1")
    except:
        print "no sheet in %s named Sheet1" % fname
    nrows = sh.nrows
    ncols = sh.ncols
    # print "nrows %d, ncols %d" % (nrows,ncols)

    cell_value = sh.cell_value(1, 1)
    # print cell_value

    row_list = []
    for i in range(1, nrows):
        row_data = sh.row_values(i)
        row_list.append(row_data)

    # for i in row_list:
    #     print i
    return row_list
