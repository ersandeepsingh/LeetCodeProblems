def isPerfectSquare(self, num: int) -> bool:
	x = num ** (1/2)
	if(int(x) ** 2 == num):
		return True
	return False