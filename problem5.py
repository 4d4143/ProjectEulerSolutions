# We have to find the smallest positive number such that all integers from 1 to 20
# are able to evenly divide it -> ( answer % x == 0 )
# Notice that if X can be divided by 4, it can also be divided by 2.
# If it can be divided by 16, it can be divided by 8, 4 and 2.
# Following this logic we take out numbers until we are left with a prime number (11)
# Since the largest number is 20, we should be checking in steps of 20.


def smallestCommonMultiple():
    startingNum = 20
    found = False
    multiplesList = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

    while not found:
        evaluation = all(startingNum % multiple == 0 for multiple in multiplesList)
        if not evaluation:
            startingNum += 20
        else:
            print("Found number!")
            return startingNum

if __name__ == '__main__':
    print(smallestCommonMultiple())