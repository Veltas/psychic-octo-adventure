#Small python script which produces a geographically accurate
#map of LAN, with a small table allocated to each person

import urllib2

#get the data
raw = urllib2.urlopen("http://www.uwcs.co.uk/events/seating/1560/")
source = raw.read()

source = source.splitlines(True)

col = -1
output1 = ""
tables = 1
table2 = '<table id="table2"><tr>'
table3 = '<table id="table3"><tr>'
last = ""
finished = False
count = 0

#open file for writing
f = open('output.html', 'w')
f.write('<table id="table1">\n<tr>\n')

for line in source:
	if line.find("seating seating") != -1:
		#start of important data
		if line.find('col0') != -1:
			col = 0
		elif line.find("</td>"):
			tables = tables + 1
			#treating the situation different depending on the alignment of the
			#table in question
			if tables < 3 or tables > 6:
				if finished == False:
					f.write('</tr>\n<tr>\n')
			if tables == 3:
				f.write('</table>\n')
				finished = True
			if tables == 6:
				f.write(table2 + '\n')
				f.write('</tr></table>')
				f.write(table3 + '\n')
				f.write('</tr></table>')
				f.write('<table id="table4">')
			if tables == 8:
				f.write('</table>')
				
	if col == 0:
		#the data we want
		if line.find("title") != -1:
			output1 = line

	if output1 != "":
		if tables < 8:
			current = '<td title="' + output1[27:-2] + "\">" + "<table class='small'><tr><td class='one'><td class='two'></tr><tr><td class='three'><td class='four'></tr></table></td>\n"
			if tables < 3 or tables > 6:
				f.write('<td title="' + output1[27:-2] + "\">" + "<table class='small'><tr><td class='one'><td class='two'></tr><tr><td class='three'><td class='four'></tr></table></td>\n")
				output1 = ""
				finished = False
			elif tables < 5 and current != last:
				if count == 2:
					f.write('</tr><tr>')
					count = 0
				table2 = table2 + current
				last = current
				count = count + 1
				finished = False
			elif current != last:
				if count == 2:
					f.write('</tr><tr>')
					count = 0
				table3 = table3 + current
				last = current
				finished = False
				count = count + 1

	

