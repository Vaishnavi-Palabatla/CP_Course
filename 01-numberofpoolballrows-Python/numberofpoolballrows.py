# Pool balls are arranged in balls where the first row contains 1 pool ball and each row contains 1
# more pool ball than the previous row. 
# numberOfPoolBallRows(balls) that takes a non-negative int number of pool balls, and returns the 
# smallest int number of balls required for the given number of pool balls. Thus, numberOfPoolBallRows(6) 
# returns 3. Note that if any balls must be in a row, then you count that row, and so 
# numberOfPoolBallRows(7) returns 4 (since the 4th row must have a single ball in it).

def fun_numberofpoolballrows(balls):
	l=[]
	c1=0
	c2=0
	for i in range(0,balls):
		# for j in range(i+1):
		j=i+1
		c1=c1+j
		c3=c1+j+1
		c2=c2+1
		# print("...",c1)
		# print("",c3)
		if(c1==balls):
			return c2
		elif(c1<balls and c3>balls):
			# print(c1)
			# print(c2)
			return c2+1
			# l.append(x)
		

	# return 0
print(fun_numberofpoolballrows(28))
