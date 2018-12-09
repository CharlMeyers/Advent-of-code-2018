fileContent = []
fabric = []

def initFabric(height, width):
	for row in range(height):
		fabricRow = []
		for column in range(width):
			fabricRow.append('*')
		fabric.append(fabricRow)

def printFabric():
	for row in fabric:
		for column in row:
			print(column, end = " ")
		print()

def countOverlappingClaims():
	overlapCount = 0
	for row in fabric:
		for column in row:
			if column == 'X':
				overlapCount += 1

	return overlapCount

def insertClaim(id, left, top, height, width):
	for row in fabric[top: top+height]:
		for column in range(left, left+width):
			if row[column] == '*':
				row[column] = id
			else:
				row[column] = 'X'

def readClaims():
	with open("input.txt", "r") as file:
		fileContent = file.read().splitlines()

	for line in fileContent:
		claimId = line[1:line.find('@')].strip()#we know the input always starts with '#'
		leftPosition = int(line[line.find('@')+1:line.find(',')].strip())
		topPosition = int(line[line.find(',')+1:line.find(':')].strip())
		width = int(line[line.find(':')+1:line.find('x')].strip())
		height = int(line[line.find('x')+1:].strip())

		insertClaim(claimId, leftPosition, topPosition, height, width)

initFabric(1000,1000)
readClaims()

# printFabric()
print(countOverlappingClaims())