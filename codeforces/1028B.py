# n, m = map(int, input().split())
n, m = 8, 16

def s(x):
	x = str(x)
	ans = 0
	for i in range(len(x)):
		ans += int(x[i])
	return ans

def uns(x):
	if x % 2 == 0:
		return [int(x / 2), int(x / 2)]
	else:
		return [x // 2, x // 2 + 1]

# s(a) >= n
# s(b) >= n
# s(a + b) <= m
a = b = n
k = 0
while s(a) >= n and s(b) >= n and s(a + b) <= m:
	print(a, b)
	if k % 2 == 0:
		a+=1
	else:
		b+=1
	k+=1