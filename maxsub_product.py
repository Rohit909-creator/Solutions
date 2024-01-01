class Solution:

    def maxsubarr(self, nums: list):

        res = max(nums)
        curMin, curMax = 1, 1

        for num in nums:

            if num == 0:
                curMax = 1
                curMin = 1
                continue

            tmp = curMax*num
            curMax = max(curMax*num, curMin*num, num)
            curMin = min(tmp, curMin*num, num)

            res = max(res, curMax, curMin)

        return res
    
if __name__ == "__main__":

    S = Solution()
    nums = [1,2,-3,4]
    print("result:",S.maxsubarr(nums))
