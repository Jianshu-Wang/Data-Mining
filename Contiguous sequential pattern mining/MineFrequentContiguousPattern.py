originalFile = open('reviews_sample.txt')
fout = open('patterns.txt','w')
singlePatterns={}
final_result={}
def read_singlepattern(file):
	singleCandidate = {}
	for line in file:
		for word in line.rstrip().split(' '):
			if word not in singleCandidate: 
				singleCandidate[word] = 0
	# print singleCandidate
	# print 'walking' in singleCandidate
	return singleCandidate

def generate_candidates(previous_map):
	candidate_map = {}
	for key1 in previous_map:
		for key2 in singlePatterns:
			new_key = key1+' '+key2
			candidate_map[new_key] = 0
	# candidate_map = {}
	# for line in bbb:
	# 	t+=1
	# 	print t
	# 	for key in previous_map:
	# 		# print 3
	# 		if key in line.strip():
	# 			# print 4
	# 			word_list = [n for n in xrange(len(line)) if line.find(key, n) == n]
	# 			for index in word_list:
	# 				s = line[index:]
	# 				next_word= s.split(key,1)[1].strip().split(' ')[0]
	# 				if next_word in singlePatterns and next_word is not '':
	# 					new_key = key+' '+next_word
	# 					candidate_map[new_key] = 0
	return candidate_map

def check_result(pattern_sequence):
	for key in pattern_sequence:
		if pattern_sequence[key]>100:
			list1 = key.split(' ')
			out = str(pattern_sequence[key])+':'+ ';'.join(list1) + '\n'
			fout.write(out)
			print out

def get_support(candidate,length):
	aaa = open('reviews_sample.txt')
	for line in aaa:
		li = extract_list(line.strip(),length)
		su = {}
		for word in li:
			if word in candidate and word not in su:
				candidate[word]+=1
				su[word] = 0
	aaa.close()
	return candidate

def extract_list(line,length):
	word_list = line.split(' ')
	key_list = []
	i = 0
	while i+length<=len(word_list):
		key_list.append(" ".join(word_list[i:i+length]))
		i+=1

	return key_list

def find_frequent(candidate):
	candidate_result={}
	for key in candidate:
		if candidate[key]>=100:
			candidate_result[key] = candidate[key]
	return candidate_result

# t=0
# for line in originalFile:
# 	t+=1
# 	print t
# 	if "walking" in line:
# 		print 'yy'


sss = read_singlepattern(originalFile)
# print sss
# print 'walking' in sss
sss = get_support(sss,1)
# print sss
singlePatterns = find_frequent(sss)
print singlePatterns
length = 2
candidate = singlePatterns
final_result.update(candidate)
while candidate:
	final_result.update(candidate)
	print length
	candidate = generate_candidates(candidate)
	# print candidate
	candidate = get_support(candidate,length)
	# print candidate
	candidate = find_frequent(candidate)
	length+=1
	print candidate
	
# print final_result

check_result(final_result)





# print ans
# check_result(ans)



# This function extracts fixed length substring list from each line
# def extract_substring(result,len):


minsupport = 100
len = 2

fout.close()
originalFile.close()