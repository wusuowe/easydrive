#!/usr/bin/python
import re,sys
import MySQLdb
import urllib2
from crawler import *

#sys.exit()
conn = MySQLdb.connect('localhost','joker','likejoke','finance',charset='utf8')
cursor = conn.cursor()

tabrep = re.compile(r'<table width="100%" id="Table3">.*?</table>',re.MULTILINE|re.DOTALL)
bodyrep = re.compile(r'<tbody>.*?</tbody>',re.MULTILINE|re.DOTALL)
rowrep = re.compile(r'<tr.*?</tr>',re.MULTILINE|re.DOTALL)
colrep = re.compile(r'<td><div align="left" style="padding-left:4px;">(.*?)</div></td>',re.MULTILINE|re.DOTALL)

query = "select code from BaseInfo where industrycode=''"
cursor.execute(query)
for code in cursor.fetchall():
    code = code[0]
    url = "http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpOtherInfo/stockid/%s/menu_num/2.phtml"%code
    sys.stderr.write("Down load %s industry data\n"%code)
    try:
        page = crawl(url)
       #print page 
        table = tabrep.findall(page.decode('utf8'))[0]
#        print table.encode('gbk')
        body =  bodyrep.findall(table)[0]
#        print body.encode('gbk')
        rows =  rowrep.findall(body)
#        print rows
        industry_name =  colrep.findall(rows[0])[0]
        industry_code =  colrep.findall(rows[1])[0]
    except Exception,e:
        sys.stderr.write("%s"%e)
        print "DownLoad %s industry failed"%code
        continue 
    query = "update BaseInfo set industry = '%s', industrycode='%s' where code='%s';"%(industry_name,industry_code,code)
    cursor.execute(query)
conn.commit()

