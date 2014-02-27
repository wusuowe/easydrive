#!/bin/bash
code=600001
wget "http://money.finance.sina.com.cn/corp/go.php/vDOWN_BalanceSheet/displaytype/4/stockid/$code/ctrl/all.phtml" -O all.phtml
cat all.phtml |awk '{if(NR>2 && NF>1) print $1}' |awk 'BEGIN{print "rdate\t报表日期"}{print "b"NR"\t"$1}' >balancesheet.txt

wget "http://money.finance.sina.com.cn/corp/go.php/vDOWN_CashFlow/displaytype/4/stockid/$code/ctrl/all.phtml" -O all.phtml
cat all.phtml |awk '{if(NR>2 && NF>1) print $1}' |awk 'BEGIN{print "rdate\t报表日期"}{print "c"NR"\t"$1}' >cashflow.txt

wget "http://money.finance.sina.com.cn/corp/go.php/vDOWN_ProfitStatement/displaytype/4/stockid/$code/ctrl/all.phtml" -O all.phtml
cat all.phtml |awk '{if(NR>2 && NF>1) print $1}' |awk 'BEGIN{print "rdate\t报表日期"}{print "p"NR"\t"$1}' >profitstatement.txt

cat balancesheet.txt cashflow.txt profitstatement.txt|grep -v 'rdate'|awk 'BEGIN{printf("create table figures (id int(11) not null AUTO_INCREMENT,code varchar(6) not null,rdate date not null")}{printf(",%s double not null default 0",$1)}END{printf("PRIMARY KEY (`id`),UNIQUE KEY `code` (`code`,`rdate`))ENGINE=InnoDB DEFAULT CHARSET=utf8;")}'


echo "rdate 报告期" >>cashflow.txt
