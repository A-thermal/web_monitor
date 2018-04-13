#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,time,requests,re,difflib,sys
from get import getHTML,write,get_write
from compare import time_compare,file_compare
from sender import senders,read
from delete import delete_all
def web_monitor():
	get_write()
	while 0<1:
		if file_compare()==1:
			#print('有更新')
			senders()
			delete_all()
			time.sleep(10800)
		#elif file_compare()==2:
			#senders(_user = "532554678@qq.com",_pwd  = "xayokzllzpubcbci",_to = "zhuojiubanhuanian@163.com",subject="对比爬虫出错", con="error")
			#time.sleep(600)
			#continue
		else:
			time.sleep(10800)





web_monitor()




