class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # we need to have a pointer and in this case its called k 

        k = 0 

        # we are going to iterate through the nums array 

        for num in nums: 
            if num != val: 
                nums[k]= num 
                k+=1
        return k 
    