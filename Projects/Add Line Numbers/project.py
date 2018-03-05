infile = input('What file do you want to open? ')
infile = open(infile, 'r+')
outfile = input('What do you want to call the output file? ')
outfile = open(outfile, 'w')

line = 1
for i in infile:
	outfile.write(str(line) + ' - ' + i)
	line+=1