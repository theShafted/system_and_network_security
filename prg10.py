"""
Aditya Paode
BT18CSE143
System and Network Security: Lab Assignment 1
Program 10
"""

# imports system module for command line arguments
import sys

# computes the gcd of two numbers using the euclidean algo.
def gcd(a, b) -> int:
    while b:
       a, b = b, a % b
  
    return a

# computes euler's totient function using its properties in O(sqrt(n)loglogn) time
def totient(m) -> int:

    # variables to store the result and all the prime factors of m along with their powers 
    result = 1
    primes = dict()

    # if 2 is a prime factor increments its power and keeps dividing the number until it's odd
    while m % 2 == 0:

        # here the int division operator "//" is used as the "/" operator converts m to a float
        primes[2] = primes.get(2, 0) + 1
        m //= 2

    # iterates from 3 -> sqrt(num) in steps of 2 as num is now odd
    for factor in range(3, m + 1, 2):

        # checks if any factor is greater than sqrt(m)
        if factor * factor > m:
            break

        # checks if the loop invariant is a prime factor and keeps dividing until it isn't possible
        while m % factor == 0:
            primes[factor] = primes.get(factor, 0) + 1
            m /= factor

    # checks if the argument itself is a prime greater than 2
    if m > 2:
        primes[m] = primes.get(m, 0) + 1

    # iterates through all the factors and their powers, computing the value of phi for each one
    for factor, power in primes.items():
        result *= factor ** power - factor ** (power - 1)

    # returns the computed value of the number of elements in rrsm m
    return int(result)

# calculates the product of primes of the argument in ascending order 
def factors(num) -> tuple:

    # stores all the primes in a set to eliminate duplicates
    result = set()

    # checks if 2 is a prime factor and keeps dividing the number until it's odd
    while num % 2 == 0:
        result.add(2)
        num //= 2

    # iterates from 3 -> sqrt(num) in steps of 2 as num is now odd
    for factor in range(3, num + 1, 2):

        # checks if any factor is greater than sqrt(num)
        if factor * factor > num:
            break

        # checks if the loop invariant is a prime factor and keeps dividing until it isn't possible
        while num % factor == 0:
            result.add(factor)
            num //= factor

    # checks if the argument itself is a prime greater than 2
    if num > 2:
        result.add(num)

    # return the primes as an immutable list of numbers (tuple)
    return tuple(result)

# computes all the primitive roots under modulo argument in O(m phi(m)) time
def primitive_root(m) -> tuple:

    # variables to store the values of the primitive roots, euler's totient function and its prime factors
    roots = set()
    phi = totient(m)
    primes = factors(phi)

    # computes the reduced residue system modulo m using list comprehension
    rrsm = set([num for num in range(1, m) if gcd(num, m) == 1])

    # iterate from 2 -> phi to check if any one of the nums is a primitive root
    for num in rrsm:

        # flag to check if any of the orders equate to 1
        flag = False

        # iterates through all the prime factors of phi and checks if they're aceeptable
        for factor in primes:
            if num ** (phi // factor) % m == 1:
                flag = True
                break

        # adds the num as an acceptable primitive root
        if flag == False:
            roots.add(num)

    # return the primitive roots as a tuple if solution exists
    return tuple(roots)

# driver code
if __name__ == "__main__":

    # computes the primitive roots (if any) using the user defined function
    roots = primitive_root(int(sys.argv[1]))

    # prints the number of roots
    print(len(roots), end="")

    # checks if there are any primitive roots exist
    if roots:
        # prints the roots after parsing the solution
        print(" " + " ".join(map(str, roots)), end="")