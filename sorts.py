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


def choiceSort(alist):
	for end_pointer in range(len(alist)-1, 0, -1):
		loc_max = 0
		for pos in range(1, end_pointer+1):
			if alist[pos] > alist[loc_max]:
				loc_max = pos
		alist[end_pointer], alist[loc_max] = alist[loc_max], alist[end_pointer]
	return alist


def myInsertSort(alist):
	for iter_num in range(1, len(alist)):
		flag = False
		temp = alist[iter_num]
		for i in range(iter_num-1, -1, -1):
			tmp2 = alist[i]
			if tmp2 > temp:
				alist[i+1] = alist[i]
				if i == 0:
					alist[0] = temp
				flag = True
			if tmp2 < temp and flag:
				alist[i+1] = temp
				break
			if tmp2 < temp:
				break
	return alist


def get_rand_mass(size):
	res = list()
	for i in range(size):
		res.append(random.randint(0, 100))
	return res


if __name__ == "__main__":
	rand_mass = get_rand_mass(9)
	print(rand_mass)
	# print('bubble sort: ', bubbleSort(rand_mass))
	# print('bubble sort2: ', bubbleSort2(rand_mass))
	# print('choiceSort: ', choiceSort(rand_mass))
	print('insertSort: ', myInsertSort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
