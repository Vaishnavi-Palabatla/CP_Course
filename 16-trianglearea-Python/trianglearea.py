# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.

import math
def trianglearea(s1, s2, s3):
	# your code goes here
	x=((s1+s2+s3)/2)
	print(s1,s2,s3,x)
	a=abs(x-s1)
	b=abs(x-s2)
	c=abs(x-s3)
	y=math.sqrt(x*a*b*c)
	print(y)
	return y
	# pass
