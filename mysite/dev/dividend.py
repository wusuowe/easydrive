#!/usr/bin/python
#coding = utf8
import re,sys
import MySQLdb
import urllib2
from crawler import *



def getLastDayClose(code,rdate,cursor):
    query = "select close from DailyTrade where code='%s' and rdate<'%s' order by rdate desc limit 1"%(code,rdate)
    print query
    cursor.execute(query)
    close = cursor.fetchone()
    if close != None: return close[0]
    return None

conn = MySQLdb.connect('localhost','joker','likejoke','finance',charset='utf8')
cursor = conn.cursor()

query = "select code from BaseInfo where code = '000001'"
cursor.execute(query)
for code in cursor.fetchall():
    code = code[0]

    query = "select d.send,d.donate,d.divid,d.regdate,d.exedate,d.allotment,d.allotmentprice,t.close from Dividend as d left join DailyTrade as t on d.regdate=t.rdate and d.code=t.code where d.code='%s' order by d.exedate,d.allotment"%code
    print query
    cursor.execute(query)
    print code    
    dividList = []
    recordList = []
   
    num = 0
     
    factor = 1.0
    lastDate = ''
    lastPrice = None
    for send,donate,divid,regdate,exedate,allotment,allotmentprice,close in cursor.fetchall():
        print send,donate,divid,regdate,exedate,allotment,allotmentprice,close
        print '---------------------------------------------------'
        if close == None: 
            close = getLastDayClose(code,exedate,cursor)
        if close == None:
            continue
        print lastDate,exedate
        if lastDate == exedate:
            close = lastPrice
            print close
        print send,donate,divid,regdate,exedate,allotment,allotmentprice,close

        price = (10.0*close + allotmentprice*allotment - divid)/(10.0+send+donate+allotment)
        lastPrice = price
        lastDate = exedate
        print close,price,close/price,factor
        factor *= close/price

        
        dividList.append((exedate,factor))
    
#    print dividList
    length = len(dividList)
    if length == 0: continue
    for i in range(length-1):
        start  = dividList[i][0]
        end    = dividList[i+1][0]
        factor = dividList[i][1]
        query = "update DailyTrade set adjclose=close*%f, adjfactor=%f where code='%s' and rdate>='%s' and rdate<'%s'"%(factor,factor,code,start,end)
        cursor.execute(query)
    start  = dividList[-1][0]
    factor = dividList[-1][1]
    query = "update DailyTrade set adjclose=close*%f, adjfactor=%f where code='%s' and rdate>='%s' "%(factor,factor,code,start)
    cursor.execute(query)
    conn.commit()

   
