# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs


def fun_eggcartons(eggs):
	# your code goes here
	eggs=abs(eggs)
	
	if(eggs<=12 and eggs>=1):
		return 1
	elif(eggs==0):
		return 0 

	elif(eggs%12==0):
		return eggs//12
	else:
		x=round(eggs//12)+1

		print(x)
		return x
