from itertools import combinations
from collections import Counter
singlePatternFile = open('patterns1.txt')
allFile = open('categories.txt')

a = frozenset(['a'])
b = frozenset(['b'])
c = frozenset(['c'])
s= set()
s.add(c)
s.add(b)
s.add(a)

def read_singlepattern(inputData):
	singlepattern = {}
	for line in inputData:
		line = line.rstrip().split(':')
		word = frozenset([line[1]])
		singlepattern[word] = line[0]
	return singlepattern

def detect_length(inputData):
	k = 0
	for line in inputData:
		line = line.rstrip().split(';')
		n = len(line)
		if n > k:
			k = n
	return k

def generate_candidates(L, k):
    """Generate candidate set from `L` with size `k`"""
    candidate = {}
    if len(L) < k: return {}
    for a in L:
    	for b in L:
    		union = a | b
    		if len(union) == k and a != b:
    			candidate[union] = 0
                # if k==3: print union
                #if k==3: print candidates
    # if k==3: print candidate
    return candidate

def get_support(candidates,inputData,k):
	aaa = open('categories.txt')
	for line in aaa:
		line = line.rstrip().split(';')
		linekey = frozenset(line)
		for key in candidates:
			if key <=linekey:
				# print key,line
				candidates[key]+=1
	aaa.close()
	return candidates

def select_frequent(candidates,minsupport):
	setMap = {}
	for key in candidates:
		if candidates[key] > minsupport:
			setMap[key] = candidates[key]
	return setMap

def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z

def apriori_algorithms(maxlength,totalMap,i,minsupport):
	candidates = totalMap
	with open('patterns.txt', 'a') as file:
		while candidates:
			candidates = generate_candidates(candidates, i)
			# if i==2: print candidates
			candidates = get_support(candidates,allFile,i)
			# if i==2: print candidates
			candidates = select_frequent(candidates,minsupport)

			for key in candidates:
				out=str(candidates[key])+':'
				for word in key:
					out = out+str(word)+';'
				out = out[:len(out)-1] + '\n'
				print out
				file.writelines(out)

			i+=1



maxlength = detect_length(allFile)
totalMap = read_singlepattern(singlePatternFile)
i=2
minsupport = 771
final_map = apriori_algorithms(maxlength,totalMap,i,minsupport)
#print final_map
# candidates = generate_candidates(totalMap, i)
# candidates = get_support(candidates,allFile,i)
# candidates = select_frequent(candidates,minsupport)
# totalMap = totalMap.update(candidates)
# print totalMap






singlePatternFile.close()
allFile.close()



