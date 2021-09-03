"""
Aditya Paode
BT18CSE143
System and Network Security: Lab Assignment 1
Program 5
"""

# imports system module for command line arguments
import sys

# computes the gcd of two numbers using the euclidean algo.
def gcd(a, b) -> int:
    while b:
       a, b = b, a % b
  
    return a

# computes the number of elements in rrsm m based on euler's totient function in O(nlogn) time
def phi(m) -> int:

    # all the rrsm's contain 1 as an element
    result = 1

    # iterates though 2 -> (m - 1) and checks if gcd(m, loop invariant) = 1
    for num in range(2, m):
        if gcd(num, m) == 1:
            result += 1

    # returns the length of rrsm m
    return result

# computes euler's totient function using its properties in O(sqrt(n)loglogn) time
def phi_eff(m) -> int:

    # variables to store the result and all the prime factors of m along with their powers 
    result = 1
    primes = dict()

    # if 2 is a prime factor increments its power and keeps dividing the number until it's odd
    while m % 2 == 0:
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
            m //= factor

    # checks if the argument itself is a prime greater than 2
    if m > 2:
        primes[m] = primes.get(m, 0) + 1

    # iterates through all the factors and their powers, computing the value of phi for each one
    for factor, power in primes.items():
        result *= factor ** power - factor ** (power - 1)

    # returns the computed value of the number of elements in rrsm m
    return result

# computes the solution to the given equation according to fermat's theorem
def fermat(a, x, n) -> int:

    # variables to store phi(n) and the ans to the equation
    p = phi_eff(n)
    result = 0

    # prints initial equation
    #print(f"{a}^{x} (mod {n})", end=" ")

    # prints intermediate step of the equation after power is broken down into parts
    #print(f"{a}^{x%p} * {a}^({x//p} * {p}) (mod {n})", end=" ")

    # calculates the result without modulo n
    result = a ** (x % p)

    # prints the penultimate step of the equation
    #print(f"{result} (mod {n})", end=" ")

    # returns the final result 
    return result % n

# driver code
if __name__ == "__main__":

    # takes command line input, parses it before and after computing the solution then prints it
    print(fermat(*[int(i) for i in sys.argv[1:]]), end="")