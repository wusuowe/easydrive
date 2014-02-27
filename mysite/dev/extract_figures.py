#!/usr/bin/python
import re,sys
import MySQLdb
import urllib2
from crawler import *

types = ['cashflow','balancesheet','profitstatement']
type2fields = {}

for t in types:
    d = {}
    for line in file('%s.txt'%t):
        print line
        items = line.decode('gb18030').split()
        d[items[1]] = items[0]
#        print items[1].encode('utf8')
#        print items[1].encode('gb18030')
        type2fields[t] = d
       
#print type2fields



#sys.exit()
conn = MySQLdb.connect('localhost','joker','likejoke','finance',charset='utf8')
cursor = conn.cursor()

query = "select code,`type`,content from Source"
cursor.execute(query)
for code,typ,content in cursor.fetchall():
    updateList = []
    dateList  = []
    for line in content.split('\n'):
        items = line.split()
        if len(updateList) ==0 :
            updateList = [""]*(len(items)-1)
            num = len(items)
        if len(items) < num:continue

        for i in range(0,num-1):
            if type2fields.has_key(typ) and type2fields[typ].has_key(items[0]):
                if type2fields[typ][items[0]] == 'rdate':
                    dateList.append(items[i+1])
                else:
                    updateList[i] += "%s='%s',"%(type2fields[typ][items[0]],items[i+1])
    for i in range(len(updateList)):
        if dateList[i] == '19700101': continue
        initStatement = "insert ignore into figures(code,rdate)values('%s','%s');"%(code,dateList[i])
        updateStatement = "update figures set %s where code='%s' and rdate='%s';"%(updateList[i].strip(','),code,dateList[i])
        print initStatement
        print updateStatement
        cursor.execute(initStatement)
        cursor.execute(updateStatement)
        conn.commit()

        

   
