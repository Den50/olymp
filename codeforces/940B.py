n = int(input())
k = int(input())
a = int(input())
b = int(input())

# n = 9
# k = 2
# a = 3
# b = 1

ans = 0

x = n
while x > 1:
	if x % k == 0:
		x /= k
		ans += b
	else:
		x-=1
		ans += a

print(min((n - 1) * a, ans))