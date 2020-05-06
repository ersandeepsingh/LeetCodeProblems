def majorityElement(self, nums: List[int]) -> int:
        num={}
        n=len(nums)
        for i in nums:
            num[i] = num.get(i, 0) + 1
        print(num)
        for key,value in num.items():
            if(num[key] > n/2):
                print (key)
                return (key)
        return 0


# one pass + dictionary
def majorityElement2(self, nums):
    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] = 1
        if dic[num] > len(nums)//2:
            return num
        else:
            dic[num] += 1 