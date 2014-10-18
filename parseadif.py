#!/usr/bin/env python

import cStringIO as StringIO
import adif
from decimal import Decimal
from datetime import datetime


filename = 'lloydfinal.adi'
data = open(filename, 'r+').read()

flo = StringIO.StringIO(data)
reader = adif.Reader(flo)
i = iter(reader)

for contact in i:
    if contact['band'] == '20M':
        freq = '14'
    elif contact['band'] == '40M':
        freq = '7'
    else:
        print contact['band']
    line = "{0},,{1},{2}".format(contact['app_datetime_on'], contact['call'], freq)
    print line