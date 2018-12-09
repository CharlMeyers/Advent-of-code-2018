import fabric

fabric.initFabric(1000,1000)
fabric.readClaims()

# printFabric()
print(fabric.countOverlappingClaims())