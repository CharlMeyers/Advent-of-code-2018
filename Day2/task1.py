two = 0
three = 0

with open("input.txt", "r") as file:
	results = file.read().splitlines()
	for line in results:
		uniqueCharacters = list(set(line))
		twoCharactersHasBeenCounted = False
		threeCharactersHasBeenCounted = False

		for character in uniqueCharacters:
			countCharacters = line.count(character)
			if not twoCharactersHasBeenCounted and countCharacters == 2:
				two += 1
				twoCharactersHasBeenCounted = True

			if not threeCharactersHasBeenCounted and countCharacters == 3:
				three += 1
				threeCharactersHasBeenCounted = True

print("Two: {}, Three: {}".format(two, three))
print("Final result: {}".format(two * three))
