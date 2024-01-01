class Solution:

    def solve(self, array: list):

        maxsub = array[0]
        cursum = 0

        for num in array:

            if cursum < 0:
                cursum = 0

            cursum += num
            maxsub =  max(maxsub, cursum)

        return maxsub

if __name__ == "__main__":

    S = Solution()

    array = [-2,1,-3,4,-1,2,1,-5,4]

    print(f"output: {S.solve(array)}")