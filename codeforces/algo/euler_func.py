# int phi (int n) {
# 	int result = n;
# 	for (int i=2; i*i<=n; ++i)
# 		if (n % i == 0) {
# 			while (n % i == 0)
# 				n /= i;
# 			result -= result / i;
# 		}
# 	if (n > 1)
# 		result -= result / n;
# 	return result;
# }

def phi(n):
	result = n
	i = 2
	while i*i <= n:
		if n % i == 0:
			while n % i == 0:
				n /= i
			result -= result / i
		i+=1
	if n > 1:
		result -= result / n
	return int(result)

print(phi(38)) # -> 8