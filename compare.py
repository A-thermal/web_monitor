#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,time,requests,re,difflib,sys
from get import getHTML,write

def time_compare():#比较网页的修改时间和爬取的本地文件修改时间的前后
	def turn_time_1(time_1):#对网页的修改时间进行转换（转换为时间戳）
		tm = time.strptime(time_1, '%a, %d %b %Y %H:%M:%S GMT')
		timeArray = time.strptime(time_1, '%a, %d %b %Y %H:%M:%S GMT')
		timeStamp = int(time.mktime(timeArray))
		return timeStamp

	def turn_time_2(time_2):#对文件的日期格式进行转化
		tm = time.strptime(time_2, '%a %b %d %H:%M:%S %Y')
		timeArray = time.strptime(time_2, '%a %b %d %H:%M:%S %Y')
		timeStamp = int(time.mktime(timeArray))
		return timeStamp
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
	url = 'http://ctt.swjtu.edu.cn/zh/newsList.jsp?m=248&cp=1&pm=jumpPage'
	z = requests.get(url,headers=headers)
	#print(z.headers)#测试成功
	last_modified = z.headers['Date']
	#print(last_modified)#测试成功   
	STAMP_TIME_1=turn_time_1(last_modified)
	#print(STAMP_TIME_1)#测试成功
	file_time=time.ctime(os.stat("F:\\2018\\web_monitor.txt").st_mtime)#获得本地链接库的最后修改时间
	#print(file_time)#测试成功
	STAMP_TIME_2=turn_time_2(file_time)
	#print(STAMP_TIME_2)#测试成功
	if STAMP_TIME_2-STAMP_TIME_1>0:
		#print("没有更新")
		return 0
	else:
		#print("更新了")
		return 1


def file_compare():
	url_1='http://ctt.swjtu.edu.cn/zh/newsList.jsp?m=248&cp=1&pm=jumpPage'
	file_name='F:\\2018\\temperate.txt'
	if getHTML==0:
		return 2#抓不到temperate.text
	else:

		write(getHTML(url_1),file_name)
		file1 = 'F:\\2018\\web_monitor.txt'
		file2 = 'F:\\2018\\temperate.txt'
		f_diff = 'F:\\2018\\diff.txt'

		# ---------- 对比文件内容，输出差异
		f1 = open(file1, "r",encoding='UTF-8')
		f2 = open(file2, "r",encoding='UTF-8')
		file1 = f1.readlines()
		file2 = f2.readlines()
		f1.close()
		f2.close()
		outfile = open(f_diff, "w",encoding='UTF-8')
		flag = 0
		for i in file2:
			if i not in file1:
				outfile.write(i)
		flag = 1
		outfile.close()
		if flag == 1:
			return 1
			#print( "数据存在差异，请仔细核对！") 
		else:
			return 0#院网没有更新




file_compare()