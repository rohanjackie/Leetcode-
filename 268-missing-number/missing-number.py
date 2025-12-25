class Solution:
    def missingNumber(self, nums: List[int]) -> int:
            res = len(nums)

            for i in range(len(nums)):
                res += (i - nums[i])

            return res
                





        # # res = len(nums)

        # # [3,0,1]
        # # i = 0, 1, 2

        # # 0-3, = -3   3+ -3 = 0 

        #   1-0, = 1    0 + 1 = 1

        # # 2-1  = 1    1 + 1 = 2        i - nums[i]


               

        