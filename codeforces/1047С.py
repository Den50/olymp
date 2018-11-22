import math
# n = int(input())
# arr = list(map(int, input().split()))

# print(arr)
arr = [8, 6, 7, 3, 7]
arr = sorted(arr)

def gcdNum(a, b):
	# print(a, b)
	if b != 0: 
		return gcdNum(b, a % b) 
	else: 
		return a


def gcd(arr):
	if len(arr) == 0:
		return 0
	if len(arr) == 1:
		return arr[0]
	res = gcdNum(arr[0], arr[1])
	i = 2
	while i < len(arr) and res != 1:
		res = gcdNum(res, arr[i])
		i+=1
	return res

# int simple(int n)
# {
#     if(n<=1)
#         return 0;
 
#      for (int i = 2; i<=sqrt(n); i++)
#           if (n % i == 0)
#             return 0;
 
#      return 1;
# }
def simple(n):
	if n < 1:
		return False
	for i in range(2, math.ceil(math.sqrt(n)) + 1):
		if n % i == 0:
			return False

	return True

indexes = []
k = 0
for i in arr:
	if simple(i):
		indexes.append(k)
	k+=1



i = 0
res = gcd(arr)
if res == 1:
	arr.pop((i for i in indexes))
ans = 0

while i < len(arr):

	nex = gcd(arr[i:])
	print(nex, arr[i:])
	if res < nex:
		ans = i
		break
	i+=1

if ans != 0:
	print(ans)
else:
	print(-1)