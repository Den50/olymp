"""

Школьная олимпиада по информатике

"""
#inputs_Start
n = int(input())
arr = []
for i in range(n):
	arr.append(int(input()))
#inputs_End

def copyArr(_arr):
	tmp = []
	for i in _arr:
		tmp.append(i)
	return tmp
################################################
ans = []

def main():
	Arr = copyArr(arr)
	j = 0
	for i in arr:
		tmp = int(i * 0.75)
		for p in Arr:
			if p == tmp:
				global ans
				ans.append(p)
		j+=1
	#####ANSWER
	ans = sorted(ans)
	for i in ans:
		print(i)


if __name__ == "__main__":
	main()