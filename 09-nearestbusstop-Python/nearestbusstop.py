# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
	
	if(street%8==0):
		return street
	else:
		y=street%8
		x=street/8
		if(street%8<=4):
			# print((round(x)-1)*8)
			return street-y
		
		else:
			return street-y+8
	# return -1
