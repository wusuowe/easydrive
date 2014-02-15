#!/usr/bin/python
#coding = utf8
import re
import MySQLdb
import urllib2
from crawler import *

conn = MySQLdb.connect('localhost','joker','likejoke','finance',charset='utf8')
cursor = conn.cursor()

url='http://www.sse.com.cn/disclosure/listedinfo/regular/'
page = crawl(url)
regex = re.compile(r"([\d]{6})\((.*)\)")
for code,name in regex.findall(page):
    query = "insert ignore into BaseInfo(code,name)values('%s','%s');"%(code,name)
    print query
    cursor.execute(query)
#    print code,name
conn.commit()

url='http://www.szse.cn/szseWeb/FrontController.szse?ACTIONID=8&CATALOGID=1110&TABKEY=tab1&ENCODE=1'
page = crawl(url)
page = re.sub('<td.*?>','<td>',page)
#print page
regex = re.compile(r'>([\d]{6})</td><td>(.*?)</td>')
for code,name in regex.findall(page):
    query = "insert ignore into BaseInfo(code,name)values('%s','%s');"%(code,name)
    print query
    cursor.execute(query)


conn.commit()
   
