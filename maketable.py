__author__ = 'hogenj'

import csv
import re

input = 'fallfoliagefinal.csv'
basefile = ':uploads:beford-fall-foliage-certificate_{0}.pdf'

with open(input, 'rU') as csvfile:
    data = csv.reader(csvfile, dialect=csv.excel)
    for row in data:
        call = row[1]
        lcall = call.lower()
        if lcall == 'call':
            continue

        fcall = re.sub('[!@#$/]', '_', lcall)

        link = basefile.format(fcall)

        # {{:uploads:beford-fall-foliage-certificate_aa1lh.pdf|aa1lh}}
        print '| {{{{ {0}|{1} }}}} | {2} | {3} Mhz |'.format(link, lcall, row[0], row[2])

