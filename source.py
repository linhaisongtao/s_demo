import os
import tushare as ts
import pandas as pd
import csv

if (not os.path.exists('_source')) or (not os.path.isdir('_source')):
    os.mkdir("_source")
    pass

def get_selected_stocks():
    f = open('_source/source.txt')
    lines = f.readlines()
    stocks = []
    for l in lines:
        stocks.append(l.replace("\n", ""))
        pass
    print stocks
    return stocks
    pass


def get_hs300_codes():
    s = []
    # stock
    if not os.path.exists("_stock/hs300.csv"):
        df = ts.get_hs300s()
        df.to_csv("_stock/hs300.csv")
        pass
    reader = csv.reader(open("_stock/hs300.csv"))

    for i, row in enumerate(reader):
        if i != 0:
            s.append(row[1])
            pass
        pass

    return s
    pass

def get_zz500_codes():
    s = []
    # stock
    if not os.path.exists("_stock/zz500.csv"):
        df = ts.get_zz500s()
        df.to_csv("_stock/zz500.csv")
        pass
    reader = csv.reader(open("_stock/zz500.csv"))

    for i, row in enumerate(reader):
        if i != 0:
            s.append(row[1])
            pass
        pass

    return s
    pass

def get_sz50_codes():
    s = []
    # stock
    if not os.path.exists("_stock/sz50.csv"):
        df = ts.get_sz50s()
        df.to_csv("_stock/sz50.csv")
        pass
    reader = csv.reader(open("_stock/sz50.csv"))

    for i, row in enumerate(reader):
        if i != 0:
            s.append(row[1])
            pass
        pass

    return s
    pass
