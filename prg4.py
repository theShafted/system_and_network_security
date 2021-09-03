"""
Aditya Paode
BT18CSE143
System and Network Security: Lab Assignment 1
Program 4
"""

# imports system module for command line arguments
import sys

# computes the gcd of two numbers using the euclidean algo.
def gcd(a, b) -> int:
    while b:
       a, b = b, a % b
  
    return a

# computes and returns the reduced residue system modulo m in O(mlogm) time
def rrsm(m) -> tuple:

    # variables to store the crsm and rrsm for modulo m
    result = list()
    crsm = range(0, m)

    # check all the elements in crsm and add them to rrsm if gcd(element, m) = 1
    for num in crsm:
        if gcd(num, m) == 1:
            result.append(num)

    # return the rrsm as an immutable list of numbers (tuple)
    return tuple(result)

# driver code
if __name__ == "__main__":

    # stores the rrsm m in a variable where m is taken from command line argument
    result = rrsm(int(sys.argv[1]))

    # prints the elements in rrsm m and the value of phi(m)
    print(" ".join(map(str, result)) + f" {len(result)}", end="")