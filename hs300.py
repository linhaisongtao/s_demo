import tushare as ts
import pandas as pd
import csv
import datetime
import os
import model

import sys

MAX_PE = 20
MIN_R = 15

reload(sys)
sys.setdefaultencoding('utf-8')

now = datetime.datetime.now()
now_time = now.strftime("%Y-%m-%d_%H%M")
now_date = now.strftime("%Y-%m-%d")

print "start " + now_time
stockList = []
stockMap = {}

if (not os.path.exists('_stock')) or (not os.path.isdir('_stock')):
    os.mkdir("_stock")
    pass


def getStock(code):
    if stockMap.has_key(code):
        return stockMap[code]
        pass
    pass


# stock
if not os.path.exists("_stock/all.csv"):
    df = ts.get_stock_basics()
    df.to_csv("_stock/all.csv")
    pass
reader = csv.reader(open("_stock/all.csv"))

for i, row in enumerate(reader):
    if i != 0:
        m = {}
        m['code'] = row[0]
        m['name'] = row[1]
        stockList.append(m)
        stockMap[m['code']] = m
        pass
    pass

# price,pe,pb
if not os.path.exists("_stock/price_" + now_date + ".csv"):
    print "_stock/get price_" + now_date
    df = ts.get_today_all()
    print "_stock/got price_" + now_date
    df.to_csv("_stock/price_" + now_date + ".csv")
    pass
reader = csv.reader(open("_stock/price_" + now_date + ".csv"))
for i, row in enumerate(reader):
    if i != 0:
        s = getStock(row[1])
        if s:
            s['price'] = float(row[4])
            s['pe'] = float(row[12])
            s['pb'] = float(row[13])
        pass
    pass

index = len(stockList) - 1
while index >= 0:
    s = stockList[index]
    if not s.has_key('price'):
        stockMap.pop(s['code'])
        stockList.remove(s)
        pass
    index -= 1
    pass

if (now.hour <= 15):
    os.remove("_stock/price_" + now_date + ".csv")
    pass


# roe
def fillROE(y, q):
    if not os.path.exists("_stock/roe_" + str(y) + "_" + str(q) + ".csv"):
        print "get", "_stock/roe_" + str(y) + "_" + str(q)
        df = ts.get_profit_data(y, q)
        print "got", "_stock/roe_" + str(y) + "_" + str(q)
        df.to_csv("_stock/roe_" + str(y) + "_" + str(q) + ".csv", encoding='utf-8')
        pass
    reader = csv.reader(open("_stock/roe_" + str(y) + "_" + str(q) + ".csv"))
    for i, row in enumerate(reader):
        if i != 0:
            s = getStock(row[1])
            if s:
                try:
                    s['roe_' + str(y) + "_" + str(q)] = float(row[3])
                except Exception, e:
                    s['roe_' + str(y) + "_" + str(q)] = 0
                    pass
                pass
            pass
        pass

    for s in stockList:
        if not s.has_key('roe_' + str(y) + "_" + str(q)):
            s['roe_' + str(y) + "_" + str(q)] = 0
            pass
    pass


fillROE(2017, 1)
fillROE(2016, 4)
fillROE(2015, 4)
fillROE(2014, 4)
fillROE(2013, 4)
fillROE(2012, 4)

for i, s in enumerate(stockList):
    roe_average_5 = (s['roe_2016_4'] + s['roe_2015_4'] + s['roe_2014_4'] + s['roe_2013_4'] + s['roe_2012_4']) / 5;
    s['r5'] = roe_average_5 / s['pb']
    s['r3'] = (s['roe_2016_4'] + s['roe_2015_4'] + s['roe_2014_4']) / 3 / s['pb']
    s['r1'] = s['roe_2016_4'] / s['pb']
    s['r'] = s['roe_2017_1'] * 4 / s['pb']

    s['count'] = 0
    if s['r5'] >= MIN_R:
        s['count'] = s['count'] + 1
        pass
    if s['r3'] >= MIN_R:
        s['count'] = s['count'] + 1
        pass
    if s['r1'] >= MIN_R:
        s['count'] = s['count'] + 1
        pass
    if s['r'] >= MIN_R:
        s['count'] = s['count'] + 1
        pass
    if s['pe'] > 0.1 and s['pe'] <= MAX_PE:
        s['count'] = s['count'] + 1
        pass

    s['score'] = 0
    if (s['r5'] >= 15):
        s['score'] = s['score'] + 1
        pass
    if (s['r3'] >= 15):
        s['score'] = s['score'] + 1
        pass
    if (s['r1'] >= 15):
        s['score'] = s['score'] + 1
        pass
    if (s['r'] >= 15):
        s['score'] = s['score'] + 1
        pass

    if (s['r5'] >= 12):
        s['score'] = s['score'] + 1
        pass
    if (s['r3'] >= 12):
        s['score'] = s['score'] + 1
        pass
    if (s['r1'] >= 12):
        s['score'] = s['score'] + 1
        pass
    if (s['r'] >= 12):
        s['score'] = s['score'] + 1
        pass

    if (s['r5'] >= 8):
        s['score'] = s['score'] + 1
        pass
    if (s['r3'] >= 8):
        s['score'] = s['score'] + 1
        pass
    if (s['r1'] >= 8):
        s['score'] = s['score'] + 1
        pass
    if (s['r'] >= 8):
        s['score'] = s['score'] + 1
        pass

    pass

stockList = sorted(stockList, cmp=model.cmp1)

if (not os.path.exists('stock')) or (not os.path.isdir('stock')):
    os.mkdir("stock")
    pass

# model.write_to_csv(stockList, "stock_select_" + now_time + ".csv")
model.write_to_excel(stockList, "stock/all_" + now_date + ".xls")

import source

model.write_selected_stocks_xls(source.get_hs300_codes(), stockMap, "stock/hs300_" + now_date + ".xls")
model.write_selected_stocks_xls(source.get_selected_stocks(), stockMap, "stock/selected_" + now_date + ".xls")
model.write_selected_stocks_xls(source.get_zz500_codes(), stockMap, "stock/zz500_" + now_date + ".xls")
model.write_selected_stocks_xls(source.get_sz50_codes(), stockMap, "stock/sz50_" + now_date + ".xls")

print "success"
