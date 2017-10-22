a = int(input())
def main():
	res = 0
	if a <= 0:
		print("Ошибка ввода")
	else:
		res = a
		while res != 1:
			if res % 2 == 0:
				res = res / 2
				if res == 1:
					break
			if res % 2 == 1:
				res = (res * 3 + 1) / 2
				if res == 1:
					break
		if res == 1:
			print("Гипотеза верна")
		else:
			print("Гипотеза неверна")
				

if __name__ == "__main__":
	main()