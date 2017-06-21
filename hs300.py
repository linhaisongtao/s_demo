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

now_time = datetime.datetime.now().strftime("%Y-%m-%d_%H")

print "start " + now_time
stockList = []
stockMap = {}


def getStock(code):
    if stockMap.has_key(code):
        return stockMap[code]
        pass
    pass


# stock
if not os.path.exists("hs300.csv"):
    df = ts.get_hs300s()
    df.to_csv("hs300.csv")
    pass
reader = csv.reader(open("hs300.csv"))

for i, row in enumerate(reader):
    if i != 0:
        m = {}
        m['code'] = row[1]
        m['name'] = row[2]
        stockList.append(m)
        stockMap[m['code']] = m
        pass
    pass

# pb,pe
if not os.path.exists("all_stock_" + now_time + ".csv"):
    df = ts.get_stock_basics()
    df.to_csv("all_stock_" + now_time + ".csv")
    pass
reader = csv.reader(open("all_stock_" + now_time + ".csv"))
for i, row in enumerate(reader):
    if i != 0:
        s = getStock(row[0])
        if s:
            s['pe'] = float(row[4])
            s['pb'] = float(row[14])
        pass
    pass


# roe
def fillROE(y, q):
    if not os.path.exists("roe_" + str(y) + "_" + str(q) + ".csv"):
        print "get", "roe_" + str(y) + "_" + str(q)
        df = ts.get_profit_data(y, q)
        print "got", "roe_" + str(y) + "_" + str(q)
        df.to_csv("roe_" + str(y) + "_" + str(q) + ".csv", encoding='utf-8')
        pass
    reader = csv.reader(open("roe_" + str(y) + "_" + str(q) + ".csv"))
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


def cmp1(o1, o2):
    if (o2['score'] - o1['score']) == 0:
        return (int)(10000 * (o2['r1'] - o1['r1']))
    else:
        return o2['score'] - o1['score']
    pass


stockList = sorted(stockList, cmp=cmp1)

model.write_to_csv(stockList, "stock_select_" + now_time + ".csv")
model.write_to_excel(stockList, "stock_select_" + now_time + ".xls")

import json

selected_array = json.load(open("select.json"))
selected_list = []
for selected in selected_array:
    s = getStock(selected)
    if s:
        selected_list.append(s)
        pass
    pass
selected_list = sorted(selected_list, cmp=cmp1)
for i, s in enumerate(selected_list):
    print i, s
    pass

model.write_to_csv(selected_list, "select_" + now_time + ".csv")
model.write_to_excel(selected_list, "select_" + now_time + ".xls")

print "success"
