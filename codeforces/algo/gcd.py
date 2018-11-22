def gcd(a, b):
	# print(a, b)
	if b != 0: 
		return gcd(b, a % b) 
	else: 
		return a
	
print(gcd(10, 7))
