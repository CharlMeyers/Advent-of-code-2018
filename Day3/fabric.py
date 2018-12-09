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

def insertClaim(id, left, top, height, width):
	for row in fabric[top: top+height]:
		for column in range(left, left+width):
			if row[column] == '*':
				row[column] = id
			else:
				row[column] = 'X'

def findClaim(claimId):
	claim = ""
	for line in fileContent:
		if line.find("#" + claimId) > -1:
			claim = line
			break

	return claim

def countOverlappingClaims():
	overlapCount = 0
	for row in fabric:
		for column in row:
			if column == 'X':
				overlapCount += 1

	return overlapCount

def compareSquareInchesToClaim(claimId):
	claim = findClaim(claimId)
	left = int(claim[claim.find('@') + 1:claim.find(',')].strip())
	top = int(claim[claim.find(',') + 1:claim.find(':')].strip())
	width = int(claim[claim.find(':') + 1:claim.find('x')].strip())
	height = int(claim[claim.find('x') + 1:].strip())
	count = 0

	for row in fabric[top: top + height]:
		for column in range(left, left + width):
			if row[column] == claimId:
				count += 1

	return count == width * height

def findIntactClaim():
	foundClaims = []
	claimId = ""

	for row in fabric:
		for column in row:
			if column != '*' and column != 'X' and foundClaims.count(column) == 0:
				foundClaims.append(column)
				if compareSquareInchesToClaim(column):
					claimId = column
					break

	return claimId

def readClaims(filename):
	with open(filename, "r") as file:
		global fileContent
		fileContent = file.read().splitlines()

	for line in fileContent:
		claimId = line[line.find("#")+1:line.find('@')].strip()
		leftPosition = int(line[line.find('@')+1:line.find(',')].strip())
		topPosition = int(line[line.find(',')+1:line.find(':')].strip())
		width = int(line[line.find(':')+1:line.find('x')].strip())
		height = int(line[line.find('x')+1:].strip())

		insertClaim(claimId, leftPosition, topPosition, height, width)