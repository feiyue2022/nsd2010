#!/usr/bin/env python
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#定义主体
msg_from = '903511044@qq.com'
password = 'qapufihrwyqobfhc'           #不是QQ邮箱的密码，是拿到的那个授权码
# msg_to = '2851318846@qq.com'
msg_to = 'lijiying@tedu.cn'
# #你们可以都发送给我
msg_sub = "你好"
content = '这是Python测试用QQ邮箱发送邮件'
#封装邮件信息
msg = MIMEText(content,'plain','utf-8')
msg['From'] = Header(msg_from,'utf-8')
msg['To'] = Header(msg_to,'utf-8')
msg['Subject'] = Header(msg_sub,'utf-8')

receivers = ['903511044@qq.com','2851318846@qq.com']
#发送邮件
try:
    #1、连接QQ邮件服务器
    # smtp = smtplib.SMTP_SSL('smtp.qq.com', smtplib.SMTP_SSL_PORT)
    smtp = smtplib.SMTP('smtp.qq.com')
    print('连接QQ邮件服务器成功')
    #2、登录QQ邮箱
    smtp.login(msg_from,password)
    print('登录成功')
    #3、发送邮件
    smtp.sendmail(msg_from,receivers,msg.as_bytes())
    print('邮件发送成功')
except smtplib.SMTPException as e:
    print('发送邮件失败')
finally:
    smtp.quit()