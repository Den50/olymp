<<<<<<< HEAD
# n = int(input())
# k = int(input())
# a = int(input())
# b = int(input())


if k == 1:
	print((n - 1) * a)
else:
	x = n
	ans = 0
	while x > 1:
		if x == 1:
			break
		if x >= k:
			if x % k == 0 and (b < a * (x / k)):
				ans += b
				x /= k
			elif x % k == 0 and (b > a * (x / k)):
				ans += a
				x -= 1
			else:
				ans += a
				x -= 1
		else:
			ans += (x - 1) * a
			break
	print(int(ans))
=======
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
>>>>>>> ed48be475c5c726ee315f0070e023120b5feb4ea
