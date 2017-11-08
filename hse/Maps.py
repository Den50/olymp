"""

Решение олимпиады по информатике hse
https://olymp.hse.ru/data/2016/10/05/1122855045/%D0%94%D0%B5%D0%BC%D0%BE%20%D0%BE%D1%82%D0%B1%D0%BE%D1%80%D0%B0%202016-2017.pdf

"""

import re
first = re.compile(r'/\\')
middle = re.compile('(r(.*?)l)|(l(.*?)r)')
last = re.compile(r'\\/')

count = 0
def Regfirst(str):
	return len(re.findall(first, str))

def Regmiddle(str):
	_str = str.replace('/', 'r').replace('\\', 'l')
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