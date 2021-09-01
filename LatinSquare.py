# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(lst):
    # Your code goes here...
    d = {}
    for i in lst:
        temp = i
        for j in range(len(lst[0])):
            temp2 = i[:j] + i[j+1:]
            if i[j] in temp2:
                return False
            if j in d:
                if i[j] in d[j]:
                    return False
                else:
                    d[j].append(i[j])
            else:
                d[j] = [i[j]]
    return True