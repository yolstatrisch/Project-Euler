'''
https://projecteuler.net/problem=2
Solution by: yolstatrisch

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed n, find the sum of the even-valued terms.
'''

import math
from decimal import *

getcontext().prec = 24
phi = (Decimal(5) ** Decimal(0.5) + Decimal(1)) / Decimal(2)

def pe002(n):
	n = Decimal(n - 1)
	
	index = (math.floor(math.log(n * (phi + Decimal(2)), phi) - 1)  // Decimal(3)) * Decimal(3) + Decimal(2)
	num = round(phi ** Decimal(index + 1)) / (phi + Decimal(2))
	sum = num // Decimal(2)
	
	return int(sum)