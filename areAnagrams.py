# areAnagrams(s1, s2)
# Write the function areAnagrams(s1, s2) that takes two strings, 
# s1 and s2, that you may assume contain only upper and/or 
# lower case letters, and returns True if the strings are 
# anagrams, and False otherwise. Two strings are anagrams 
# if each can be reordered into the other. Treat "a" and "A"
# as the same letters (so "Aba" and "BAA" are anagrams). 
# You may not use sort() or sorted() or any other list-based
# functions or approaches. Hint: you may use s.count(), 
# which could be quite handy here.
# Hint: The time complexity can be achieved in Linear.

def areAnagrams(s1, s2):
    # Your code goes here...
    # pass
    s1=s1.lower()   
    s2=s2.lower()
    l=0
    k=0
    
    if(len(s1)!=len(s2)):
        return False
    for i in range(len(s1)):
        
        l=l+s1.count(s1[i])
        k=k+s2.count(s2[i])
    # print(l,k)
    if(l==k):
        return True
    else:
        return False


