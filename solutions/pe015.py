'''
https://projecteuler.net/problem=15
Solution by: yolstatrisch

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a n×n grid?
'''

from math import factorial as f 

pe015 = lambda n : f(2 * n) / f(n) ** 2
