class Solution:

    def solve(self, array: list):

        result = []
        pre = 1
        for i, val in enumerate(array):
            result.append(pre)
            pre = val*pre

        print(result)

        post = 1

        for i, val in enumerate(reversed(array)):
            result[len(result)-i-1] = post*result[len(result)-i-1]
            post *= val
        print(result)

if __name__ == "__main__":

    S = Solution()

    array = [1,2,3,4]

    S.solve(array)