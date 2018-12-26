#pattern printing


"""
*
**
***
****
*****


    *
   ***
  *****
 *******
*********

"""


from  __future__ import print_function
def pattern1():
	for i in range(5):
		for j in range(i):
			print('*',end='')
		print("")
		# print_line

def print_i_star(i):
	for j in range(i):
		print('*',end='')









def pattern2():
	for i in range(5):
		# i baar star
		print_i_star(i)
		# nextline
		print('')


pattern2()