n, m = map(int, input().split())
arr = []

# n, m = 5, 6
# arr = [
# 	"WWWWWW",
# 	"WWWBBB",
# 	"WWWBBB",
# 	"WWWBBB",
# 	"WWWWWW",
# ]
for i in range(n):
	arr.append(input())

count = 0
start = False

#WWBBBW
#WWBbBW
#WWBBBW
#WWWWWW
#WWWWWW
k = 0
r_index = 0
c_index = 0
for i in arr:
	s_index = i.find("B")
	f_index = i.rfind("B")
	k+=1
	if s_index == -1:
		continue
	else:
		r_index = (s_index + f_index) // 2 + 1
		c_index = k - count // 2
		count+=1

print(c_index, r_index)
