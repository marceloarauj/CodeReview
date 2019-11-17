# Python code to find highest 
# K-digit number divisible by X 

def answer(X, K): 
	
	# Computing MAX 
	MAX = pow(10, K) - 1
	
	#returning ans 
	return (MAX - (MAX % X)) 

X = 30; 
K = 3; 

print(answer(X, K)); 

# Code contributes by Mohit Gupta_OMG <(0_o)> 
