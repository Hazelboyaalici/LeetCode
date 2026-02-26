class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newlist=[]
        
        for i in range (len(nums)-1):
            value= nums[i]
            searchingValue = target - value
            for j in range(i+1, len(nums)):
                if nums[j]== searchingValue:
                    newlist.append(i)
                    newlist.append(j)
            

        return newlist
