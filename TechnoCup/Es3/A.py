arr = [1, 2, 1, 2, 1, 1]#list(map(int, input().split()))
t1 = 0
t2 = 0
class INIT:
	def __init__(self, arr):
		self.arr = []
		for i in arr:
			self.arr.append({
				"st": 0,
				"val": i
			})

	def getState(self):
		tmp = []
		for i in self.arr:
			if i['st'] != 1:
				tmp.append(i)
		return tmp

	def setLock(self, pos):
		self.arr[pos]['st'] = 1

	def getVal(self, pos):
		return self.arr[pos]['val']
	def reset(self):
		__init__()
	def getVals(self):
		tmp = []
		for i in self.getState():
			tmp.append(i['val'])
		return tmp
def main():
	global t1
	global t2
	data = INIT(arr)
	print(arr)
	print(data.arr)

	i = 0
	while i < len(data.arr):
		data = INIT(arr)
		t1 += data.getVal(i)
		data.setLock(i)
		j = 0
		while j < len(data.getState()):
			t1 += data.getVal(j)
			data.setLock(j)
			c = 0
			while c < len(data.getState()):
				t1 += data.getVal(j)
				data.setLock(j)
				for k in data.getVals():
					t2 += k
				if t1 == t2:
					break
				c+=1
			j += 1
		i += 1

	if t1 == t2:
		print("YES")
	else:
		print("NO")
	
if __name__ == "__main__":
	main()