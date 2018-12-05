output = 0
results = []

with open("input.txt", "r") as file:
	output = int(file.readline())
	while output not in results:
		results.append(output)
		line = file.readline()
		if line == '':
			print('resetting file')
			file.seek(0)
			line = file.readline()
		output = output + int(line)

print(output)

