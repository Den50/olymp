import itertools
arr = list(map(int, input().split()))
rn = range(6)

def othersIters(arr):
	_arr = set(rn)
	return list(_arr.symmetric_difference(arr))

t = False
for i in list(itertools.combinations(rn, 3)):
	summ1 = sum((arr[j] for j in i))
	summ2 = sum((arr[j] for j in othersIters(i)))
	if summ1 == summ2:
		t = True
		break
if t:
	print("YES")
else:
	print("NO")

