n = int(input())
arr = list(map(int, input().split()))
def main():
	i = 0
	ans = 0
	while i < len(arr):
		first = 0
		last = len(arr) - 1
		if i != first and i != last:
			if (arr[i] < arr[i - 1] and arr[i] < arr[i + 1]) or (arr[i] > arr[i - 1] and arr[i] > arr[i + 1]):
				ans += 1
		i+=1
	print(ans)

if __name__ == "__main__":
	main()