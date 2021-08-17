# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	n=str(n)
	l=[]
	for i in n:
		if(i not in l):
			l.append(i)
	l.sort()
	d={}
	for i in l:
		d[i]=n.count(i)
	y=sorted(d.items(), key=lambda x:(x[1]), reverse=True)
	print(y)
	return int(y[0][0])
print(mostfrequentdigit(5312312355565))	