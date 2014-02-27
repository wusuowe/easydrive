#!/usr/bin/python
import re,sys
import MySQLdb
import urllib2
from crawler import *

#sys.exit()
conn = MySQLdb.connect('localhost','joker','likejoke','finance',charset='utf8')
cursor = conn.cursor()

tabrep = re.compile(r'<table id="sharebonus_1">.*?</table>',re.MULTILINE|re.DOTALL)
tabrep2 = re.compile(r'<table id="sharebonus_2">.*?</table>',re.MULTILINE|re.DOTALL)
bodyrep = re.compile(r'<tbody>.*?</tbody>',re.MULTILINE|re.DOTALL)
rowrep = re.compile(r'<tr>.*?</tr>',re.MULTILINE|re.DOTALL)
colrep = re.compile(r'<td>(.*?)</td>',re.MULTILINE|re.DOTALL)

query = "select code from BaseInfo"
cursor.execute(query)
for code in cursor.fetchall():
    code = code[0]
    url = "http://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_ShareBonus/stockid/%s.phtml"%code
    sys.stderr.write("Down load %s dividend data\n"%code)
    try:
        page = crawl(url)
        #print page
        table = tabrep.findall(page.decode('utf8'))[0]
#        print table.encode('gbk')
        body =  bodyrep.findall(table)[0]
#        print body.encode('gbk')
        rows =  rowrep.findall(body)
#        print rows
    except Exception,e:
        sys.stderr.write("%s"%e)
        print "DownLoad %s dividend failed"%code
        continue

    for row in rows:
        try:
            rd,send,donate,divid,process,exedate,regdate,listdate,desc = colrep.findall(row)
        except:
            print "Extract %s Divived data failed"%code
            continue
        query = "insert ignore into Dividend (code,rdate) values('%s','%s');"%(code,rd)
        cursor.execute(query)
        query = "update Dividend set send = '%s',donate='%s',divid='%s',process='%s',exedate='%s',regdate='%s',listdate='%s' where code='%s' and rdate='%s';"%(send,donate,divid,process,exedate,regdate,listdate,code,rd)
        cursor.execute(query)
    table = tabrep2.findall(page.decode('utf8'))[0]
#    print table.encode('gbk')
    body =  bodyrep.findall(table)[0]
#    print body.encode('gbk')
    rows =  rowrep.findall(body)
    for row in rows: 
        try:        
            rd,allotment,allotmentprice,oldnum,exedate,regdate,startpay,endpay,listdate,money,desc = colrep.findall(row)
            #print rd,allotment,allotmentprice,oldnum,exedate,regdate,startpay,endpay,listdate,money
        except Exception,e:
            print "Extract %s Alloment data failed:\n\t%s"%(code,e)
            continue
        
        query = "insert ignore into Dividend (code,rdate) values('%s','%s');"%(code,rd)
        cursor.execute(query)
        query = "update Dividend set allotment = '%s',allotmentprice='%s',exedate='%s',regdate='%s',startpay='%s',endpay='%s',listdate='%s' where code='%s' and rdate='%s';"%(allotment,allotmentprice,exedate,regdate,startpay,endpay,listdate,code,rd)
        cursor.execute(query)

        
    conn.commit()

