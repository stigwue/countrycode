#!/usr/bin/env python

#function to write data to file
def write_to_file(filename, line):
    f = open(filename, 'ab')
    #open(filename, 'ab')

    f.write(line)
    f.write('\n')
    f.close()
    return

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
		print '"%s",%s,%s,%s,%s' % (col0, col1, col2, col3, col4)

		#send to csv output
		write_to_file('output/csv.csv', '%s,%s,%s,%s,%s' % (col0, col1, col2, col3, col4))


#get col 5 from
#https://github.com/mhs/world-currencies/blob/master/currencies.json
#or
#http://fx.sauder.ubc.ca/currency_table.html
# import json
# f = open('input/currencies.json', 'rb')
# json_string = ''
# line = f.readline()
# while line != '':
# 	json_string = json_string + line

# 	line = f.readline()

# currencies = json.loads(json_string) #cc/currency code, symbol, name
# for currency in currencies:
# 	print currency['cc'], currency['symbol'] #, currency['name']

# 	#send to csv output
# 	try:
#    		write_to_file('output/cc.csv', '%s,%s' % (currency['cc'], currency['symbol']))
#    	except:
#    		write_to_file('output/cc.csv', '%s,%s' % (currency['cc'], currency['symbol'].encode('utf-8').strip()))
	
	#write_to_file('output/cc.csv', '%s,%s' % (currency['cc'], u''.join(('',currency['symbol'])).encode('utf-8').strip()))
	#write_to_file('output/cc.csv', '%s,%s' % (currency['cc'], currency['symbol'].encode("ascii", "ignore").strip()))
	#write_to_file('output/cc.csv', '%s,%s' % (currency['cc'], currency['symbol'].encode("ascii").strip()))

	#write_to_file('output/cc.csv', '%s,%s' % (currency['cc'], unicode(currency['symbol'])))

