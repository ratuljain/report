# __author__ = 'rjain1'

from openpyxl.reader.excel import load_workbook
from win32com.client.gencache import EnsureDispatch
from win32com.client import constants
import os, time
from ConsolidateHtmlCSS import consolidateToHTML
from SendEmail import sendMail


def test_remove_sheet():
    wb = load_workbook('res.xlsx')
    locales = wb.get_sheet_names()
    for i in locales:
        if i == "Sheet1":
            continue
        new_sheet = wb.get_sheet_by_name(i)
        wb.remove_sheet(new_sheet)
        assert new_sheet not in wb.worksheets
    wb.save("res1.xlsx")
    print "Sheets removed"


def convert():
    yourExcelFile = os.getcwd() + '\\res1.xlsx'
    newFileName = os.getcwd() + '\\res.htm'

    xl = EnsureDispatch('Excel.Application')
    wb = xl.Workbooks.Open(yourExcelFile)
    wb.SaveAs(newFileName, constants.xlHtml)
    xl.Workbooks.Close()
    xl.Quit()
    del xl
    print "Converted to HTML"


def execute():
    test_remove_sheet()
    convert()
    time.sleep(3)
    consolidateToHTML()
    time.sleep(3)
    sendMail()

# execute()
