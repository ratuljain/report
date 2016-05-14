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


def cleanUp():
    try:
        shutil.rmtree('C:\\Users\\rjain1\\PycharmProjects\\report\\DailyRep\\res_files')
    except:
        pass
    try:
        os.remove('C:\\Users\\rjain1\\PycharmProjects\\report\\DailyRep\\res.htm')
    except:
        pass
    try:
        os.remove('C:\\Users\\rjain1\\PycharmProjects\\report\\DailyRep\\res.xlsx')
    except:
        pass
    try:
        os.remove('C:\\Users\\rjain1\\PycharmProjects\\report\\DailyRep\\res1.xlsx')
    except:
        pass
    try:
        os.remove('C:\\Users\\rjain1\\PycharmProjects\\report\\DailyRep\\stats.xlsx')
    except:
        pass
    try:
        os.remove('C:\\Users\\rjain1\\PycharmProjects\\report\\DailyRep\\stats.xls')
    except:
        pass
    try:
        os.remove('C:\\Users\\rjain1\\PycharmProjects\\report\\DailyRep\\output.html')
    except:
        pass


cleanUp()


# os.remove('C:\\Users\\rjain1\\PycharmProjects\\report\\DailyRep\\res.xlsx')

def run():
    RetrieveEmail.getMail()
    RetrieveEmail.convertToXlsx()

    ProcessSheet.processSheet()

    Auto.populateDataAuto()
    DoAssignments.doAssignments()

    FormatSheet.formatSheet()

    ConvertTOHTML.test_remove_sheet()
    ConvertTOHTML.convert()
    time.sleep(2)
    ConsolidateHtmlCSS.consolidateToHTML()
    time.sleep(2)

    SendEmail.sendMail()

# run()
