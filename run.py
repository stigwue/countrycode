#!/usr/bin/env python

#function to write data to file
def write_to_file(filename, line):
    f = open(filename, 'a')

    f.write(line)
    f.write('\n')
    f.close()
    return

from csv import reader


#parse into
#country_code, country name, currency, currency_code, symbol

#expected output for say, Nigeria, should be:
#      Nigeria, NG, 234, Naira, NGN, =N=
#cols: 0      , 1 , 2  , 3    , 4  ,  5

#get cols 0, 1, 2, 3 and 4 from
#https://github.com/datasets/country-codes/blob/master/data/country-codes.csv

import csv
with open('input/country-codes.csv', 'rb') as f:
	reader = csv.reader(f)
	col0 = ''
	col1 = ''
	col2 = ''
	col3 = ''
	col4 = ''
	for row in reader:
		col0 = row[0]
		col1 = row[2]
		col2 = row[9]
		col3 = row[14]
		col4 = row[17]
		#print row
		#print '%s,%s,%s,%s,%s' % (col0, col1, col2, col3, col4)

		#send to csv output
		write_to_file('output/new.csv', '%s,%s,%s,%s,%s' % (col0, col1, col2, col3, col4))


#get col 5 from
#https://github.com/mhs/world-currencies/blob/master/currencies.json
#or
#http://fx.sauder.ubc.ca/currency_table.html
