import random
import timeit
# t = timeit.Timer('min_search()', 'from __main__ import min_search')
# print(t.timeit(number=100))


def min_search():
	massive = list()
	for i in range(10):
		massive.append(random.randint(1, 100))
	print(massive)
	min = massive.pop()
	for i in massive:
		if i < min:
			min = i
	print(min)


def sequentionalSearch(alist, item):
	for elem in alist:
		if elem == item:
			return True
	return False


def binarySearch(alist, item):
	while True:
		if len(alist) == 1:
			if alist[0] == item:
				return True
			else:
				return False
		middle = len(alist)//2
		if alist[middle] == item:
			return True
		else:
			if alist[middle] > item:
				alist = alist[:middle]
			else:
				alist = alist[middle:]


def binarySearch2(alist, item):
	first = 0
	last = len(alist) - 1
	found = False

	while first <= last and not found:
		middle = (first + last) // 2
		if alist[middle] == item:
			found = True
		else:
			if item > alist[middle]:
				first = middle + 1
			else:
				last = middle - 1
	return found


def binaryRecurseSearch(alist, item):
	if len(alist) == 0:
		return False
	else:
		middle = len(alist) // 2
		if alist[middle] == item:
			return True
		else:
			if item < alist[middle]:
				return binaryRecurseSearch(alist[:middle], item)
			else:
				return binaryRecurseSearch(alist[middle+1:], item)


if __name__ == "__main__":
	print(binaryRecurseSearch([1, 2, 3, 4, 5], 1))
