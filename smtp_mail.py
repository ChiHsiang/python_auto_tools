#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
import string

HOST = "smtp.gmail.com"
SUBJECT = "Test Email from python"
TO = "example@gmail.com"
FROM = "example@gmail.com"
text = "Python rules them all!"

BODY =  '''
        From:  {FROM}
        To: {TO}
        Subject {SUBJECT}
         
        {text}
        '''

BODY = BODY.format(FROM=FROM, TO=TO, SUBJECT=SUBJECT, text=text)

server = smtplib.SMTP()
server.connect(HOST, "25")
server.starttls()
server.login("example@gmail.com", "test123")
server.sendmail(FROM, [TO], BODY)
server.quit()
