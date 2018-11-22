q, n = map(int, input().split())
arri = []

for i in range(n):
	arri.append(int(input()))


arr = []

for i in range(1, q+1):
	arr.append(i)
	arr.append("-")
del arr[len(arr) - 1]


l = len(arr) - 1
while l + 1 > q:
	last = arr[l]
	i = l-1
	while i >= 0:
		if arr[i] == "-":
			mid = i
			break
		else:
			pass
		i-=1
	arr[mid] = last
	del arr[l]
	l-=1

for i in arri:
	print(arr[i - 1])