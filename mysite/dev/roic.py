#!/usr/bin/python
#coding=gbk
import MySQLdb
import sys
#b1	货币资金
#b2	结算备付金
#b3	拆出资金
#b4	交易性金融资产
#b5	衍生金融资产
#b6	应收票据
#b7	应收账款
#b8	预付款项
#b9	应收保费
#b10	应收分保账款
#b11	应收分保合同准备金
#b12	应收利息
#b13	应收股利
#b14	其他应收款
#b15	应收出口退税
#b16	应收补贴款
#b17	应收保证金
#b18	内部应收款
#b19	买入返售金融资产
#b20	存货
#b21	待摊费用
#b22	待处理流动资产损益
#b23	一年内到期的非流动资产
#b24	其他流动资产
#b25	流动资产合计
#b26	发放贷款及垫款
#b27	可供出售金融资产
#b28	持有至到期投资
#b29	长期应收款
#b30	长期股权投资
#b31	其他长期投资
#b32	投资性房地产
#b33	固定资产原值
#b34	累计折旧
#b35	固定资产净值
#b36	固定资产减值准备
#b37	固定资产净额
#b38	在建工程
#b39	工程物资
#b40	固定资产清理
#b41	生产性生物资产
#b42	公益性生物资产
#b43	油气资产
#b44	无形资产
#b45	开发支出
#b46	商誉
#b47	长期待摊费用
#b48	股权分置流通权
#b49	递延所得税资产
#b50	其他非流动资产
#b51	非流动资产合计
#b52	资产总计
#b53	短期借款
#b54	向中央银行借款
#b55	吸收存款及同业存放
#b56	拆入资金
#b57	交易性金融负债
#b58	衍生金融负债
#b59	应付票据
#b60	应付账款
#b61	预收款项
#b62	卖出回购金融资产款
#b63	应付手续费及佣金
#b64	应付职工薪酬
#b65	应交税费
#b66	应付利息
#b67	应付股利
#b68	其他应交款
#b69	应付保证金
#b70	内部应付款
#b71	其他应付款
#b72	预提费用
#b73	预计流动负债
#b74	应付分保账款
#b75	保险合同准备金
#b76	代理买卖证券款
#b77	代理承销证券款
#b78	国际票证结算
#b79	国内票证结算
#b80	递延收益
#b81	应付短期债券
#b82	一年内到期的非流动负债
#b83	其他流动负债
#b84	流动负债合计
#b85	长期借款
#b86	应付债券
#b87	长期应付款
#b88	专项应付款
#b89	预计非流动负债
#b90	递延所得税负债
#b91	其他非流动负债
#b92	非流动负债合计
#b93	负债合计
#b94	实收资本(或股本)
#b95	资本公积
#b96	库存股
#b97	专项储备
#b98	盈余公积
#b99	一般风险准备
#b100	未确定的投资损失
#b101	未分配利润
#b102	拟分配现金股利
#b103	外币报表折算差额
#b104	归属于母公司股东权益合计
#b105	少数股东权益
#b106	所有者权益(或股东权益)合计
#b107	负债和所有者权益(或股东权益)总计
#p1      一、营业总收入
#p2      营业收入
#p3      利息收入
#p4      已赚保费
#p5      手续费及佣金收入
#p6      房地产销售收入
#p7      其他业务收入
#p8      二、营业总成本
#p9      营业成本
#p10     利息支出
#p11     手续费及佣金支出
#p12     房地产销售成本
#p13     研发费用
#p14     退保金
#p15     赔付支出净额
#p16     提取保险合同准备金净额
#p17     保单红利支出
#p18     分保费用
#p19     其他业务成本
#p20     营业税金及附加
#p21     销售费用
#p22     管理费用
#p23     财务费用
#p24     资产减值损失
#p25     公允价值变动收益
#p26     投资收益
#p27     其中:对联营企业和合营企业的投资收益
#p28     汇兑收益
#p29     期货损益
#p30     托管收益
#p31     补贴收入
#p32     其他业务利润
#p33     三、营业利润
#p34     营业外收入
#p35     营业外支出
#p36     非流动资产处置损失
#p37     利润总额
#p38     所得税费用
#p39     未确认投资损失
#p40     四、净利润
#p41     归属于母公司所有者的净利润
#p42     少数股东损益
#p43     基本每股收益
#p44     稀释每股收益
#p45     六、其他综合收益
#p46     七、综合收益总额
#p47     归属于母公司所有者的综合收益总额
#p48     归属于少数股东的综合收益总额

#c1	销售商品、提供劳务收到的现金
#c2	客户存款和同业存放款项净增加额
#c3	向中央银行借款净增加额
#c4	向其他金融机构拆入资金净增加额
#c5	收到原保险合同保费取得的现金
#c6	收到再保险业务现金净额
#c7	保户储金及投资款净增加额
#c8	处置交易性金融资产净增加额
#c9	收取利息、手续费及佣金的现金
#c10	拆入资金净增加额
#c11	回购业务资金净增加额
#c12	收到的税费返还
#c13	收到的其他与经营活动有关的现金
#c14	经营活动现金流入小计
#c15	购买商品、接受劳务支付的现金
#c16	客户贷款及垫款净增加额
#c17	存放中央银行和同业款项净增加额
#c18	支付原保险合同赔付款项的现金
#c19	支付利息、手续费及佣金的现金
#c20	支付保单红利的现金
#c21	支付给职工以及为职工支付的现金
#c22	支付的各项税费
#c23	支付的其他与经营活动有关的现金
#c24	经营活动现金流出小计
#c25	经营活动产生的现金流量净额
#c26	收回投资所收到的现金
#c27	取得投资收益所收到的现金
#c28	处置固定资产、无形资产和其他长期资产所收回的现金净额
#c29	处置子公司及其他营业单位收到的现金净额
#c30	收到的其他与投资活动有关的现金
#c31	减少质押和定期存款所收到的现金
#c32	投资活动现金流入小计
#c33	购建固定资产、无形资产和其他长期资产所支付的现金
#c34	投资所支付的现金
#c35	质押贷款净增加额
#c36	取得子公司及其他营业单位支付的现金净额
#c37	支付的其他与投资活动有关的现金
#c38	增加质押和定期存款所支付的现金
#c39	投资活动现金流出小计
#c40	投资活动产生的现金流量净额
#c41	吸收投资收到的现金
#c42	其中：子公司吸收少数股东投资收到的现金
#c43	取得借款收到的现金
#c44	发行债券收到的现金
#c45	收到其他与筹资活动有关的现金
#c46	筹资活动现金流入小计
#c47	偿还债务支付的现金
#c48	分配股利、利润或偿付利息所支付的现金
#c49	0
#c50	支付其他与筹资活动有关的现金
#c51	筹资活动现金流出小计
#c52	筹资活动产生的现金流量净额
#c53	汇率变动对现金及现金等价物的影响
#c54	现金及现金等价物净增加额
#c55	期初现金及现金等价物余额
#c56	期末现金及现金等价物余额
#c57	净利润
#c58	少数股东权益
#c59	未确认的投资损失
#c60	资产减值准备
#c61	固定资产折旧、油气资产折耗、生产性物资折旧
#c62	无形资产摊销
#c63	长期待摊费用摊销
#c64	待摊费用的减少
#c65	预提费用的增加
#c66	处置固定资产、无形资产和其他长期资产的损失
#c67	固定资产报废损失
#c68	公允价值变动损失
#c69	递延收益增加（减：减少）
#c70	预计负债
#c71	财务费用
#c72	投资损失
#c73	递延所得税资产减少
#c74	递延所得税负债增加
#c75	存货的减少
#c76	经营性应收项目的减少
#c77	经营性应付项目的增加
#c78	已完工尚未结算款的减少(减:增加)
#c79	已结算尚未完工款的增加(减:减少)
#c80	其他
#c81	经营活动产生现金流量净额
#c82	债务转为资本
#c83	一年内到期的可转换公司债券
#c84	融资租入固定资产
#c85	现金的期末余额
#c86	现金的期初余额
#c87	现金等价物的期末余额
#c88	现金等价物的期初余额
#c89	现金及现金等价物的净增加额

#息税前利润(EBIT) = 净利润(p40) + 所得税费用(p38) + 利息支出(p10)
#企业价值(EV) = 市值(V) + 期末现金及现金等价物余额(c56) - 负债合计(b93)
#企盈率(ROIC) = 息税前利润(EBIT) / 企业价值(EV)

#有形净资产(NTA) = 资产总计(b52) - 负债合计(b93) - 无形资产(b44)
#有形资产回报率(ROTE) = 息税前利润(EBIT) / 有形净资产(NTA)

DEBUG = True
def LOG(s):
    if DEBUG: print s

conn = MySQLdb.connect('localhost','joker','likejoke','finance',charset='utf8')
cursor = conn.cursor()

def ROTE(code,rdate):
    query = "select p10,p38,p40,b52,b93,b44 from figures where code='%s' and rdate='%s'"%(code,rdate)
    cursor.execute(query)
    rst = cursor.fetchone()
    if rst == None:
        query = "select  p10,p38,p40,b52,b93,b44 from figures where code='%s' and rdate<='%s' order by rdate desc"%(code,rdate)
        cursor.execute(query)
        rst = cursor.fetchone()
    if rst == None:
        return 0
    p10,p38,p40,b52,b93,b44 = rst
    LOG("净利润:%s\n所得税费用:%s\n利息支出:%s\n资产总计:%s\n负债合计:%s\n无形资产:%s\n"%(p40,p38,p10,b52,b93,b44))

    
    ebit = float(p40) + float(p38) + float(p10)
    nta = b52 - b93 - b44
    if nta < 0: return 0

    return ebit/nta

def ROIC(code,rdate):
    query = "select p10,p38,p40,c56,b93 from figures where code='%s' and rdate='%s'"%(code,rdate)
    cursor.execute(query)
    rst = cursor.fetchone()
    if rst == None:
        query = "select p10,p38,p40,c56,b93 from figures where code='%s' and rdate<='%s' order by rdate desc"%(code,rdate)
        cursor.execute(query)
        rst = cursor.fetchone()
    if rst == None:
        return 0
    p10,p38,p40,c56,b93 = rst
    LOG("净利润:%s\n所得税费用:%s\n利息支出:%s\n末现金及现金等价物余额:%s\n负债合计:%s\n"%(p40,p38,p10,c56,b93)) 

    query = "select value from BaseInfo where code='%s'"%code
    cursor.execute(query)
    rst = cursor.fetchone()
    if rst[0] == 0:
        return 0
    v = rst[0]
    
    print v
    
    ebit = float(p40) + float(p38) + float(p10)
    ev = float(v)*100000000 +float(c56) - float(b93)
    if ev < 0: return 0

    return ebit/ev
    
code = '000056'
rdate = '20140101'
LOG("%s\t%.2f%%\t%.2f%%"%(code,ROIC(code,'20140101')*100,ROTE(code,rdate)*100))
sys.exit()
query = "select code from BaseInfo"
cursor.execute(query)

rank = []

for code in cursor.fetchall():
#    print code[0],ROIC(code[0],'20140101')
    code=code[0]
    roic = ROIC(code,rdate)
    rote = ROTE(code,rdate)
    
    rank.append([code,roic,rote])

    LOG("%s\t%.4f\t%.4f"%(code,ROIC(code,rdate),ROTE(code,rdate)))
    LOG("%s\t%.2f%%\t%.2f%%"%(code,ROIC(code,rdate)*100,ROTE(code,rdate)*100))

def cmp1(a):
    return a[1] 

def cmp2(a):
    return a[2]

def cmp5(a):
    return a[5]
    
rank.sort(key=cmp1,reverse=True)
for i in range(len(rank)):
    rank[i].append(i+1)
#    print rank[i]
rank.sort(key=cmp2,reverse=True)
for i in range(len(rank)):
    rank[i].append(i+1)
#    print rank[i]

for i in range(len(rank)):
    rank[i].append(rank[i][3]+rank[i][4])
#    print rank[i]

rank.sort(key=cmp5,reverse=False)

s = "\n".join(["%s\t%.2f\t%.2f\t%d\t%d\%d"%tuple(r) for r in rank])

print s


