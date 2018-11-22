n = int(input())

arr = list(map(int, input().split()))
# n = 3
# arr = [2, 2, 2]

def step1(arr):
	i = arr.index(max(arr))
	_arr = arr
	del _arr[i]
	return _arr

def step2(arr):
	i = arr.index(min(arr))
	_arr = arr
	del _arr[i]
	return _arr
	
if len(arr) > 1:
	while(True):
		if len(arr) > 2:
			step1(arr)
			step2(arr)
		elif len(arr) == 2:
			step1(arr)
		else:
			print(arr[0])
			break
else:
	print(arr[0])


# print(arr)