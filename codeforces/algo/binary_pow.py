def binpow(a, n):
	res = 1
	i=0 # for debug
	while n:
		print(i, n)
		if n & 1:
			res *= a
			n-=1
		else:
			a *= a
			n >>= 1
		i+=1 # for debug
	return res

print(binpow(2, 10)) # -> 1024

print(16 & 1)