def singleNonDuplicate(self, nums: List[int]) -> int:
	num = 0
	for i in nums:
		num ^= i
	return num