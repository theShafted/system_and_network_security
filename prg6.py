"""
Aditya Paode
BT18CSE143
System and Network Security: Lab Assignment 1
Program 6
"""

# imports system module for command line arguments
import sys

# calculates gcd and its linear combo. according to the extended euclidean algorithm
def gcd_extended(x, y) -> tuple:

    # base case
    if x == 0:
        return y, 0, 1

    # recursive call 
    g, a, b = gcd_extended(y % x, x)

    # returns the gcd and its linear combo. wrt x and y
    return (g, b - (y//x) * a, a)

# checks the existence of and computes the multiplicative inverse modulo m in O(log min(a, m)) time
def mul_inverse(a, m) -> int or str:

    # gets the gcd and the inverse of a under modulo m
    gcd, inverse = gcd_extended(a, m)[:2]

    # the inverse exists iff gcd(a, m) = 1
    if gcd == 1:

        # if the inverse exists then print "Y"
        print("Y", end=" ")

        # if the inverse is negative then add m before returning
        return inverse if inverse > 0 else inverse + m

    # if the gcd doesn't exist then print "N"
    return "N"

# driver code
if __name__ == "__main__":

    # takes command line input, parses it before and after computing the inverse then prints it
    print(mul_inverse(int(sys.argv[1]), int(sys.argv[2])), end="")