import xlwt


def write_to_excel(list, file_name):
    wb = xlwt.Workbook(encoding='utf-8')
    sh = wb.add_sheet("a")
    sh.write(0, 0, 'code')
    sh.write(0, 1, 'name')
    sh.write(0, 2, 'count')
    sh.write(0, 3, 'score')
    sh.write(0, 4, 'pe')
    sh.write(0, 5, 'pb')
    sh.write(0, 6, 'r')
    sh.write(0, 7, 'r1')
    sh.write(0, 8, 'r3')
    sh.write(0, 9, 'r5')
    sh.write(0, 10, 'roe_2017_1')
    sh.write(0, 11, 'roe_2016_4')
    sh.write(0, 12, 'roe_2015_4')
    sh.write(0, 13, 'roe_2014_4')
    sh.write(0, 14, 'roe_2013_4')
    sh.write(0, 15, 'roe_2012_4')
    for i, s in enumerate(list):
        sh.write(i + 1, 0, s['code'])
        sh.write(i + 1, 1, s['name'])
        sh.write(i + 1, 2, s['count'])
        sh.write(i + 1, 3, s['score'])
        sh.write(i + 1, 4, s['pe'])
        sh.write(i + 1, 5, s['pb'])
        sh.write(i + 1, 6, "%.2f" % s['r'])
        sh.write(i + 1, 7, "%.2f" % s['r1'])
        sh.write(i + 1, 8, "%.2f" % s['r3'])
        sh.write(i + 1, 9, "%.2f" % s['r5'])
        sh.write(i + 1, 10, s['roe_2017_1'])
        sh.write(i + 1, 11, s['roe_2016_4'])
        sh.write(i + 1, 12, s['roe_2015_4'])
        sh.write(i + 1, 13, s['roe_2014_4'])
        sh.write(i + 1, 14, s['roe_2013_4'])
        sh.write(i + 1, 15, s['roe_2012_4'])
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
        ['code', 'name', 'count', 'score', 'pe', 'pb', 'r', 'r1', 'r3', 'r5', 'roe2017-1', 'roe2016', 'roe2015',
         'roe2014',
         'roe2013', 'roe2012'])
    for i, s in enumerate(list):
        # print i, s
        csv_writer.writerow(
            ["A" + s['code'], s['name'], s['count'], s['score'], s['pe'], s['pb'], "%.2f" % (s['r']), "%.2f" % s['r1'],
             "%.2f" % s['r3'], "%.2f" % s['r5'], s['roe_2017_1'],
             s['roe_2016_4'], s['roe_2015_4'], s['roe_2014_4'], s['roe_2013_4'], s['roe_2012_4']])
        pass
    pass
