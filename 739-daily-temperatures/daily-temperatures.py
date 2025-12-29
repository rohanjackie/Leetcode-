class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  #temp:index

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = (i - stackIdx)
            stack.append([t,i])
        return res




        # we need to have an answer array and a stack. 
        # The stack will add the given array values and check the top of the stack to see if the value coming next is greater than the previous value
        # If the value is greater we check the distance and record that in the answer array. 
        # If the value occuring next is smaller we don't record anything in the answer array and move to the next value to check for a bigger value
        # If a previous value is small and is not popped yet wait for a higher value to appear and then record the distance in the answer array

        # [73,74,75,71,69,72,76,73]
        
        # Output array = [1,1,4,2,1,1,0,0]
        # stack = [73,74,75,69,72,76,73]
                #   /, /, blank, blank, /(pop 69 check 72 and 75 72<75 so wait 72>72 so record that distance), /,/(pop 72 and also record the distance for 76>71),
                # 73<76 so record as 0 as array ends
