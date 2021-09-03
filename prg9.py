"""
Aditya Paode
BT18CSE143
System and Network Security: Lab Assignment 1
Program 9
"""

# imports system module for command line arguments
import sys

# computes euler's totient function using its properties in O(sqrt(n)loglogn) time
def phi(m) -> int:

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

# computes order of a modulo m using euler's totient function
def order(a, m):

    # computes the value of euler's totient function and creates an empty set to store all its divisors
    p = phi(m)
    divisors = list()

    # iterates from 2 -> p as the all the order is among the divisors
    for divisor in range(2, p + 1):

        # if any number is greater than the sqrt(phi(m)) then it's not a common divisor
        if divisor * divisor > p:
            break

        # if the number divides the phi(m) then it is accepted
        if p % divisor == 0:
            divisors.append(divisor)


    # iterate through the divisors again to get them in ascending order
    for divisor in range(p, 0, -1):

        # check if the quotient of (phi(m) / divisor) is also acceptable 
        if divisor * divisor < p and p % divisor == 0:
            divisors.append(p // divisor)

    # iterates through all the divisors and returns the smallest accepted value
    for divisor in divisors:
        if pow(a, divisor, m) == 1:
            return divisor

# driver code
if __name__ == "__main__":

    # takes command line input, parses it before and after computing the order then prints it
    print(order(int(sys.argv[1]), int(sys.argv[2])))