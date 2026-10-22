class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count= 0 
        current_count = 0 
        # we consider using a single loop instead of using a nested loop due to time complexity 
        # for single loop we are only using O(n) insted of O(n2)

        for i in nums: 
            if i ==1 : 
                current_count +=1
                # the decision making (if else conditional statemnet)
                if current_count>max_count: 
                    max_count= current_count 
            
            # we are goint to use a else here to stop the streak of 1 when we see a 0 and reset the current_count to be 0 
            else: 
                current_count = 0 
        # we need to return the max count at the end of the function 
        return max_count


            

