# Summation of primes
# We need to find all primes below 2M and add them
# This involves using the sieve of erastothenes

from typing import final
from bitarray import bitarray


def primesFinder(finalNumber):
    primesList = bitarray(finalNumber)
    primesList.setall(True)
    primesList[0] = 0
    primesList[1] = 0

    prime = 2
    while prime < finalNumber:
        if primesList[prime] != 1:
            prime += 1
        for primeMultiple in range(prime*2, finalNumber, prime):
            primesList[primeMultiple] = 0
        prime += 1

    return primesList
    
def bitAdder(bitsArray):
    total = 0
    
    for prime, truthVal in enumerate(bitsArray):
        if truthVal:
            total += prime

    return total

print(bitAdder(primesFinder(2_000_000)))



