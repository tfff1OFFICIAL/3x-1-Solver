#from __future__ import division
import math

# Replaced - Caused maximum recursion limit breaches for certain numbers.
def get_final_number(n, count = -1):
    count += 1
    final_count = count
    if n != 1:
        print("Iteration %s returns: %s" % (count, n))
        if n % 2 == 0:
            # Even
            n, final_count = get_final_number(n / 2, count)
        else:
            # Odd
            n, final_count = get_final_number((3 * n) + 1, count)
    return n, final_count

def get_number(n):
    recursion_count = -1
    while n != 1:
        recursion_count += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
        print("Iteration %s returns: %s" % (recursion_count, n))
    return n, recursion_count

while True:
    number = input("Enter a starting number: ")
    print("Returned %s on iteration %s." % get_number(int(number)))