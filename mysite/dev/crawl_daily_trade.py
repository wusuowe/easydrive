#!/usr/bin/python
import re,sys
import MySQLdb
import urllib2
from crawler import *
from datetime import date
#sys.exit()
conn = MySQLdb.connect('localhost','joker','likejoke','finance',charset='utf8')
cursor = conn.cursor()


def createYearExtractor():
    selrep = re.compile('<select name="year">.*?</select>',re.MULTILINE|re.DOTALL)
    yearrep = re.compile('<option value="(\d+)?"',re.MULTILINE|re.DOTALL)
    def yearExtractor(url):
        page = crawl(url)
        select = selrep.findall(page.decode('utf8'))[0]
        return yearrep.findall(select)
    return yearExtractor

def createTradeExtractor():
    tabrep = re.compile(r'<table id="FundHoldSharesTable">.*?</table>',re.MULTILINE|re.DOTALL)
    rowrep = re.compile(r'<tr.*?</tr>',re.MULTILINE|re.DOTALL)
    colrep = re.compile(r'>([\d|\-|\.]+)</div>',re.MULTILINE|re.DOTALL)
    def tradeExtractor(url):
        sys.stderr.write("Download:%s\n"%(url))
        page = crawl(url)
        table = tabrep.findall(page)
        if len(table) == 0:
            return []
        rows  = rowrep.findall(table[0].replace('\n','').replace('\r','').replace(' ','').replace('\t','').replace('</a>',''))
        tradeList = []
        for row in rows:
            items = colrep.findall(row)
            if len(items) == 7: 
                tradeList.append(items)
        return tradeList
    return tradeExtractor


def createInserter(conn):
    cursor = conn.cursor()
    def Inserter(tradeList):
        for Date,Open,High,Close,Low,Volume,Money in tradeList:
            query = "insert ignore into DailyTrade(code,rdate,open,high,low,close,volume,adjclose)values('%s','%s','%s','%s','%s','%s','%s','%s')"%(code,Date,Open,High,Low,Close,Volume,Close)
            print query
            cursor.execute(query)
        conn.commit()
    return Inserter




query = "select code from BaseInfo"
cursor.execute(query)

yearExtractor = createYearExtractor()
tradeExtractor = createTradeExtractor()
Inserter = createInserter(conn)

if len(sys.argv) > 1:
    mode = sys.argv[1]
else:
    mode = "incremental"

today = date.today()

for code in cursor.fetchall():
    code = code[0]
    url = "http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_MarketHistory/stockid/%s.phtml"%code


#    sys.stderr.write("Down load %s dividend data\n"%code)
    try:
        if mode == "incremental":
            tradeList = tradeExtractor(url)
            Inserter(tradeList)
            continue

        years = yearExtractor(url) 
        urls = []
        for year in years:
            if int(year) < 1990: 
                urls = []
                break
            for quart in range(4,0,-1):
                if today.year == int(year) and quart > (today.month+2)/3:
                    continue
                urls.append("%s?year=%s&jidu=%d"%(url,year,quart))
        for url in urls:
            tradeList = tradeExtractor(url)
            Inserter(tradeList)

    except Exception,e:
        sys.stderr.write("\nDownload %s daily trade data\n\t%s"%(code,e))
