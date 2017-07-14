#!/usr/bin/python
from math import ceil
def find_champ_num(d):
    tmp, base = remaining_nums(d)
    # just roll with this
    tmp, pos = ceil(10**(base - 1) - 1 + (tmp / base)), tmp % base
    return int(str(tmp)[pos-1])


def remaining_nums(n):
    # subtract the number of digits we get from lower powers of 10 until we hit the right one
    # eg, for 1000 we subract 189 for 2 digits * 90 2-digit numbers + 1 digit * 9 1-digit numbers
    i = 1
    tmp, past = n, n
    while tmp > 0:
        past = tmp
        tmp -= (10**i - 10**(i - 1)) * i
        i += 1
    return past, i - 1


tmp = 1
for i in range(7):
    v = find_champ_num(10**i)
    tmp *= v
print(tmp)