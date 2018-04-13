#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests,time,re 

def getHTML(url_1):
	try:
		headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
		html_1=requests.get(url_1,timeout=30,headers=headers)
		#print(html_1.text)
		detail_list=re.findall('<a   href="(.*?)">(.*?)</a>',html_1.text)
		#print(detail_list)	
		return detail_list
	except:
		return 0
def write(list,file_name):
	for m in list:
		url_2="http://ctt.swjtu.edu.cn/zh/"+m[0]
		with open(file_name,'a',encoding='utf-8')as f:
                 f.write(url_2+'\n'+m[1]+'\n')#将所有研究生教学链接写入text文件。


def get_write():
	url_1='http://ctt.swjtu.edu.cn/zh/newsList.jsp?m=248&cp=1&pm=jumpPage'
	file_name='F:\\2018\\web_monitor.txt'
	if getHTML(url_1)==0:
		return 0
	else:
		write(getHTML(url_1),file_name)
		#print("111")


get_write()













