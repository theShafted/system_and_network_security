"""
Aditya Paode
BT18CSE143
System and Network Security: Lab Assignment 1
Program 1
"""

# imports system module for command line arguments
import sys

# computes the gcd of two numbers using the euclidean algo.
def gcd(a, b) -> int:
    while b:
       a, b = b, a % b
  
    return a

# computes all the common divisors of all arguments in O(nlogm) where m is the max number
def common_divisors(args) -> tuple:

    # variables to store the gcd and the common divisors of the arguments
    g = args[0]
    result = list()

    # iterates through all the numbers to compute the overall gcd
    for num in args:
        g = gcd(g, num)

    # iterates from 1 -> gcd as the all the common divisors lie in this range
    for num in range(1, g + 1):

        # if any number is greater than the sqrt(gcd) then it's not a common divisor
        if num * num > g:
            break

        # if the number divides the gcd then it is accepted
        if g % num == 0:
            result.append(num)

    # iterate through the numbers a second time to get the divisors in ascending order
    for num in range(g, 0, -1):
            
        # check if the divisors are equal and accept them if they aren't
        if num * num < g and g % num == 0:
            result.append(g // num)

    # returns the result as an immutable list of numbers (tuple)
    return tuple(result)

# driver code
if __name__ == "__main__":

    # takes command line input, parses it before and after computing the common divisors and prints them
    print(" ".join(map(str, common_divisors([int(num) for num in sys.argv[2:]]))), end="")