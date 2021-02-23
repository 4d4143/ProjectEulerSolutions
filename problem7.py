# We have to find the 10001th prime number
# Just that. We have to start at 3 and from there check odd numbers.
# This algorithm could be improved with a generator to save memory
# The use of a list is quite memory intensive

def findNthPrime(number):
    primes = [2]
    check = 3

    while len(primes) < number: 
        if all(check % prime != 0 for prime in primes ):
            primes.append(check) # In case it is, we go to the next prime
            check += 2
        else:
            check += 2 # In case its not we go to the next one
    
    return primes[-1] # We return the last element

if __name__ == '__main__':
    print(findNthPrime(10_001))
        