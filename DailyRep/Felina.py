__author__ = 'rjain1'
import RetrieveEmail
import ProcessSheet
import ConvertTOHTML
import SendEmail
import Auto
import FormatSheet
import ConsolidateHtmlCSS
import time
import shutil
import DoAssignments

import os

cwd = os.getcwd()

def cleanUp():
    try:
        shutil.rmtree(cwd + '\\res_files')
    except:
        pass
    try:
        os.remove(cwd + '\\res.htm')
    except:
        pass
    try:
        os.remove(cwd + '\\res.xlsx')
    except:
        pass
    try:
        os.remove(cwd + '\\res1.xlsx')
    except:
        pass
    try:
        os.remove(cwd + '\\stats.xlsx')
    except:
        pass
    try:
        os.remove(cwd + '\\stats.xls')
    except:
        pass
    try:
        os.remove(cwd + '\\output.html')
    except:
        pass


cleanUp()


# os.remove(cwd + '\\res.xlsx')

def run():
    RetrieveEmail.getMail()
    RetrieveEmail.convertToXlsx()

    ProcessSheet.processSheet()

    Auto.populateDataAuto()
    DoAssignments.doAssignments()

    FormatSheet.formatSheet()

    ConvertTOHTML.test_remove_sheet()
    time.sleep(10)
    try:
        ConvertTOHTML.autoFit()
        time.sleep(10)
    except:
        time.sleep(5)
        ConvertTOHTML.autoFit()
        time.sleep(5)
    ConvertTOHTML.convert()
    time.sleep(2)
    ConsolidateHtmlCSS.consolidateToHTML()
    time.sleep(2)

    SendEmail.sendMail()


run()

# RetrieveEmail.getMail()
# RetrieveEmail.convertToXlsx()
# ProcessSheet.processSheet()
#
# Auto.populateDataAuto()
