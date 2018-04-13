#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

def delete_all():
	file1 = open('F:\\2018\\temperate.txt','w')#打开文件
	file1.truncate()
	file1.close()
	file2 = open('F:\\2018\\diff.txt','w')#打开文件
	file2.truncate()
	file2.close()


delete_all()