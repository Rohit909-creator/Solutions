# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:

#         if target != 0:
#             elements = self.sort(nums, target)
#         else:
#             elements = nums
#         print(elements)
#         solution = set()
#         # solution = []
#         for idx,i in enumerate(elements):
#             for j in elements[idx+1:]:
#                 # print("Sum",i+j)
#                 s = i+j
#                 # print("idx",idx)
#                 if s == target:
#                     idx1 = nums.index(i)
#                     idx2 = nums.index(j)
#                     if i == j:
#                         idx2 = nums.index(i, idx1+1)
#                     solution.add(idx1)
#                     solution.add(idx2)
#                     # solution.append(idx1)
#                     # solution.append(idx2)
#         print("solution:", solution)

#     def sort(self, nums, target):
#         elements = []
#         for element in nums:
#             if element <= target:
#                 elements.append(element)
#         return elements

class Solution:

    def twoSum(self, nums: list, target: int) -> list:

        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target-nums[i]
            print(complement)
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i
        return []




if __name__ == "__main__":
    S = Solution()
    out = S.twoSum([-3,4,3,90], 0)
    print(out)