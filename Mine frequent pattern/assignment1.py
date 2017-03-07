file = open('categories.txt')
fout = open('patterns.txt','w')
patterns={}
for line in file:
	for word in line.rstrip().split(';'):
		if word not in patterns: patterns[word] = 1
		else: patterns[word] += 1

for key in patterns:
	if patterns[key]>771:
		out = str(patterns[key])+':'+key+'\n'
		fout.write(out)
		print out 


fout.close()
file.close()