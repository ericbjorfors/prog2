#!/usr/bin/env python3.9

from person import Person
from time import perf_counter as pc

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))
	
def main():
	fib_list = []
	start = pc()
	for i in [n for n in range(30,46)]:
		fib_list.append(fib_py(i))
	end = pc()
	print(f'Generated fibonacci sequence {fib_list} in time {start-end} seconds')
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())

if __name__ == '__main__':
	main()
