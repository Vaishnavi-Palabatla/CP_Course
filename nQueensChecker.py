def canqueenattack(qR, qC, oR, oC):
	if (qR-oR) == 0 or (qC-oC) == 0 or abs(qR-qC) == abs(oR-oC):
		return True
	return False

def nQueensChecker(a):
    # Your code goes here...
    if len(a)!=len(a[0]):
        return False
    queenpositions = [(i,j) for i in range(len(a)) for j in range(len(a[0])) if a[i][j]]
    if len(a)!= len(queenpositions):
        return False
    for i in range(len(queenpositions)):
        for j in range(i+1,len(queenpositions)):
            qr1,qc1 = queenpositions[i]
            qr2,qc2 = queenpositions[j]
            if canqueenattack(qr1,qc1,qr2,qc2):
                return False
    return True

assert nQueensChecker([[False,False,False,True],[True,False,False,False],[False,False,True,False],[False,True,False,False]])==True
assert nQueensChecker([[True,False,False,False],[True,False,False,False],[False,False,True,False],[False,True,False,False]])==False
assert nQueensChecker([[False,True,False,False],[True,False,False,False],[False,False,True,False],[False,True,False,False]])==False
assert nQueensChecker([[False,False,False,False],[True,False,False,False],[False,False,True,False],[False,True,False,False]])==False
assert nQueensChecker([[False,False,False,False],[True,False,False,False],[False,False,True,False]])==False
print("All testcases passed")