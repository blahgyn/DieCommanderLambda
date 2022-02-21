class Node:

	def __init__(self, value):
		self.value = value
		self.child = []
		self.child2 = []
		
def solution(l):

	nodesList = {}

	for index in range(len(l)):
		if not index in nodesList:
			currentNode = Node(l[index])
			nodesList[index] = currentNode
		else:
			currentNode = nodesList[index]
		for newIndex in range(index+1, len(l)):
			if l[newIndex] % l[index] == 0:
				if not newIndex in nodesList:
					node = Node(l[newIndex])
					nodesList[newIndex] = node
					currentNode.child.append(node)
				else:
					currentNode.child.append(nodesList[newIndex])

	nOfTuples = 0
	for keyIndex in nodesList:
		for child in nodesList[keyIndex].child:
			nOfTuples = nOfTuples + len(child.child)

	return nOfTuples

# =========

# Test 1
print(solution([1,1,1]))

# Test 2
print(solution([1,2,3,4,5,6]))