__author__ = 'rjain1'
import win32com.client


def sendMail():
    text_file = open("C:/Users/rjain1/PycharmProjects/report/DailyRep/output.html", "r")
    x = text_file.read()
    # print x

    olMailItem = 0x0
    obj = win32com.client.Dispatch("Outlook.Application")
    newMail = obj.CreateItem(olMailItem)
    newMail.Subject = "International Locale Report"
    # newMail.Body = "body text"
    # newMail.body = open("C:\\Users\\rjain1\\PycharmProjects\\report\\DailyRep\\res.htm").read()
    newMail.To = "rjain1@yodlee.com"
    # newMail.body = open("C:\\Users\\rjain1\\PycharmProjects\\report\\DailyRep\\res_files\\sheet009.htm").read()
    # attachment1 = "c:\\mypic.jpg"
    newMail.HTMLBody = x
    # newMail.Attachments.Add(attachment1)
    newMail.Send()

    print "Mail Sent"

    # sendMail()
