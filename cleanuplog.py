__author__ = 'hogenj'

import csv

input = 'fallfoliage.csv'
output = 'cleanlog.csv'
out = open(output, 'wb')
writer = csv.writer(out, dialect=csv.excel)

with open(input, 'rU') as csvfile:
    data = csv.reader(csvfile, dialect=csv.excel)
    lastrow = None
    for row in data:
        if row == lastrow:
            continue
        else:
            lastrow = row
        date = row[0]
        call = row[1]
        freq = row[2]
        writer.writerow([date, call.upper(), freq])

out.close()

