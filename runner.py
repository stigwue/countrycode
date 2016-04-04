#!/usr/bin/env python

#function to write data to file
def write_to_file(filename, line):
    f = open(filename, 'a')

    f.write(line)
    f.write('\n')
    f.close()
    return

f = open('raw_code.html', 'r')
line = f.readline()

while line != '':
	#<option data-countryCode="AE" value="+971">United Arab Emirates (+971)</option>

	part = line.split(' ') #<option data-countryCode="ES" value="+34">Spain (+34)</option>
	#part[1]: data-countryCode="ES"
	#part[2]: value="+34">Spain

	#ES
	country_code_alpha = part[1].split('=')[1]
	
	country_code = part[2].split('>')
	

	#Spain
	#country = country_code[1]

	#country_code: value="+34"
	country_code_int = country_code[0].split('=')[1]
	
	#print country_code_int, country, country_code_alpha
	print country_code_int, country_code_alpha
	write_to_file('country_code.csv', '%s, "%s"' % (country_code_int, country_code_alpha))

	line = f.readline()

	#strip quotes from country_code_alpha

f.close()