import os


def fibo(n):
	if n == 0:
		return 1
	else:
		return n*fibo(n-1)

if __name__ == "__main__":
	print(fibo(3))
