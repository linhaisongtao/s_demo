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
    sh.write(0, c, 'benefit')
    c += 1
    sh.write(0, c, 'pe')
    c += 1
    sh.write(0, c, 'pb')
    c += 1
    sh.write(0, c, 'r1')
    c += 1
    sh.write(0, c, 'r3')
    c += 1
    sh.write(0, c, 'r5')
    c += 1
    sh.write(0, c, 'roe2016')
    c += 1
    sh.write(0, c, 'roe2015')
    c += 1
    sh.write(0, c, 'roe2014')
    c += 1
    sh.write(0, c, 'roe2013')
    c += 1
    sh.write(0, c, 'roe2012')
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
        sh.write(i + 1, c, "%.2f%%" % (s['benefit'] * 100))
        c += 1
        sh.write(i + 1, c, "%.2f" % s['pe'])
        c += 1
        sh.write(i + 1, c, "%.2f" % s['pb'])
        c += 1
        sh.write(i + 1, c, "%.2f%%" % (s['r1'] * 100))
        c += 1
        sh.write(i + 1, c, "%.2f%%" % (s['r3'] * 100))
        c += 1
        sh.write(i + 1, c, "%.2f%%" % (s['r5'] * 100))
        c += 1
        sh.write(i + 1, c, "%.2f%%" % (s['roe2016'] * 100))
        c += 1
        sh.write(i + 1, c, "%.2f%%" % (s['roe2015'] * 100))
        c += 1
        sh.write(i + 1, c, "%.2f%%" % (s['roe2014'] * 100))
        c += 1
        sh.write(i + 1, c, "%.2f%%" % (s['roe2013'] * 100))
        c += 1
        sh.write(i + 1, c, "%.2f%%" % (s['roe2012'] * 100))
        pass
    wb.save(file_name)
    pass
