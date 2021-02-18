# In order to find the largest prime factor of 600851475143 we DONT use the sieve of erastothenes...
# Look at 200_success explanation in code review exchange for an explanation of this algorithm.

def findLargestPrimeFactor(n):
    number = n
    primeToCheck = 3  # We dont start with 2 as we know it wont divide evenly the number we look for.
    while number / primeToCheck != 1:  # We will stop when we find the largest prime factor
        if number % primeToCheck == 0:
            number = number / primeToCheck
        else:
            primeToCheck += 2  # We only test odd numbers to see if they are a prime factor


    return primeToCheck

print(findLargestPrimeFactor(600851475143))
            


        

    