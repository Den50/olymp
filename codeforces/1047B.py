n = int(input())
arr = []
for i in range(n):
	arr.append(tuple(map(int, input().split())))


print(max([i[0] + i[1] for i in arr]))