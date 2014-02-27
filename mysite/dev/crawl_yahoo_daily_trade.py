#!/usr/bin/python
import re,sys
import MySQLdb
import urllib2
from crawler import *

#sys.exit()
conn = MySQLdb.connect('localhost','joker','likejoke','finance',charset='utf8')
cursor = conn.cursor()

query = "select code from BaseInfo"
cursor.execute(query)
for code in cursor.fetchall():
    code = code[0]
    if code.startswith('60'):
        url = "http://table.finance.yahoo.com/table.csv?s=%s.ss"%code
    else: 
        url = "http://table.finance.yahoo.com/table.csv?s=%s.sz"%code
    sys.stderr.write("down load %s daily trade data\n"%code)
    try:
        page = crawl(url)
    except Exception,e:
        sys.stderr.write("%s"%e)
        print "DownLoad %s failed"%code
    for line in page.strip().split('\n')[1:]:
        Date,Open,High,Low,Close,Volume,AdjClose = line.split(',')
        query = "insert ignore into DailyTrade(code,rdate,open,high,low,close,volume,adjclose)values('%s','%s','%s','%s','%s','%s','%s','%s')"%(code,Date,Open,High,Low,Close,Volume,AdjClose)
        cursor.execute(query)
    conn.commit()

