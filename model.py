import xlwt


def write_to_excel(list, file_name):
    wb = xlwt.Workbook(encoding='utf-8')
    sh = wb.add_sheet("a")
    c = 0
    sh.write(0, c, 'name')
    c += 1
    sh.write(0, c, 'code')
    c += 1
    sh.write(0, c, 'price')
    c += 1
    sh.write(0, c, 'count')
    c += 1
    sh.write(0, c, 'score')
    c += 1
    sh.write(0, c, 'pe')
    c += 1
    sh.write(0, c, 'pb')
    c += 1
    sh.write(0, c, 'r')
    c += 1
    sh.write(0, c, 'r1')
    c += 1
    sh.write(0, c, 'r3')
    c += 1
    sh.write(0, c, 'r5')
    c += 1
    sh.write(0, c, 'roe_2017_1')
    c += 1
    sh.write(0, c, 'roe_2016_4')
    c += 1
    sh.write(0, c, 'roe_2015_4')
    c += 1
    sh.write(0, c, 'roe_2014_4')
    c += 1
    sh.write(0, c, 'roe_2013_4')
    c += 1
    sh.write(0, c, 'roe_2012_4')
    for i, s in enumerate(list):
        c = 0
        sh.write(i + 1, c, s['name'])
        c += 1
        sh.write(i + 1, c, s['code'])
        c += 1
        sh.write(i + 1, c, "%.2f" % s['price'])
        c += 1
        sh.write(i + 1, c, s['count'])
        c += 1
        score = 0
        if s.has_key('score'):
            score = s['score']
            pass
        sh.write(i + 1, c, score)
        c += 1
        sh.write(i + 1, c, "%.2f" % s['pe'])
        c += 1
        sh.write(i + 1, c, "%.2f" % s['pb'])
        c += 1
        r = 0
        if s.has_key('r'):
            r = s['r']
            pass
        sh.write(i + 1, c, "%.2f" % r)
        c += 1
        sh.write(i + 1, c, "%.3f" % s['r1'])
        c += 1
        sh.write(i + 1, c, "%.3f" % s['r3'])
        c += 1
        sh.write(i + 1, c, "%.3f" % s['r5'])
        c += 1
        roe2017 = 0
        if s.has_key('roe_2017_1'):
            roe2017 = s['roe_2017_1']
            pass
        sh.write(i + 1, c, "%.3f" % roe2017)
        c += 1

        if s.has_key('roe_2016_4'):
            roe2016 = s['roe_2016_4']
            pass
        else:
            roe2016 = s['roe2016']
            pass
        sh.write(i + 1, c, "%.3f" % roe2016)
        c += 1

        if s.has_key('roe_2015_4'):
            roe2015 = s['roe_2015_4']
            pass
        else:
            roe2015 = s['roe2015']
            pass
        sh.write(i + 1, c, "%.3f" % roe2015)
        c += 1

        if s.has_key('roe_2014_4'):
            roe2014 = s['roe_2014_4']
            pass
        else:
            roe2014 = s['roe2014']
            pass
        sh.write(i + 1, c, "%.3f" % roe2014)
        c += 1

        if s.has_key('roe_2013_4'):
            roe2013 = s['roe_2013_4']
            pass
        else:
            roe2013 = s['roe2013']
            pass
        sh.write(i + 1, c, "%.3f" % roe2013)
        c += 1

        if s.has_key('roe_2012_4'):
            roe2012 = s['roe_2012_4']
            pass
        else:
            roe2012 = s['roe2012']
            pass
        sh.write(i + 1, c, "%.3f" % roe2012)
        pass
    wb.save(file_name)
    pass


import codecs
import csv


def write_to_csv(list, file_name):
    csv_file = open(file_name, "wb")
    csv_file.write(codecs.BOM_UTF8)
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(
        ['code', 'name', 'price', 'count', 'score', 'pe', 'pb', 'r', 'r1', 'r3', 'r5', 'roe2017-1', 'roe2016',
         'roe2015',
         'roe2014',
         'roe2013', 'roe2012'])
    for i, s in enumerate(list):
        # print i, s
        csv_writer.writerow(
            ["A" + s['code'], s['name'], s['price'], s['count'], s['score'], s['pe'], s['pb'], "%.2f" % (s['r']),
             "%.2f" % s['r1'],
             "%.2f" % s['r3'], "%.2f" % s['r5'], s['roe_2017_1'],
             s['roe_2016_4'], s['roe_2015_4'], s['roe_2014_4'], s['roe_2013_4'], s['roe_2012_4']])
        pass
    pass


def getStock(stockMap, code):
    if stockMap.has_key(code):
        return stockMap[code]
        pass
    pass


def cmp1(o1, o2):
    if o1.has_key('score'):
        k1 = o1['score']
        k2 = o2['score']
        pass
    else:
        k1 = o1['count']
        k2 = o2['count']
        pass
    if (k2 - k1) == 0:
        return (int)(10000 * (o2['r1'] - o1['r1']))
    else:
        return k2 - k1
    pass


def write_selected_stocks_xls(selectedList, stockMap, fileName):
    selected_array = selectedList
    selected_list = []
    for selected in selected_array:
        s = getStock(stockMap, selected)
        if s:
            selected_list.append(s)
            pass
        pass
    selected_list = sorted(selected_list, cmp=cmp1)
    for i, s in enumerate(selected_list):
        print i, s
        pass

    # model.write_to_csv(selected_list, "select_" + now_time + ".csv")
    write_to_excel(selected_list, fileName)
    pass
