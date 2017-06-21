# -*- coding: UTF-8 -*-
print "Hello Python!"

import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

import json
import urllib
import urllib2
import datetime
import csv
import codecs

MIN_R = 0.1
MAX_PE = 20
MIN_BENEFIT = 0.036

body = "{\"area\":\"cn\",\"ranges\":{\"stockCollectionIdsList\":[[],[10000000300]]},\"filterItems\":[{\"id\":\"stockPriceMetrics.pb\",\"date\":\"\",\"min\":0,\"max\":5},{\"id\":\"stockPriceMetrics.pb_wo_gw\",\"date\":\"\",\"min\":0,\"max\":5},{\"id\":\"metrics.roe.t\",\"date\":\"2016-12-31\",\"min\":0.09,\"max\":\"\"},{\"id\":\"metrics.roe.t\",\"date\":\"2015-12-31\",\"min\":0.09,\"max\":\"\"},{\"id\":\"metrics.roe.t\",\"date\":\"2014-12-31\",\"min\":0.09,\"max\":\"\"},{\"id\":\"metrics.roe.t\",\"date\":\"2013-12-31\",\"min\":0.09,\"max\":\"\"},{\"id\":\"metrics.roe.t\",\"date\":\"2012-12-31\",\"min\":0.09,\"max\":\"\"},{\"id\":\"stockPriceMetrics.dividend_r\",\"date\":\"\",\"min\":\"\",\"max\":\"\"},{\"id\":\"stockPriceMetrics.pe_ttm\",\"date\":\"\",\"min\":\"\",\"max\":\"\"},{\"id\":\"stockPriceMetrics.stock_price\",\"date\":\"\",\"min\":\"\",\"max\":\"\"}],\"sort\":{\"name\":\"stockPriceMetrics.pb\",\"order\":\"desc\"}}"
url = "https://www.lixinger.com/api/analyt/screener/stock"
cookie = "jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1OTNhMTBjYjg3NDQ5NzY3NWYwYTU2N2QiLCJpYXQiOjE0OTc4MzY3NDksImV4cCI6MTQ5ODQ0MTU0OX0.Jl4r6wCSIRH41ZPXfWS4_jetZeV2EBxVKoW20MY6p9I; Hm_lvt_ec0ee7e5c8bed46d4fdf3f338afc08f5=1497836726,1497836762; Hm_lpvt_ec0ee7e5c8bed46d4fdf3f338afc08f5=1497836771"

request = urllib2.Request(url, body)
request.add_header("Cookie", cookie)
request.add_header("Content-Type", "application/json;charset=UTF-8")
result = urllib2.urlopen(request)

resultString = result.read()
print resultString

open("net_result.json", "w").write(resultString)

jsonObject = json.load(open("net_result.json", "r"))

stockList = []

jsonArray = jsonObject["data"]
for o in jsonArray:
    d = {}
    d["code"] = o["stockCode"]
    d["name"] = o["cnName"]

    d["price"] = o["stockPriceMetrics"]["stock_price"]
    d["benefit"] = o["stockPriceMetrics"]["dividend_r"]
    d["pe"] = o["stockPriceMetrics"]["pe_ttm"]
    d["pb"] = o["stockPriceMetrics"]["pb"]
    d["pb_no_corp"] = o["stockPriceMetrics"]["pb_wo_gw"]

    d["roe2012"] = o["2012-12-31"]["metrics"]["roe"]["t"]
    d["roe2013"] = o["2013-12-31"]["metrics"]["roe"]["t"]
    d["roe2014"] = o["2014-12-31"]["metrics"]["roe"]["t"]
    d["roe2015"] = o["2015-12-31"]["metrics"]["roe"]["t"]
    d["roe2016"] = o["2016-12-31"]["metrics"]["roe"]["t"]
    stockList.append(d)

os.remove("net_result.json")


print stockList
for o in stockList:
    o["r1"] = o["roe2016"] / o["pb_no_corp"]
    o["r3"] = (o["roe2016"] + o["roe2015"] + o["roe2014"]) / 3 / o["pb_no_corp"]
    o['roe_average_5'] = (o["roe2016"] + o["roe2015"] + o["roe2014"] + o["roe2013"] + o["roe2012"]) / 5
    o["r5"] = o['roe_average_5'] / o["pb_no_corp"]
    count = 0
    if (o["r1"] >= MIN_R):
        count = count + 1
        o['r1Ok'] = True
    else:
        o['r1Ok'] = False

    if o["r3"] >= MIN_R:
        count = count + 1
        o['r3Ok'] = True
    else:
        o['r3Ok'] = False

    if o["r5"] >= MIN_R:
        count = count + 1
        o['r5Ok'] = True
    else:
        o['r5Ok'] = False

    if o["benefit"] >= MIN_BENEFIT:
        count = count + 1
        o['benefitOk'] = True
    else:
        o['benefitOk'] = False

    if o["pe"] > 0 and o["pe"] <= MAX_PE:
        count = count + 1
        o['peOk'] = True
    else:
        o['peOk'] = False

    o['pb_15'] = o['roe_average_5'] / 15.0 * 100.0
    o['price_15'] = o['price'] / o['pb_no_corp'] * o['pb_15']

    if o['price_15'] > o['price']:
        o['buy'] = 20
    else:
        o['buy'] = 0

    o['pb_12'] = o['roe_average_5'] / 12.0 * 100.0
    o['price_12'] = o['price'] / o['pb_no_corp'] * o['pb_12']
    if o['price_12'] > o['price']:
        o['buy'] += 20
    else:
        o['buy'] += 0

    o['pb_10'] = o['roe_average_5'] / 10.0 * 100.0
    o['price_10'] = o['price'] / o['pb_no_corp'] * o['pb_10']
    if o['price_10'] > o['price']:
        o['buy'] += 60
    else:
        o['buy'] += 0

    o["count"] = count
    print o


# sort
def compare(o1, o2):
    if o2['count'] - o1['count'] != 0:
        return o2['count'] - o1['count']
    else:
        return (int)(10000 * (o2['r1'] - o1['r1']))
    pass


stockList = sorted(stockList, cmp=compare)


def colorRed(o):
    if (o):
        return "<font color='red'>"
    else:
        return ""
    pass


import model
model.write_to_excel(stockList, "lixinger/lixinger_stock_" + datetime.datetime.now().strftime("%Y-%m-%d") + ".xls")

import os
import tushare as ts
import pandas as pd
import csv

if (not os.path.exists('_source')) or (not os.path.isdir('_source')):
    os.mkdir("_source")
    pass


print "success!"
