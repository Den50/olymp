import math

n = int(input())

arr = []

for i in range(n):
	arr.append(list(map(int, input().split())))

# n = 2

# arr = [
# 	[1, 7],
# 	[6, 3],
# 	[3, 7],
# ]

state = 1
path = 0

for i in arr:
	a, b = i

	# print(math.fabs(a - state))
	path += math.fabs(a - state)
	state = a
	path += 1
	path += math.fabs(a - b)
	state = b
	path += 1


# print(arr)
print(int(path))