# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 10:20:34 2015

@author: JVICHO
"""

"""
Problem 003:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 317584931803?
"""
import math

def is_prime(n):
    """Check if the number is prime"""
    
    if n < 2:
        return False
    elif n == 2 or n == 3 or n == 5:
        return True
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    
    i = 6
    sqrt_n = int(math.ceil(math.sqrt(n)))
    
    while i <= sqrt_n + 1:
        if n % (i - 1) == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def get_prime_factors(n):
    """
    Prime factors of an integer.
    factors -> dictionary of each prime factor
    """
    factors = {}
    if n <= 1: return {}
    
    while n != 1:
        if is_prime(n):
            factors[n] = 1
            break
        
        i = 2
        while i <= n:
            j = 0
            while n % i == 0 and n != 1:
                j += 1
                n //= i
            
            if j > 0:
                factors[i] = j
                break
            i += 1
    
    return factors

N = 317584931803
print(max(get_prime_factors(N).keys()))