#http://codeforces.com/problemset/problem/892/A
n = int(input())
arrNow = list(map(int, input().split()))
arrFull = list(map(int, input().split()))

def LastTwo(arr):
	one = arr[len(arr) - 1]
	two = arr[len(arr) - 2]
	return [two, one]


def main():
	summNow = 0
	summFull = 0
	global arrFull
	# Fullglobal arr
	for i in arrNow:
		summNow += i
	arrFull = sorted(arrFull)
	summFull += LastTwo(arrFull)[0]
	summFull += LastTwo(arrFull)[1]
	if summNow <= summFull:
		print("YES")
	else:
		print("NO")

if __name__ == "__main__":
	main()
