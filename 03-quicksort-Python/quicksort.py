"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
# def quicksort(array):
# 	# Your code goes here
# 	l=0
# 	h=len(array)-1
# 	qs(array,l,h)

# 	pass
# def swap(array,x,y):
# 	temp=array[x]
# 	array[x]=array[y]
# 	array[y]=temp
# 	return array
# def partition(array,l,h):
	
# 	p=array[0]

# 	while(l<h):
# 		while(array[h]>p):
# 			h=h+1
# 		while(array[l]<p):
# 			l=l-1
# 		array=swap(array,l,h)
# 	array=swap(array,h,0)
# 	return array,h
# def qs(array,l,h):
	
# 	array,hi=partition(array,l,h)
# 	qs(array,l,hi)
# 	qs(array,hi+1,h)
# 	print(array)
	

# print(quicksort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))		

def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high]     
  
    for j in range(low, high):

        if arr[j] <= pivot:

            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
  
  
def quickSort1(arr,low,high):

    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort1(arr, low, pi-1)
        quickSort1(arr, pi+1, high)
        return arr

def quicksort(arr):
    n = len(arr)
    res = quickSort1(arr,0,n-1)
    return res

  

print(quicksort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))

