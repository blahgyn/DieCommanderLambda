import copy

class Node:

	def __init__(self, positionX, positionY, value, isEnd, h):
		self.positionX = positionX
		self.positionY = positionY
		self.value = value
		self.isEnd = isEnd
		self.h = h
		self.g = 0
		self.f = self.g + self.h
		self.neighbors = []
		self.parentNode = None

	# A wall is removable only if two or more neighbors are "walkable"
	def checkIfRemovableWall(self):
		if self.value == 0:
			return False
		nWalls = 0
		for n in self.neighbors:
			if n.value == 0:
				nWalls = nWalls + 1
		if nWalls > 1:
			return True
		return False


class Grid:

	def __init__(self, map):
		isEnd = False
		self.map = map
		self.grid = []

		# Transforming the map into Node objects
		for r in range(len(self.map)):
			# create a row
			row = []
			for c in range(len(self.map[r])):
			# Check if is End node (0,0)
				if r == len(self.map)-1 and c == len(self.map[r])-1:
					isEnd = True
			# Calculate h
				h = abs(len(self.map)-1 - c) + abs(len(self.map[r])-1 - r) + 1
			# Create Node object
				node = Node(c, r, self.map[r][c],  isEnd, h)
				row.append(node)

			self.grid.append(row)

		for row in self.grid:
			for n in row:
				self.setNeighbors(n)

	def setNeighbors(self, node):

		if (node.positionX < len(self.grid[0])-1):
			node.neighbors.append(self.grid[node.positionY][node.positionX+1])

		if (node.positionX > 0):
			node.neighbors.append(self.grid[node.positionY][node.positionX-1])
			
		if (node.positionY < len(self.grid)-1):
			node.neighbors.append(self.grid[node.positionY+1][node.positionX])

		if (node.positionY > 0):
			node.neighbors.append(self.grid[node.positionY-1][node.positionX])
			
	# Function to restart the G values of nodes
	def restartGrid(self):
	    for n in self.grid:
	        for node in n:
	            node.g = 0


def CalculatePathUsingAStar(gridToCheck, minimumDistance, openSet, closeSet):

	startingNode = gridToCheck.grid[0][0]
	openSet.append(startingNode)

	while len(openSet) > 0:
		# Looking for the best node index in the openSet to check
		lowestValue = float('inf')
		for n in range(len(openSet)):
			if openSet[n].f < lowestValue:
				lowestValue = openSet[n].f
				bestNodeIndex = n

		# If this is the end, we'r done
		if openSet[bestNodeIndex].isEnd == True:
			nodeAux = openSet[bestNodeIndex]
			totalDistance = 0
			while nodeAux is not None:
				nodeAux = nodeAux.parentNode
				totalDistance += 1
			return totalDistance

		# Check current node
		currentNode = openSet[bestNodeIndex]

		closeSet.append(currentNode)
		openSet.remove(currentNode)

		for currentNeighbor in currentNode.neighbors:
			if currentNeighbor.value == 1:
				continue
			if currentNeighbor not in closeSet:
			 	tempG = currentNode.g + 1
			 	if currentNeighbor in openSet:
			 		if tempG < currentNeighbor.g:
			 			currentNeighbor.g = tempG
			 	else:
			 		currentNeighbor.g = tempG
			 		openSet.append(currentNeighbor)

			 	currentNeighbor.f = currentNeighbor.g + currentNeighbor.h
			 	currentNeighbor.parentNode = currentNode

	return False


def solution(map):

	openSet = []
	closeSet = []

	minimumDistance = float('inf')

	g = Grid(map)

	# Create possible grid-scenarios with one wall removed
	listOfGrids = []
	listOfGrids.append(g)

	for row in g.grid:
		for r in row:
			if (r.checkIfRemovableWall()):	    
				deepCopy = copy.deepcopy(g.map)
				deepCopy[r.positionY][r.positionX] = 0
				newGrid = Grid(deepCopy)
				listOfGrids.append(newGrid)

	for gridToCheck in listOfGrids:
		minDistance = CalculatePathUsingAStar(gridToCheck, minimumDistance, copy.deepcopy(openSet), copy.deepcopy(closeSet))
		gridToCheck.restartGrid()
		if minDistance == False:
			continue
		if minDistance < minimumDistance:
			minimumDistance = minDistance

	return minimumDistance

# Test 1
print(solution([[0,1,1,0], [0,0,0,1], [1,1,0,0], [1,1,1,0]]))

# Test 2
print(solution([[0,0,0,0,0,0], [1,1,1,1,1,0], [0,0,0,0,0,0], [0,1,1,1,1,1], [0,1,1,1,1,1], [0,0,0,0,0,0]]))