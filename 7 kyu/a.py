import math


def square_root(n):
    root = n / 2  # initial guess will be 1/2 of n
    for _ in range(20):
        root = (1 / 2) * (root + (n / root))

    return root


print(dir(math), sep='\n')