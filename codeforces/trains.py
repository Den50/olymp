# Generate array with nums trains
arr = list(([] for i in range(9)))
i = 0
k = 0
while i < 36:
	if i % 4 == 0 and i != 0:
		k+=1
	arr[k].append(i+1)
	# print(k, i)
	i+=1

i = 54
k=0
while i > 36:
	if i % 2 == 0 and i != 54:
		k+=1
	arr[k].append(i)
	# print(k, i)
	i-=1

empty = list((0 for i in range(9)))

# input
n = int(input())
for i in range(n):
	i = int(input())
	k = 0
	for p in arr:
		if i in p:
			empty[k]+=1
			break
		k+=1

print(empty.count(6))
