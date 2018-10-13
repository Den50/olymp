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
	i = len(s) - 1
	j = 0
	arr = []
	while j < i:
		if len(arr) != 0:
			break
		else:
			start1 = j
			end1 = j + k
			s1 = s[start1:end1]
			l = end1
			while l < i:
				start2 = l
				end2 = l + k
				s2 = s[start2:end2]
				_str = "".join([s1, s2])
				if _search(t, _str) != -1:
					arr = [start1 + 1, start2 + 1]
					break
				l+=1
		j+=1
	return arr

arr = Puts(s, k)

if len(arr) == 0:
	print("No")
else:
	print("Yes")
	print(arr[0], arr[1])