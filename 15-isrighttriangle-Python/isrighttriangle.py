# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import math
def distance(a,b,c,d):
	x=((a-c)**2+(b-d)**2)**0.5
	return x

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	
	p=math.sqrt(((x2-x1)**2 +(y2-y1)**2)+((x3-x2)**2 +(y3-y2)**2))
	q=math.sqrt(((x1-x3)**2)+((y1-y3)**2))
	print(p,q)
	if(p==q):
		return True
	elif((math.sqrt(((x3-x1)**2 +(y3-y1)**2)+((x3-x2)**2 +(y3-y2)**2))==math.sqrt(((x1-x2)**2)+((y1-y2)**2)))):
		return True

	else:
		return False
	