#!/usr/bin/python
import re,sys
import MySQLdb
import urllib2
from crawler import *

#sys.exit()
conn = MySQLdb.connect('localhost','joker','likejoke','finance',charset='utf8')
cursor = conn.cursor()



def createStockExtractor():
    colrep = re.compile(r'<td><divalign="center">([\d|\-|\.]+)</div></td><td><divalign="center">([\d|\.]+).*?</div></td>',re.MULTILINE|re.DOTALL)
    def stockExtractor(url):
        sys.stderr.write("Download:%s\n"%(url))
        page = crawl(url)
        page = page.replace('\n','').replace('\r','').replace('\t','').replace(' ','')
        return colrep.findall(page)
    return stockExtractor


def createInserter(conn):
    cursor = conn.cursor()
    def Inserter(stockList):
        for Date,Total in stockList:
            query = "insert ignore into StockStruct(code,rdate,total)values('%s','%s','%s')"%(code,Date,Total)
            print query
            cursor.execute(query)
        conn.commit()
    return Inserter




query = "select code from BaseInfo"
cursor.execute(query)

stockExtractor = createStockExtractor()
Inserter = createInserter(conn)
for code in cursor.fetchall():
    code = code[0]
    url = "http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_StockStructureHistory/stockid/%s/stocktype/TotalStock.phtml"%code

#    sys.stderr.write("Down load %s dividend data\n"%code)
    try:
        stockList = stockExtractor(url)
        Inserter(stockList)

    except Exception,e:
        sys.stderr.write("\nDownload %s daily stock data\n\t%s"%(code,e))
