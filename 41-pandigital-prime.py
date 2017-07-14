#!/usr/bin/python
from itertools import permutations
from math import sqrt, ceil

# not used because it's really, really slow
def fermatPrimality(n):
    for a in range(1, 10):
        if pow(a, n-a, n) != 1:
            return False
    return True

def naivePrimality(n):
    for a in range(5, ceil(sqrt(n))):
        if n % a == 0:
            return False
    return True

for num_digits in range(4, 10):
    for i in range(num_digits, 1, -1):
        for numArr in permutations(''.join(set([str(j) for j in range(1, num_digits)])-set([str(i)]))):
            num = int(str(i)+''.join(numArr))
            if num % 3 == 0 or num % 2 == 0:
                # skip obviously non-prime numbers
                continue

            if naivePrimality(num):
                print(num)
                break
print('terminated')
