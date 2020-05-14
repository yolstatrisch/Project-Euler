'''
https://projecteuler.net/problem=1
Solution by: yolstatrisch

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below n.
'''

def multiples_below(num, mul):
	return (num - 1) // mul

def triangle(num):
	return num * (num + 1) // 2

def pe001(n):
	mul_three = multiples_below(n, 3)
	mul_five = multiples_below(n, 5)
	mul_fifteen = multiples_below(n, 15)
	
	print(triangle(mul_three) * 3 + triangle(mul_five) * 5 - triangle(mul_fifteen) * 15)
	
