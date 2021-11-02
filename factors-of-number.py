from functools import reduce
#   LINK: https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python

def get_factors_i(value):
    factors = []
    for x in range(1, value+1):
        if value % x == 0:
            factors.append(x)
    return factors


def get_factors_ii(value):
    return list(reduce(list.__add__, ([i, value//i] for i in range(1, int(value**0.5) + 1) if value % i == 0)))


def get_factors_iii(value):
    return set( factor for i in range(1, int(value**0.5) + 1) if value % i == 0 for factor in (i, value//i))


#   TODO: 2021-11-02T21:06:50AEDT _algorithms, factors-of-number, sympy solution?


print(sorted(get_factors_i(96)))
print(sorted(get_factors_ii(96)))
print(sorted(get_factors_iii(96)))


