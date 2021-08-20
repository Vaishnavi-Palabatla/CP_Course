# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	x=len(str(digit))
	if(k>(x-1)):
		return 0
	else:
		if(k==0):
			# digit=digit//10**(k)
			digit1=abs(digit)%10**(k+1)
			print(digit1)
		else:

			digit=digit//10**(k)
			digit1=digit%10**(k)
			print(digit1)
	return digit1
print(fun_get_kth_digit(789,0))
