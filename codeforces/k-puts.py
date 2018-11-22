import re
*first, k = map(int, input().split())
s = input()
t = input()


def _search(_t, _s):
	m = re.search(_t, _s)
	try:
		return m.span()
	except:
		return -1

def Puts(s, k):
	i = len(s) - 2 * k
	j = 0
	indexes = set()
	while i > j:
		s1 = s[0:k]
		s2 = s[k+1+j:2*k+1+j]
		_str = "".join([s1, s2])
		if _search(t, _str) != -1:
			indexes = _search(t, _str)
		j+=1
	if len(indexes) == 0:
		i = len(s) - 2 * k
		j = 0
		while i > j:
			s1 = s[j:k+j]
			s2 = s[k+1+j:2*k+1+j]
			_str = "".join([s1, s2])
			if _search(t, _str) != -1:
				indexes = _search(t, _str)
			j+=1
		return indexes
	else:
		return indexes


arr = Puts(s, k)

if len(arr) == 0:
	print("No")
else:
	print("Yes")
	print(arr[0], arr[1])