"""
Aditya Paode
BT18CSE143
System and Network Security: Lab Assignment 1
Program 2
"""

# imports system module for command line arguments
import sys

# calculates the gcd's linear combo. according to the extended euclidean algorithm in O(log min(a, b)) time
def gcd_extended(a, b) -> tuple:

    # base case
    if a == 0:
        return 0, 1

    # recursive call 
    x, y = gcd_extended(b % a, a)

    # returns the gcd and its linear combo. wrt x and y as a tuple
    return (y - (b//a) * x, x)

# driver code
if __name__ == "__main__":

    # takes command line input, parses it before and after computing (x, y) and prints them
    print(" ".join(map(str, gcd_extended(*map(int, sys.argv[1:])))))