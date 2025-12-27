class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        for r in range(len(nums)):
               if nums[r] : 
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
               r += 1
        return nums
        
        # Initiate left and right pointer and when right pointer is pointed at a non zero shift it with left pointer pointer
        # Now increment the left pointer once swap is made to the next number