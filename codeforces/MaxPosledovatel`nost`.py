#http://codeforces.com/problemset/problem/888/E
n, m = map(int, input().split())
arr = list(map(int, input().split()))

def MaxPos(arr):
	arr1 = []
	for i in arr:
		arr1.append(i % m)
	return max(arr1)
def ArrPos(arr):
	i = 0
	arr1 = []
	# 1 проход
	while i < len(arr):
		arr1.append(arr[i] + arr[i+1]) if i != len(arr) - 1 else arr1.append(arr[i])
		i+=1
	return arr1

def main():
	ans = 0
	for i in arr:
		if i % m == m - 1:
			ans = i % m
		else:
			ans = MaxPos(ArrPos(arr))
	print(ans)
if __name__ == "__main__":
	main()
