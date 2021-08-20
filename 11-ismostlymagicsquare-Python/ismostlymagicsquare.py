# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.
def row(a):
	sum1=sum(a[0])
	# print("rowww",sum1)
	for i in a:
		if(sum(i)!=sum1):
			# print("rowww",sum(i))
			return False
	return True

def col(a):
	sum1=sum(a[0])
	
	for i in range(len(a)):
		sum2=0
		for j in range(len(a[i])):
			sum2=sum2+a[i][j]
			# print(sum2)
		if(sum2!=sum1):
			# print(sum2)
			return False
	return True

def diag(a):
	sum1=sum(a[0])
	sum2=0
	for i in range(len(a)):
		for j in range(len(a[i])):
			if(i==j):
				sum2=sum2+a[i][j]
	if(sum2!=sum1):
		return False
	return True


def ismostlymagicsquare(a):
	# Your code goes here
	# print(a[1])
	# x=0
	# if(sum(a[x])==sum(a[]))
	# if()
	print(row(a))
	print(col(a))
	print(diag(a))
	if(row(a) == True and col(a) == True and diag(a)== True):
		return True
	else:
		return False


	# pass
print(ismostlymagicsquare([[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12],[4, 15, 14, 1]]))