# Write the function lookAndSay(a) that takes a list of numbers and returns a list of numbers
# that results from "reading off" the initial list using the look-and-say method, using tuples 
# for each (count, value) pair.
# 
# For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]
def lookandsay(a):
    # your code goes here
	b=[]
	c=[]
	j=0
	count=1
	if(len(a)==0):
		return b
	for i in a:
		if(i!=j):
			b.append((count,j))
			j=i
			count=1
		else:
			count=count+1
	print(i,j,count)
	b.append((count,i))
	return b[1:]

# def lookandsay(a):
# 	# Your code goes here
# 	# l=[]
# 	d={}
# 	# for i in range(len(a)):
# 	# 	if i not in l:
# 	# 		l.append(i)
# 	# for i in l:
# 	# 	d[i]=a.count(i)
	
# 	for i in range(len(a)):
# 		count=0
# 		d[i]=count
# 		for j in range(i+1,len(a)):
# 			if(a[i]==a[j]):
# 				# count=count+1
# 				x=a[i]
# 				print(d)
# 				d[a[i]]=d[x]+1
				
# 			else:
# 				# d[a[i]]=count
# 				break

# 	print(d)
print(lookandsay([3,3,8,3,3,3,3]))
	# pass