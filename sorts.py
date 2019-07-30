import random


def bubbleSort(alist):
	length = len(alist)
	for i in range(length - 1):
		for j in range(length - 1 - i):
			if alist[j] > alist[j+1]:
				alist[j], alist[j+1] = alist[j+1], alist[j]
	return alist


def bubbleSort2(alist):
	exchanges = True
	for p in range(len(alist)-1, 0, -1):
		exchanges = False
		for i in range(p):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
				exchanges = True
		if not exchanges:
			print("no exchanges")
			return alist
	return alist


def get_rand_mass(size):
	res = list()
	for i in range(size):
		res.append(random.randint(0, 100))
	return res

if __name__ == "__main__":
	rand_mass = get_rand_mass(10)
	print(rand_mass)
	print('bubble sort: ', bubbleSort(rand_mass))
	print('bubble sort2: ', bubbleSort2(rand_mass))
