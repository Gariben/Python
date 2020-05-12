


#Initialization of value arrays. One bigger so we can use finger notation (1 2 3 4)
ascending = [[None for starting_finger in range(5)] for ending_finger in range(5)]
descending = [[None for starting_finger in range(5)] for ending_finger in range(5)]
rolling = [[None for starting_finger in range(5)] for ending_finger in range(5)]


#Derivation of Mothers Chart:


#Function for drawing finger tables to command line:
def draw_finger_table(finger_list):
	#TODO: Flexible function for variable size table and values.
	for start in range(0,5):
		if start == 0:
			for end in range(1,5):
				print("   "+str(end)+"\t", end="")
			print()
			for dash in range(0,5*6+3):
				print("-", end="")
			print()
		else:
			print(str(start)+"|", end="")
			for end in range(1,5):
				print(str(finger_list[start][end]), end="")
				print("\t|", end="")
			print()
			for dash in range(0,5*6+3):
				print("-", end="")
			print()



#Begin Human-Readable Stuff:

#Comparative values for difficulty of moving from one finger to another when ascending:
# See origin Document:
# https://docs.google.com/spreadsheets/d/1EQ8WNFIp1qbgWHwbtd928ndtK_kUPdpr6xzbfFYtIrQ/edit?usp=sharing

#-------------------------------------------------------------------------------------

ascending[1][2] = 1
ascending[1][3] = 4
ascending[1][4] = 6

ascending[2][1] = 7
ascending[2][3] = 3
ascending[2][4] = 5

ascending[3][1] = 11
ascending[3][2] = 8
ascending[3][4] = 3

ascending[4][1] = 12
ascending[4][2] = 10
ascending[4][3] = 9

print("Ascending Values:")
draw_finger_table(ascending)
print("Descending Values:")
draw_finger_table(descending)
print("Rolling Values:")
draw_finger_table(descending)

input("Press Enter to continue...")



