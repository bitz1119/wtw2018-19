from __future__ import print_function

def print_n_stars(n):
	for i in range(n):
		print('*',end='')

def print_n_spaces(n):
	for i in range(n):
		print(" ",end='')

def pattern_triange():
	for i in range(5):
		# print n-i spaces
		print_n_spaces(5-i)
		# print 2*i+1 starts
		print_n_stars(2*i+1)
		# print nextline
		print('')


pattern_triange()