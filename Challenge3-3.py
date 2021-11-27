def solution(l):
    # parse to int
	l = int(l)
	# number of operations
	nOps = 0

	while l != 1:
	    # if its even, always divide
		if l % 2 == 0:
			l = int(l/2)
			nOps += 1
        # if its odd
		else:
		    # special rule for 3
			if l == 3:
				l = l-1
				nOps += 1
			# add/sub to the number that has more zeros right-to-left
			else:
				nOfZerosUp = 0
				for i in reversed(bin(l+1)[-2:]):
					if i == "0":
						nOfZerosUp += 1
					else:
						break
				nOfZerosDown = 0
				for i in reversed(bin(l-1)[-2:]):
					if i == "0":
						nOfZerosDown += 1
					else:
						break

				if nOfZerosUp > nOfZerosDown:
					l += 1
					nOps += 1
				else:
					l -= 1
					nOps += 1

	return nOps