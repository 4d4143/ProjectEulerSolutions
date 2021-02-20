# We need to find the largest palindrome number made from 2 3-digit numbers.
# Logically, the lowest number is given by 100x100 and the largest one is given by 999x999
# We need to make a function that generates the numbers and another one that checks if its palindrome
# Notice the following: If we multiply 999x998, we dont need to do 998x999.
# For obvious optimization reasons, we start off from 999x999

def isNumberPalindrome(number):

    condition = True
    digits = [x for x in str(number)]

    for index in range(0, int( len(digits) / 2)): 
        if digits[index] != digits[-(index + 1)]:
            condition = False  
            break 

    return condition
    

def largestPalindromeFinder():
    ret = 1
    for leftFactor in range(999, 99, -1):
        for rightFactor in range(999, leftFactor -1 , -1): 
            candidate = leftFactor*rightFactor

            # loop optimization: we can safely break here, as the candidate is less than the already discovered palindromic number
            if (candidate < ret):
                break
            if isNumberPalindrome(candidate):
                if candidate > ret:
                    print("palindrom-number: {}, left-factor: {}, right-factor: {}".format(candidate, leftFactor, rightFactor))
                    ret = candidate
    
    return ret


print(largestPalindromeFinder())
