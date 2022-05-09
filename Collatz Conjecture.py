def collatz(x):
	while(x != 1):
		if (x%2 == 0):
			print("EVEN: ", end='')
			print(x)
			x =  x//2
			#If a NUMBER is EVEN, the next number could be EVEN or ODD
			# 10 // 2 = 5 - ODD     ----- 20 // 2 = 10 - EVEN     ------ 30 // 2 = 15 - ODD       ----- 40 // 2 = 20 - EVEN
			# 12 // 2 = 6 - EVEN    ----- 22 // 2 = 11 - ODD      ------ 32 // 2 = 16 - EVEN
			# 14 // 2 = 7 - ODD     ----- 24 // 2 = 12 - EVEN     ------ 34 // 2 = 17 - ODD
			# 16 // 2 = 8 - EVEN    ----- 26 // 2 = 13 - ODD      ------ 36 // 2 = 18 - EVEN
			# 18 // 2 = 9 - ODD     ----- 28 // 2 = 14 - EVEN     ------ 38 // 2 = 19 - ODD
			#Every even integer yields a result 1 greater than the previous even integer.
		elif (x%2 == 1):
			print("ODD: ", end='')
			print(x)
			x = 3*x + 1
			#If a Number is ODD, the next number has to be EVEN
			# 1 * 3 + 1 = 4
			# 3 * 3 + 1 = 10
			# 5 * 3 + 1 = 16
			# 7 * 3 + 1 = 22
			# 9 * 3 + 1 = 28
			#Every odd integer yields a result 6 greater than the previous odd integer.
	print(x)

def collatz_pattern(x, report_start_minus_x=False):
	start = x
	wheel = 3
	#We are looking for a 4 step pattern like the Classic Loop
	while (wheel != 0):
		wheel -= 1
		if (x%2 == 0):
			x = x//2
		elif (x%2 == 1):
			x = 3*x + 1
	if (report_start_minus_x == True):
		print(start - x)
	if (start == x):
		#print("PATTERN FOUND: ", start)
		return True
	else:	
		return False


#Then following bit was a code to check for the existence of a new pattern. However, the collatz_pattern() only yields true for a value of 1.

#x = 1
#while (collatz_pattern(1+120*x) == False):
	#x += 1

#This will loop forever for reasons seen below

#There is a pattern in the difference between the first and the fourth x value in the collatz_pattern()

for x in range(0,101):
	collatz_pattern(1 + 120*x, True)

#There is a gap of 30x for every iteration of a possible pattern. Only when x = 0 does the collatz conjecture loop.




