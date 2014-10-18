__author__ = 'hogenj'

import csv
import re

input = 'fallfoliagefinal.csv'
basefile = 'output/beford-fall-foliage-certificate_{0}.pdf'

with open(input, 'rU') as csvfile:
    data = csv.reader(csvfile, dialect=csv.excel)
    count = 0
    for row in data:
        call = row[1]
        lcall = call.lower()
        if lcall == 'call':
            continue

        lcall = re.sub('[!@#$/]', '_', lcall)

        old = basefile.format(count)
        new = basefile.format(lcall)

        print "mv {0} {1}\n".format(old, new)
        count += 1
