# __author__ = 'rjain1'

from openpyxl.reader.excel import load_workbook
from win32com.client.gencache import EnsureDispatch
from win32com.client import constants
import os, time
from ConsolidateHtmlCSS import consolidateToHTML
from SendEmail import sendMail
from win32com.client import Dispatch


# import os, time

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


def autoFit():
    excel = Dispatch('Excel.Application')
    wb = excel.Workbooks.Open(os.getcwd() + '\\res1.xlsx')

    # Activate second sheet
    excel.Worksheets(1).Activate()

    # Autofit column in active sheet
    excel.ActiveSheet.Columns.AutoFit()
    excel.ActiveSheet.Rows.AutoFit()

    # Save changes in a new file
    # wb.SaveAs(os.getcwd() + '\\res2.xlsx')

    # Or simply save changes in a current file
    wb.Save()

    wb.Close()
    print "Autofit done"

def execute():
    test_remove_sheet()
    # convert()
    # time.sleep(3)
    # consolidateToHTML()
    # time.sleep(3)
    # sendMail()

# execute()
# autoFit()
