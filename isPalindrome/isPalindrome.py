# isPalindromicPrime() Write a function isPalindromicPrime that takes a value n as a parameter and returns True if the given n is a palindrome and prime and False otherwise.
# assert (isPalindromicPrime(2) == True)
# assert (isPalindromicPrime(10) == False)
# assert (isPalindromicPrime(104) == False)
# assert (isPalindromicPrime(235) == False)
# assert (isPalindromicPrime(131) == True)
# assert (isPalindromicPrime(900) == False)
# assert (isPalindromicPrime(101) == True)
# assert (isPalindromicPrime(383) == True)
# assert (isPalindromicPrime(373) == True)
# assert (isPalindromicPrime(121) == False)
# print("All test cases passed... :-)")
def prime(n):
    if(n==1):
        return True
    if(n==2):
        return True
    for i in range(3,int(n/2)+1):
        if(n%i==0):
            return False
    return True
def palin(n):
    n=str(n)
    # for i in range(int(len(n)/2)):
    #     for j in range(len(n),int((len(n)/2))):
    #         print(i,j)
    #         if(n[i]!=n[j]):
    #             return False
    # return True
    if(n==n[::-1]):
        return True
    else:
        return False

def isPalindromicPrime(n):
    if(palin(n) and prime(n)):
        return True
    else:
        return False
print(isPalindromicPrime(10))

