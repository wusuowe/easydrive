#!/usr/bin/python
#coding = utf8
import re
import MySQLdb
import urllib2
from crawler import *

urlDict = {'cashflow':'http://money.finance.sina.com.cn/corp/go.php/vDOWN_CashFlow/displaytype/4/stockid/%s/ctrl/all.phtml',
        'balancesheet':'http://money.finance.sina.com.cn/corp/go.php/vDOWN_BalanceSheet/displaytype/4/stockid/%s/ctrl/all.phtml',
        'profitstatement':'http://money.finance.sina.com.cn/corp/go.php/vDOWN_ProfitStatement/displaytype/4/stockid/%s/ctrl/all.phtml'}




conn = MySQLdb.connect('localhost','joker','likejoke','finance',charset='utf8')
cursor = conn.cursor()

query = "select code from BaseInfo"
cursor.execute(query)
for code in cursor.fetchall():
    code = code[0].encode('utf8')
    for k in urlDict:
        url = urlDict[k]%code
        page = crawl(url)
        query = "select count(*) from Source where code='%s' and `type`='%s'"%(code,k)
        cursor.execute(query)
        if int(cursor.fetchone()[0]) == 0:
            query = "insert into Source (code,`type`,content)values('%s','%s','%s')"%(code,k,MySQLdb.escape_string(page))
        else:
            query = "update Source set content='%s' where code='%s' and `type`='%s'"%(MySQLdb.escape_string(page),code,k)

        print "update %s %s"%(code,k)
        cursor.execute(query)
        conn.commit()
sys.exit()

   
