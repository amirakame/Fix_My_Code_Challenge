#!/usr/buin/python3
""" FizzBuzz
"""

import sys


def fizzbuzz(n):
	    """
FizzBuzz function prints numbers from 1 to n separated by  space.

- For multiples of three print "Fizz" instead of  number and for
multiples of five print "Buzz".
- For numbers which are multiples of both three and five print "FizzBuzz".
	"""
		if n < 1:
                     return

		tmp_result = []
		for m in range(1, n + 1):
		     if (m % 3) == 0 and (m % 5) == 0
		     tmp_result.append("FizzBuzz")
	elif (m % 3) == 0
		tmp_result.append("Fizz")
	elif (m % 5) == 0:
		tmp_result.append("Buzz")
	   else:
		tmp_result.append(str(m))
print(" ".join(tmp_result))


	if __name__ == '__main__':
	         if len(sys.argv) <= 1:
print("Missing number")
print("Usage: ./0-fizzbuzz.py <number>")
print("Example: ./0-fizzbuzz.py 89")
sys.exit(1)

number = int(sys.argv[1])
fizzbuzz(number)
