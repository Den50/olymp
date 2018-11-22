n, k = map(int, input().split())

# n, k = 7, 20
10 11
5



if k // 2 + 1 > n:
	print(0)
elif k // 2 + 1 == n:
	print(1)
else:
	t_anses = [1, k - 1]
	anses = []
	j = 0
	while t_anses[0] + 1 < t_anses[1]:
		if t_anses[0] <= n and t_anses[1] <= n:
			# print(t_anses)
			anses.append(t_anses)

		t_anses[0]+=1
		t_anses[1]-=1
		j+=1
	print(len(anses)+1)