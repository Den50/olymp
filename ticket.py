import math
STR = input()
def summ(str):
	tmp= []
	res = 0
	for i in str:
		tmp.append(int(i))
	for i in tmp:
		res += i
	return res
def main():
	str1 = [STR[0:math.floor(len(STR) / 2)], STR[math.floor(len(STR) / 2):len(STR)]]
	str2 = [STR[0:math.ceil(len(STR) / 2)], STR[math.ceil(len(STR) / 2):len(STR)]]

	if summ(str1[0]) == summ(str1[1]):
		print("YES")
	elif summ(str2[0]) == summ(str2[1]):
		print("YES")
	else:
		print("NO")

if __name__ == "__main__":
	main()