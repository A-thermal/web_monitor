#!/usr/bin/env Python
# coding=utf-8
import os,sys,smtplib,email
import smtplib
from email.mime.text import MIMEText

def read():
	f_diff = 'F:\\2018\\diff.txt'
	f2 = open(f_diff, "r",encoding='UTF-8')
	renew=f2.read()
	f2.close()
	return renew	


def senders(_user = "532554678@qq.com",_pwd  = "xayokzllzpubcbci",_to   = "zhuojiubanhuanian@163.com",subject= "院网更新",con=read()):

	msg = MIMEText(con)
	msg["Subject"] =subject
	msg["From"]    = _user
	msg["To"]      = _to

	try:
		s = smtplib.SMTP_SSL("smtp.qq.com", 465)
		s.login(_user, _pwd)
		s.sendmail(_user, _to, msg.as_string())
		s.quit()
		#print("Success!")
	except smtplib.SMTPException: 
		print ("Falied,%s" )  


senders()