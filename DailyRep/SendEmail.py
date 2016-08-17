__author__ = 'rjain1'
import win32com.client

import os

cwd = os.getcwd()

def sendMail():
    text_file = open(cwd + "/output.html", "r")
    x = text_file.read()
    # print x

    olMailItem = 0x0
    obj = win32com.client.Dispatch("Outlook.Application")
    newMail = obj.CreateItem(olMailItem)
    newMail.Subject = "International Report"
    # newMail.Body = "body text"
    # newMail.body = open("C:\\Users\\rjain1\\PycharmProjects\\report\\DailyRep\\res.htm").read()
    newMail.To = "rjain1@yodlee.com"

    # # newMail.From = "lvivek@yodlee.com"
    # newMail.To = "rjain1@yodlee.com ; lvivek@yodlee.com; SKumar9@yodlee.com; tgarg@yodlee.com; pdatta1@yodlee.com; atiwari4@yodlee.com; apanda1@yodlee.com; NRavindra@yodlee.com; SSunder@yodlee.com; aparna@yodlee.com"
    # newMail.body = "This is a sample report"
    # attachment1 = "c:\\mypic.jpg"
    newMail.HTMLBody = "Hi Team, <br><br><br> Please find the below table for refresh stats. <br/> This is a test run <br/> <br/> <br/>" + x + "<br>Sincerely, <br> Ratul"
    # newMail.Attachments.Add(attachment1)
    newMail.Send()

    print "Mail Sent"

# sendMail()
