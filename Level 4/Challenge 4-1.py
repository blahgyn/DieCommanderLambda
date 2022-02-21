import copy

# get the limit that the room can move
def checkRoomLimit(line):
	total = 0
	for i in line:
		total += i
	return total

# move all bunies to its next rooms
def addFullCapacityToTotalPerLine(path, line):
	for n in range(len(path[line])):
		if n in totalPerLine:
			totalPerLine[n] += path[line][n]
		else:
			totalPerLine[n] = path[line][n]
			
# dictionary to hold how many rabits has moved to a room
totalPerLine = {}

def solution(entrance, exit, path):
    
	for line in range(len(path)):
		# entrance will always send full capacity
		if line in entrance:
			addFullCapacityToTotalPerLine(path, line)
		# If is not entry
		else:
			# If the amount of rabits is bigger or equal the movement limit, send all 
			# /TODO (we could also check if there is only one corridor)
			if line in totalPerLine:
				limitRoom = checkRoomLimit(path[line])
				if totalPerLine[line] >= limitRoom:
					addFullCapacityToTotalPerLine(path, line)
				else:
					# Loop in the elements of the line
					for n in range(len(path[line])):
						# Find corridors
						if path[line][n] > 0:
							# Check if its exit, we just send there
							if n in exit:
								# if this corridor can send all to exit, send it
								if path[line][n] >= totalPerLine[line]:
									if n in totalPerLine:
										totalPerLine[n] += totalPerLine[line]
									else:
										totalPerLine[n] = totalPerLine[line]
								# else we send its limit, and remove from
								else:
									if n in totalPerLine:
										totalPerLine[n] += path[line][n]
										totalPerLine[line] -= path[line][n]
									else:
										totalPerLine[n] = totalPerLine[line]
										totalPerLine[line] -= path[line][n]
							# /TODO (looks like there is no need for this case)
				# 			else:
								# Get the room limit to send to
								# lim = checkRoomLimit(path[n])
								# if n in totalPerLine: 
								# 	tot = lim + totalPerLine[n]

	totalInExit = 0
	for i in exit:
		totalInExit += totalPerLine[i]

	return totalInExit


# Test 1
print(solution({0,1}, {4,5}, [[0,0,4,6,0,0],[0,0,5,2,0,0], [0,0,0,0,4,4], [0,0,0,0,6,6], [0,0,0,0,0,0], [0,0,0,0,0,0]]))

# Test 2
totalPerLine = {} # restarting values
print(solution({0}, {3}, [[0,7,0,0],[0,0,6,0],[0,0,0,8],[9,0,0,0]]))