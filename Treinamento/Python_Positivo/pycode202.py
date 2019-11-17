# Naive Solution to 
# find if count of 
# divisors is even 
# or odd 
import math 

# Function to count 
# the divisors 
def countDivisors(n) : 
	
	# Initialize count 
	# of divisors 
	count = 0

	# Note that this loop 
	# runs till square 
	# root 
	for i in range(1, (int)(math.sqrt(n)) + 2) : 
		if (n % i == 0) : 
			
			# If divisors are 
			# equal,increment 
			# count by one 
			# Otherwise increment 
			# count by 2 
			if( n // i == i) : 
				count = count + 1
			else : 
				count = count + 2

	if (count % 2 == 0) : 
		print("Even") 
	else : 
		print("Odd") 


# Driver program to test above function */ 
print("The count of divisor: ") 
countDivisors(10) 

#This code is contributed by Nikita Tiwari.*/ 
