#!/usr/bin/env python3.9

from person import Person
from time import perf_counter as pc
from numba import njit
import matplotlib.pyplot as plt


def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))
	
@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return(fib_numba(n-1) + fib_numba(n-2))
	

	
def main():
	fib_py_list = []
	time_py = []
	start = pc()
	for i in [n for n in range(30,46)]:
		start_split = pc()
		fib_py_list.append(fib_py(i))
		end_split = pc()
		time_py.append(end_split-start_split)
	end = pc()
	print(f'Generated fibonacci sequence with fib_py(n) {fib_py_list} in time {end-start} seconds')

	fib_numba_list = []
	time_numba = []
	start = pc()
	for i in [n for n in range(30,46)]:
		start_split = pc()
		fib_numba_list.append(fib_numba(i))
		end_split = pc()
		time_numba.append(end_split-start_split)
	end = pc()
	print(f'Generated fibonacci sequence with fib_numba(n) {fib_numba_list} in time {end-start} seconds')

	fib_c_list = []
	time_c = []
	start = pc()
	for i in [n for n in range(30,46)]:
		start_split = pc()
		f = Person(i)
		fib_c_list.append(f.fib())
		end_split = pc()
		time_c.append(end_split-start_split)
	end = pc()
	print(f'Generated fibonacci sequence with fib_c(n) {fib_c_list} in time {end-start} seconds')



	# Create a plot
	x = [n for n in range(30,46)]
	plt.figure(1)
	plt.plot(x, time_py, label = 'fib_py(n)')
	plt.plot(x,time_numba, label = 'fib_numba(n)')
	plt.plot(x, time_c, label = 'fib_c(n)')

	# Set labels and title
	plt.xlabel('n')
	plt.ylabel('seconds')
	plt.title('Fibonacci time plot numbers 30-45')
	plt.legend()

	# Save the plot as an image file (e.g., PNG)
	plt.savefig('fib30-45.png')

	fib_py_list = []
	time_py = []
	start = pc()
	for i in [n for n in range(20,31)]:
		start_split = pc()
		fib_py_list.append(fib_py(i))
		end_split = pc()
		time_py.append(end_split-start_split)
	end = pc()
	print(f'Generated fibonacci sequence with fib_py(n) {fib_py_list} in time {end-start} seconds')
	fib_numba_list = []
	time_numba = []
	start = pc()
	for i in [n for n in range(20,31)]:
		start_split = pc()
		fib_numba_list.append(fib_numba(i))
		end_split = pc()
		time_numba.append(end_split-start_split)
	end = pc()
	print(f'Generated fibonacci sequence with fib_numba(n) {fib_numba_list} in time {end-start} seconds')

	# Create a plot
	x = [n for n in range(20,31)]
	plt.figure(2)
	plt.plot(x, time_py, label = 'fib_py(n)')
	plt.plot(x,time_numba, label = 'fib_numba(n)')

	# Set labels and title
	plt.xlabel('n')
	plt.ylabel('seconds')
	plt.title('Fibonacci time plot numbers 20-30')
	plt.legend()

	# Save the plot as an image file (e.g., PNG)
	plt.savefig('fib20-30.png')

	start = pc()
	fib47n = fib_numba(47)
	end = pc()
	print(f'Fibonacci number 47 generated with fib_numba(n) {fib47n} in time {end-start} seconds')

	start = pc()
	f47 = Person(47)
	fib47c = f47.fib()
	end = pc()
	print(f'Fibonacci number 47 generated with fib_c(n) {fib47c} in time {end-start} seconds')


	

if __name__ == '__main__':
	main()

# Generated fibonacci sequence with fib_py(n) [832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170] in time 1595.390721658012 seconds
# Generated fibonacci sequence with fib_numba(n) [832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170] in time 48.139025370939635 seconds
# Generated fibonacci sequence with fib_c(n) [832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170] in time 47.73369569296483 seconds
# Generated fibonacci sequence with fib_py(n) [6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040] in time 1.1701676190132275 seconds
# Generated fibonacci sequence with fib_numba(n) [6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040] in time 0.03440034098457545 seconds
# Fibonacci number 47 generated with fib_numba(n) 2971215073 in time 47.6744947580155 seconds
# Fibonacci number 47 generated with fib_c(n) -1323752223 in time 47.57791667606216 seconds