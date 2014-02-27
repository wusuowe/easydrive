#!/usr/bin/python
#coding = utf8
import re
import MySQLdb
import urllib2
from crawler import *


conn = MySQLdb.connect('localhost','joker','likejoke','finance',charset='utf8')
cursor = conn.cursor()

query = "select code from BaseInfo"
cursor.execute(query)
for code in cursor.fetchall():
    code = code[0]
    if code.startswith('60'):
        url = "http://qt.gtimg.cn/q=s_sh"+code
    else:
        url = "http://qt.gtimg.cn/q=s_sz"+code
    page = crawl(url)
    values =  page.strip().replace('"','').replace(";","").split('~')
    if len(values) < 10: continue
    query = "update BaseInfo set value='%s' where code = '%s'"%(values[9],code)
    print code
    cursor.execute(query)
conn.commit()
sys.exit()

   
