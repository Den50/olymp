# k = int(input())
k = 5
def main():
	b1 = 1
	ans = 0
	arr = []
	i = 0
	while i < k:
		arr.append(b1)
		b1 *= 2
		i+=1
	for j in arr:
		ans += j
	print(ans)
if __name__ == "__main__":
	main()