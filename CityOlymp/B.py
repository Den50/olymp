# X = 45345
# s1 = 6
# s2 = 9
X, s1, s2 = map(int, input().split())
def ToTen(n, s1):
	tmp_str = str(n)
	tmp_arr = []
	for i in tmp_str:
		tmp_arr.append(int(i))
	tmp_rev = list(reversed(tmp_arr))
	i = 0
	ans = 0
	while i < len(tmp_rev):
		ans += tmp_rev[i] * s1 ** i
		i+=1
	return ans
def Tos(n, s2):
	tmp_global = 0
	ans = []
	_tmp = n
	while True:
		# n - ((n // s2) * s2)
		ans.append(_tmp - ((_tmp // s2) * s2))
		_tmp = _tmp // s2
		if _tmp < s2:
			ans.append(_tmp)
			break

	return list(reversed(ans))
def ToStr(arr):
	ans = ""
	for i in arr:
		ans += str(i)
	return ans
def main():
	if s2 == 10:
		print(ToTen(X, s1))
	else:
		# print(Tos(ToTen(X, s1), s2))
		print(ToStr(Tos(ToTen(X, s1), s2)))
if __name__ == "__main__":
	main()