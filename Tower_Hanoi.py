#! /usr/bin/python3


#Ricardo Vergara
#Tower of Hanoi 
#Quarantine Project


import stdio
import sys 
import stdarray
import array
import math


m = int(sys.argv[1])
n = m * 3
p = 1




sinoi = stdarray.create2D(m, 3, 0)
a = len(sinoi) 

for i in range(0, a):
	for k in range(0,a):
		if (k == 0):
			sinoi[i][k] = p
			p = p + 1

def print_sinoi():
	for j in range(0, a):
		print(sinoi[j])
		if j % 2 == 0: 
			stdio.writeln()
		if j % 2 == 1:
			stdio.writeln() 
	stdio.writeln()
	stdio.writeln()
	stdio.writeln()




first_peg = stdarray.create1D(m, 0)
second_peg = stdarray.create1D(m, 0)
third_peg = stdarray.create1D(m, 0)



def new_peg1(): 
	for i in range(0, m):
		first_peg[i] = sinoi[i][0]

def new_peg2(): 
	for i in range(0, m):
		second_peg[i] = sinoi[i][1]


def new_peg3(): 
	for i in range(0, m):
		third_peg[i] = sinoi[i][2]


def disc_location(disc_turn):
	if disc_turn in first_peg:
		return 1
	elif disc_turn in second_peg:
		return 2
	elif disc_turn in third_peg:
		return 3

def add_disc_peg1(x):


	
	
	if disc_location(x) == 2:
		index_1 = second_peg.index(x)
		second_peg[index_1] = 0
		sinoi[index_1][1] = 0
		
				

	elif disc_location(x) == 3:
		index_2 = third_peg.index(x)
		third_peg[index_2] = 0
		sinoi[index_2][2] = 0
	off_set = 0
	for i in range(0, m):
		if first_peg[i] == 0:
			off_set += 1
	sinoi[off_set-1][0] = x
	
	new_peg1()
	new_peg2()
	new_peg3()
			
	

	return print_sinoi()
				
				

def add_disc_peg2(x):
	
	
	if disc_location(x) == 3:
		index_1 = third_peg.index(x)
		third_peg[index_1] = 0
		sinoi[index_1][2] = 0
				

	elif disc_location(x) == 1:
		index_2 = first_peg.index(x)
		first_peg[index_2] = 0
		sinoi[index_2][0] = 0

	off_set = 0
	for i in range(0, m):
		if second_peg[i] == 0:
			off_set += 1
	sinoi[off_set-1][1] = x
	new_peg1()
	new_peg2()
	new_peg3()
	
	
				
	return print_sinoi()

def add_disc_peg3(x):
	

	if disc_location(x) == 1:
		index_1 = first_peg.index(x)
		first_peg[index_1] = 0
		sinoi[index_1][0] = 0
				


	elif disc_location(x) == 2:
		index_2 = second_peg.index(x)
		second_peg[index_2] = 0
		sinoi[index_2][1] = 0

	off_set = 0
	for i in range(0, m):
		if third_peg[i] == 0:
			off_set += 1
	sinoi[off_set-1][2] = x
	
	new_peg1()
	new_peg2()
	new_peg3()

	

	return print_sinoi()



num_moves = (2 ** m) - 1 
split_moves = int((2 ** m)/2)

for i in range(0,m):
		for j in range(1):
			first_peg[i] = sinoi[i][0] #The first column



def disc_turn(current_move):
	turn_array = stdarray.create2D(m, split_moves, 0)
	for i in range(0, m):
		for j in range(0, split_moves):
			plug = int(((2 ** (i + 1)) * ((j + 1) - 0.5)))
			turn_array[i][j] = int(plug)
	for i in range(0, m):
		for j in range(0, split_moves):
			if turn_array[i][j] == current_move:
				disc_turn = int(i + 1) 
				return (int(disc_turn))


		
def even_discs():
	for i in range(1, num_moves + 1):
		if disc_turn(i) % 2 == 1:
			if disc_location(disc_turn(i)) == 1:
				add_disc_peg2(disc_turn(i))
			elif disc_location(disc_turn(i)) == 2:
				add_disc_peg3(disc_turn(i))
			elif disc_location(disc_turn(i)) == 3:
				add_disc_peg1(disc_turn(i))
		elif disc_turn(i) % 2 == 0:
			if disc_location(disc_turn(i)) == 1:
				add_disc_peg3(disc_turn(i))
			elif disc_location(disc_turn(i)) == 2:
				add_disc_peg1(disc_turn(i))
			elif disc_location(disc_turn(i)) == 3:
				add_disc_peg2(disc_turn(i))


def odd_discs():
	for i in range(1, num_moves + 1):
		if disc_turn(i) % 2 == 0:
			if disc_location(disc_turn(i)) == 1:
				add_disc_peg2(disc_turn(i))
			elif disc_location(disc_turn(i)) == 2:
				add_disc_peg3(disc_turn(i))
			elif disc_location(disc_turn(i)) == 3:
				add_disc_peg1(disc_turn(i))
		elif disc_turn(i) % 2 == 1:
			if disc_location(disc_turn(i)) == 1:
				add_disc_peg3(disc_turn(i))
			elif disc_location(disc_turn(i)) == 2:
				add_disc_peg1(disc_turn(i))
			elif disc_location(disc_turn(i)) == 3:
				add_disc_peg2(disc_turn(i))


def tower_of_hanoi():
	if m % 2 == 0:
		even_discs()
	elif m % 2 == 1:
		odd_discs()

print_sinoi()
tower_of_hanoi()

			
		
	



