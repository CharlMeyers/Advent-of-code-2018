import fabric

fabric.initFabric(1000,1000)
fabric.readClaims("input.txt")

# printFabric()
print(fabric.countOverlappingClaims())