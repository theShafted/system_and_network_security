"""
Aditya Paode
BT18CSE143
System and Network Security: Lab Assignment 1
Program 7
"""

# imports system module for command line arguments
import sys

# calculates gcd and its linear combo. according to the extended euclidean algorithm
def gcd(x, y, extended=False) -> int or tuple:

    # base case
    if x == 0:
        return y, 0, 1

    # recursive call 
    g, a, b = gcd(y % x, x, extended=True)

    # returns the gcd and its linear combo. wrt x and y
    return (g, b - (y//x) * a, a) if extended else g

# computes all the solutions to a single congurence equation in O(log min(a, m)) time
def congurence_solution(a, b, m) -> tuple:

    # computes the gcd(a, m) using the euclidean algo.
    g = gcd(a, m)
    
    # checks the pre-requisites for the theorem to confirm existence of solutions
    if b <= 0 or b % g != 0:

        # prints "N" as no solutions exist and returns
        print("N")
        return 

    # prints "Y" because solution/s exist
    print("Y", end=" ")

    # calculates the values of alpha, beta, mu
    alpha, beta, mu = a//g, b//g, m//g

    # computes alpha inverse under modulo mu using the extended euclidean algo
    alpha_inv = gcd(alpha, mu, extended=True)[1]

    # if the inverse if negative then add mu to get it in the proper range
    if alpha_inv < 0:
        alpha_inv += mu

    # gets the total number of solutions according to the value of g
    x = alpha_inv * beta % mu
    solutions = [x + i * mu for i in range(g)]

    # returns a tuple of solutions to the congurence
    return tuple(solutions)

# driver code
if __name__ == "__main__":

    # takes command line input, parses it and stores the computed solution in a variable
    solutions = congurence_solution(*[int(num) for num in sys.argv[1:]])

    # checks whether the solution isn't None
    if solutions:

        # prints the number of solutions and them after parsing
        print(f"{len(solutions)} " + " ".join(map(str, solutions)))