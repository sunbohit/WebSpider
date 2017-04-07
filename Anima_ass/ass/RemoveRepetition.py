input_file = './ar_url.txt'
output_file = './url.txt'

infile = open(input_file,'r')
outfile = open(output_file,'a')

urlset = set()
for line in infile.readlines():
	line = line.strip()
	urlset.add(line)
print(len(urlset))
for line in urlset:
	outfile.write(line+'\n')

infile.close()
outfile.close()
