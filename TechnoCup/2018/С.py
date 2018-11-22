# n = int(input())
# _str = input()

n = 5
_str = "73452"

def summ(s):
	summ = 0
	for i in s:
		summ += int(i)

	return summ

length = 1
_summ = 0
for i in range(n):
	_summ = summ(_str[i:length])
	for j in range(length, n):
		print(j)
	length+=1
