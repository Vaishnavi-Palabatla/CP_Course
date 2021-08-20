# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	j=0
	count=0
	n=str(abs(n))
	for i in range(len(n)):
		
		if(n[i] ==j):
			return True
		j=n[i]
	return False

print(hasconsecutivedigits(5231123123123))



	# pass