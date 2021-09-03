"""
Aditya Paode
BT18CSE143
System and Network Security: Lab Assignment 1
Program 3
"""

# imports system module for command line arguments
import sys

# calculates the product of primes of the argument in ascending order in O(logn) time
def fta(num) -> tuple:

    # stores all the primes in a set to eliminate duplicates
    result = list()

    # checks if 2 is a prime factor and keeps dividing the number until it's odd
    while num % 2 == 0:
        result.append(2)
        num //= 2

    # iterates from 3 -> sqrt(num) in steps of 2 as num is now odd
    for factor in range(3, num + 1, 2):

        # checks if any factor is greater than sqrt(num)
        if factor * factor > num:
            break

        # checks if the loop invariant is a prime factor and keeps dividing until it isn't possible
        while num % factor == 0:
            result.append(factor)
            num //= factor

    # checks if the argument itself is a prime greater than 2
    if num > 2:
        result.append(num)

    # return the primes as an immutable list of numbers (tuple)
    return tuple(result)

# driver code
if __name__ == "__main__":

    # takes command line input, parses it before and after computing the primes and prints them
    print(" ".join(map(str, fta(int(sys.argv[1])))), end="")