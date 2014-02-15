#!/usr/bin/python
#coding = utf8
import re
import MySQLdb
import urllib2

urlDict = {'cashflow':'http://money.finance.sina.com.cn/corp/go.php/vDOWN_CashFlow/displaytype/4/stockid/%s/ctrl/all.phtml',
        'balancesheet':'http://money.finance.sina.com.cn/corp/go.php/vDOWN_BalanceSheet/displaytype/4/stockid/%s/ctrl/all.phtml',
        'profitstatement':'http://money.finance.sina.com.cn/corp/go.php/vDOWN_ProfitStatement/displaytype/4/stockid/%s/ctrl/all.phtml'}


def crawl(url):
    opener = urllib2.urlopen(url)
    page = opener.read()
    try:
        page = page.decode('gb18030').encode('utf8')
    except:
        pass
    return page


conn = MySQLdb.connect('localhost','joker','likejoke','finance',charset='utf8')
cursor = conn.cursor()

page = file("/home/work/download/stock/stocks.html").read()
regex = re.compile(r"([\d]{6})\((.*)\)")

query = "select code from BaseInfo"
cursor.execute(query)
for code in cursor.fetchall():
    code = code[0]
    for k in urlDict:
        url = urlDict[k]%code
        print '`hhh`%s,%s'%(code,k)
        page = crawl(url)
        query = "select count(*) from Source where code='%s' and `type`='%s'"%(code,k)
        cursor.execute(query)
        if int(cursor.fetchone()[0]) == 0:
            query = "insert into Source (code,`type`,content)values('%s','%s','%s')"%(code,k,page)
        else:
            query = "update Source set content='%s' where code='%s' and `type`='%s'"%(MySQLdb.escape_string(page),code,k)

        print query 
        sys.exit()

#conn.commit()
   
