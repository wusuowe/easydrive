#!/usr/bin/python
#coding = utf8
import re,sys
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
        url = "http://hq.sinajs.cn/list=sh"+code
    else:
        url = "http://hq.sinajs.cn/list=sz"+code

    try:
        page = crawl(url)
        values =  page.strip().replace('"','').replace(";","").split(',')
        if len(values) < 33: continue
        Name,Open,YClose,Current,High,Low,B,S,Volume,Money,BV1,B1,BV2,B2,BV3,B3,BV4,B4,BV5,B5,SV1,S1,SV2,S2,SV3,S3,SV4,S4,SV5,S5,Date,Time,TZ = values
        #print Open,Current,High,Low,Volume,Date 
        query = "insert ignore into DailyTrade set code = '%s',rdate = '%s'"%(code,Date)
        cursor.execute(query)
        query = "update DailyTrade set open='%s',close='%s',high='%s',low='%s',volume='%s' where code = '%s' and rdate='%s'"%(Open,Current,High,Low,Volume,code,Date)
        cursor.execute(query)
    except Exception,e:
        sys.stderr.write("Download current daily trade:\n\t>>%s\n"%e)
conn.commit()

   
