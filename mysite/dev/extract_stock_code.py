#!/usr/bin/python
#coding = utf8
import re
import MySQLdb

conn = MySQLdb.connect('localhost','joker','likejoke','finance',charset='utf8')
cursor = conn.cursor()

page = file("/home/work/download/stock/stocks.html").read()
regex = re.compile(r"([\d]{6})\((.*)\)")
for code,name in regex.findall(page):
    query = "insert ignore into BaseInfo(code,name)values('%s','%s');"%(code,name)
#    print query
    cursor.execute(query)
#    print code,name
conn.commit()
   
