# n = int(input())
# arr = []
# for i in range(n):
# 	arr.append(list(map(int, input().split())))

n = 6
arr = [[1, 4],
[9, 9],
[5, 7],
[12, 29],
[137, 591],
[1, 1000000]]

def GenerateStep(n):
	a = 2
	p = 2
	arr = set()
	while a ** p <= n:
		p = 1
		while (a + 1) ** p <= n:
			print(a)
			print(p)
			arr.add(a ** p)
			p+=1
		a+=1
		p+=1
	return sorted(arr)

print(GenerateStep(10000))


# for i in range(n):
# 	print(arr[i])
# 	a = 1
# 	p = 2
# 	ans = 0
# 	while a ** p <= arr[i][1]:
# 		if a ** p >= arr[i][0] and a ** p <= arr[i][1]:
# 			ans += 1
# 		a+=1
# 	a = 2
# 	p = 2
# 	while a ** p <= arr[i][1]:
# 		if a ** p >= arr[i][0] and a ** p <= arr[i][1]:
# 			ans += 1
# 		p+=1
# 	print(ans)
