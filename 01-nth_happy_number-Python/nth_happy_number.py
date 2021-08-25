# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)

def sod(n):
	sum=0
	while(n>0):
		rem=n%10
		n=n//10
		sum=sum+rem**2
	return sum

def ishappynumber(n):
	# your code goes here
	count=0
	x=0
	if(n<1):
		return False
	else:
		x=n
		while(True):
			x=sod(x)
			# print(x)
			
			if(len(str(x))==1):
				if(x==1):
					return True
				else:
					return False

def nth_happy_number(n):
	l=[]
	for i in range(1,n*5):
		print(i)
		if(ishappynumber(i)==True):
			
			l.append(i)
			
			if(len(l)==n):
				print(len(l),n)
				return l[-1]

	
print(nth_happy_number(7))