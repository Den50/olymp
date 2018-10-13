l, r, a = map(int, input().split())

ans = 0

"""
1 4 2  =>  6
5 5 5  =>  14
0 2 0  =>  0
"""

if l < r and a != 0:
	sub = r - l
	if sub - a > 0:
		ans = (l + a) * 2
	elif sub - a == 0:
		ans = r * 2
	else:
		_sub = a - sub
		ans = (r +_sub // 2) * 2

elif l > r and a != 0:
	sub = l - r
	if sub - a > 0:
		ans = (r + a) * 2
	elif sub - a == 0:
		ans = l * 2
	else:
		_sub = a - sub
		ans = (l +_sub // 2) * 2
elif l == r and a != 0:
	isy = a // 2
	ans = (l + isy) * 2
elif a == 0:
	_min = min([l, r])
	ans = _min * 2

print(ans)