# Even fibonacci numbers
# If we have to iterate through each fibonacci number and check if fibNum % 2 == 0
# That is going to take us a lot of time. But we know the following facts:
# Odd + odd = even
# Even + odd = odd
# Odd + Even = odd
# So we have to first know in which places the even numbers will pop up.
# Seeing the series 1 1 2 3 5 8 13 21 34 55 89 144 we can deduce that even numbers
# will show in f(n) when n is a multiple of 3.
# Therefore, we only need to calculate those numbers.

from math import sqrt

def calcFibNum(n):
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

sumFibNums = 0
stepNumber = 3
fibNum = calcFibNum(3)

while fibNum < 4_000_000:  # if the fibonacci series number is below 4M, we continue
    # yeap, underscores can be used like that
    sumFibNums += fibNum
    stepNumber += 3
    fibNum = calcFibNum(stepNumber)
    # We add it to the sum, jump 3 steps ahead and calculate it again.

print(sumFibNums)
