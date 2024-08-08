#!/usr/bin/python3
"""
Module: min_operations
-----------------------
This module contains a function `minOperations` that calculates
the minimum number of operations required to achieve exactly `n`
'H' characters in a text file, starting with a single 'H'.

Operations allowed:
- Copy All: Copies all the characters present in the file.
- Paste: Pastes the copied characters.

The function uses a factorization approach to minimize the number
of operations needed.

Example:
    n = 9
    H => Copy All => Paste => HH => Paste => HHH
    => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
    Number of operations: 6

Functions:
- minOperations(n): Returns the minimum number of operations needed to reach `n` characters.
"""

def minOperations(n):
    """Calculate the minimum number of operations required to get n 'H' characters."""
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    return operations

