import sys
from math import prod

# calculates gcd and its linear combo. according to the extended euclidean algorithm
def gcd(x, y, extended=False) -> int or tuple:
    if x == 0:
        return y, 0, 1

    # recursive call 
    g, a, b = gcd(y % x, x, extended=True)

    # returns the gcd and its linear combo. wrt x and y
    return (g, b - (y//x) * a, a) if extended else g

# computes solutions to the system of congurences according to crt in O(nlog min(a, m)) time
def chinese_remainder_theorem(a, b, m) -> int:

    # gets the number of equations in the system and stored them in a variable
    length = len(m)

    # guard clause satisfying the pre-requisites for the theorem
    for i in range(length):
        if m[i] <= 0:
            return "N"

        for j in range(length):
            if i != j and gcd(m[i], m[j]) != 1:
                return "N"

    M = prod(m)

    # converts to the standard form by inversing the coeff. of x
    a = [b[i] * gcd(a[i], m[i], extended=True)[1] for i in range(length)]

    # calcs. b[j], i.e. the inverse of M/m[j] under modulo m[j]
    b = [gcd(M/m[j], m[j], extended=True)[1] for j in range(length)]

    # gets the final value of x[0] under modulo M
    x = int(sum([M * b[j] * a[j] / m[j] for j in range(length)]) % M)

    print("Y", end=" ")
    return x

# driver code
if __name__ == "__main__":

    # parse the command line arguments and store them in variables
    args = [[], [], []]
    for i in range(2, 3 * int(sys.argv[1]) + 2):
        args[(i - 2) % 3].append(int(sys.argv[i]))

    # prints the solution to the system of congurences using the crt
    print(chinese_remainder_theorem(*args))