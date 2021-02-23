# We have to find the difference of the sum of the first n squared num and the square of the sum of
# the first n numbers Ie: (1^2 + 2^2 + 3^2) - (1+2+3)^2
# We know the formulas for sums of n terms and n^2 terms

def squaredNumbersSum(number):
    total = number * (number + 1) / 2
    return total ** 2


def sumSquares(number):
    total = (number * (number + 1) * (2 * number + 1) / 6)
    return total

def difSums(number):
    difference = squaredNumbersSum(number) - sumSquares(number)
    return difference

if __name__ == '__main__':
    print(difSums(100))