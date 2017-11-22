#http://codeforces.com/problemset/problem/894/A
str1 = input()
tmp = "QAQ"
def main():
	ans = 0
	i = 0
	while i < len(str1):
		if str1[i] == "Q":
			j = i + 1
			while j < len(str1):
				if str1[j] == "A":
					k = j + 1
					while k < len(str1):
						if str1[k] == "Q":
							ans+=1
						k+=1
				j+=1
		i += 1
	print(ans)

if __name__ == "__main__":
	main()
