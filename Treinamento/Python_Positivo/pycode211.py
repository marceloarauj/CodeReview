# Python code to find the minimum number 
# of jump required to reach 
# (d, 0) from (0, 0) 

def minJumps(a, b, d): 
	
	temp = a 
	a = min(a, b) 
	b = max(temp, b) 
	
	if (d >= b): 
		return (d + b - 1) / b 
	
	# if d is 0 
	if (d == 0): 
		return 0

	# if d is equal to a. 
	if (d == a): 
		return 1

	# else make triangle, and only 2 
	# steps required. 
	return 2
		
# main() 
a = 3
b = 4
d = 11
print (int(minJumps(a, b, d))) 

# Contributed by _omg 
