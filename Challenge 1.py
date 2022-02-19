
def solution(s):

	seqStart = 0 # index where the sequence to check start
	seqSize = 1 # size of the sequence to check
	numberOfSlices = 0;

	while seqSize + seqStart <= len(s):

		if (seqSize + seqStart > len(s)):
			numberOfSlices = 1
			return numberOfSlices

		if (s[seqStart:seqStart+seqSize] != s[seqSize:seqSize+seqSize]):
			seqSize = seqSize + 1
			seqStart = 0
			numberOfSlices = 0
			continue
		else:
			seqStart = seqStart + seqSize
			numberOfSlices = numberOfSlices + 1
			continue

	if (len(s) % numberOfSlices != 0):
		numberOfSlices = 1
		return numberOfSlices

	if (numberOfSlices == 0):
		return 1
	
	return numberOfSlices



# ==========

# s = "abcabcabcabc" # Test 1: answer is 4
s = "abccbaabccba" # Test 2: answer is 2

print(solution(s))