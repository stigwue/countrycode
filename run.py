#!/usr/bin/env python

#function to write data to file
def write_to_file(filename, line):
    f = open(filename, 'a')

    f.write(line)
    f.write('\n')
    f.close()
    return

#parse name_code.csv into
#country_code, country name, currency, currency_code, symbol

#expected output for say, Nigeria, should be:
#234, Nigeria, Naira, NGN, =N=
f = open('csv/name_code.csv', 'r')
#from
#http://data.okfn.org/data/core/country-list
#or
#https://github.com/datasets/country-list/blob/master/data.csv

#currencies from
#https://github.com/mhs/world-currencies/blob/master/currencies.json
#or
#http://fx.sauder.ubc.ca/currency_table.html
line = f.readline()

while line != '':
	parts = line.split(',')
	#get last part
	last_part = parts[len(parts) - 1]
	#remove the trailing endline in last_part
	last_part = last_part[:len(last_part) - 1]
	#all other parts
	other_parts = ''
	for splits in range(0, len(parts) - 1):
		other_parts = other_parts + parts[splits]
	#print last_part, other_parts
	print '%s, %s' % (last_part, other_parts)
	#send to csv output
	#write_to_file('output/new.csv', '%s, %s' % (last_part, other_parts))

	line = f.readline()

f.close()