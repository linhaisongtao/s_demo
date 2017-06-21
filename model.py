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
        sh.write(i + 1, c, "%.2f"%s['price'])
        c += 1
        sh.write(i + 1, c, s['count'])
        c += 1
        sh.write(i + 1, c, s['score'])
        c += 1
        sh.write(i + 1, c, s['pe'])
        c += 1
        sh.write(i + 1, c, s['pb'])
        c += 1
        sh.write(i + 1, c, "%.2f" % s['r'])
        c += 1
        sh.write(i + 1, c, "%.2f" % s['r1'])
        c += 1
        sh.write(i + 1, c, "%.2f" % s['r3'])
        c += 1
        sh.write(i + 1, c, "%.2f" % s['r5'])
        c += 1
        sh.write(i + 1, c, s['roe_2017_1'])
        c += 1
        sh.write(i + 1, c, s['roe_2016_4'])
        c += 1
        sh.write(i + 1, c, s['roe_2015_4'])
        c += 1
        sh.write(i + 1, c, s['roe_2014_4'])
        c += 1
        sh.write(i + 1, c, s['roe_2013_4'])
        c += 1
        sh.write(i + 1, c, s['roe_2012_4'])
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
