"""

Решение олимпиады по информатике hse

"""

import re
first = re.compile(r'/\\')
middle = re.compile('(r(.*?)l)|(l(.*?)r)')
last = re.compile(r'\\/')

count = 0
def Regfirst(str):
	return len(re.findall(first, str))

def Regmiddle(str):
	_str = str.replace('/', 'r')
	_str = _str.replace('\\', 'l')
	ren = 0
	arr = re.findall(middle, _str)
	j = 0
	for i in arr:
		if i[j] != '':
			ren += len(i[1]) + 1
		elif i[j] == '':
			ren += len(i[3]) + 1
		j+=1
	return ren


def Reglast(str):
	return len(re.findall(last, str))
#(/.*?\\)|(\\.*?/)

n, m = map(int, input().split())
for i in range(n):
	str = input()
	if i == 0:
		count += Regfirst(str)
	elif i == n - 1:
		count += Reglast(str)
	else:
		count += Regmiddle(str)
print(count)