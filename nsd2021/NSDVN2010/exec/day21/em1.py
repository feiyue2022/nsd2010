#!/usr/bin/env python
import smtplib

from email.mime.text import MIMEText
from email.header import Header

#邮件的四个主体，发件人、收件人、主题、正文
fromer = 'tom'
reciver = 'root'
subject = 'Python test email'
text = 'This is python test for email sender'

#对邮件的四个主体进行封装
msg = MIMEText(text,'plain','utf-8')        #plain表示纯文本、utf-8表示富文本
msg['From'] = Header(fromer,'utf-8')
msg['To'] = Header(reciver,'utf-8')
msg['Subject'] = Header(subject,'utf-8')

#发送邮件，所有信息流在发送的过程中都是bytes类型
smtp = smtplib.SMTP('127.0.0.1')
smtp.sendmail(fromer,reciver,msg.as_bytes())