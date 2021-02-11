# Multiples of 3 and 5 
# We need to find the numbers that have 3 or (inclusive or..) 5 as factors and then sum them.
# If 3 or 5 is a factor of X, then X divided by 3 or 5 gives a remainder equal to 0

sumOfNumbers = 0  # For each number we find, we will add it


for number in range(1001):
    # We loop through all numbers below 1000 and see which ones are divisible by 3 or 5
    if (number % 3 == 0) or (number % 5 == 0):
        sumOfNumbers += number

print(sumOfNumbers)


