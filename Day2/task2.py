def findAndRemoveUncommenCharacter(string1, string2):
	differenceCount = 0
	indexToRemove = -1
	result = ""

	if len(string1) == len(string2):
		for i in range(len(string1)):
			if string1[i] != string2[i]:
				differenceCount += 1
				indexToRemove = i

	if differenceCount == 1:
		result = string1[:indexToRemove] + string1[indexToRemove+1:]

	return result

def findCharacterDifferenceAmount():
	fileContent = []
	with open("input.txt", "r") as file:
		fileContent = file.read().splitlines()

	for i in range(len(fileContent)):
		if i + 1 < len(fileContent):
			for j in range(i + 1, len(fileContent)):
				newString = findAndRemoveUncommenCharacter(fileContent[i], fileContent[j])
				if newString:
					print(newString)
					break

findCharacterDifferenceAmount()