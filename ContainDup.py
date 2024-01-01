import time

class Solution:

    def checkdup(self, nums: list):

        strt = time.time()

        l,r = 0,1

        nums_sorted = sorted(nums)

        while r < len(nums_sorted):

            if nums_sorted[l] == nums_sorted[r]:
                end = time.time() - strt

                return True, end
            
            l+=1
            r+=1

        end = time.time() - strt
        return False, end
    

    def checkdup_HashSet(self, nums: list):

        hashset = set()
        strt = time.time()
        for val in nums:
            
            if val in hashset:
                end = time.time() - strt
                return True, end
            
            else:
                hashset.add(val)
        end = time.time() - strt
        return False, end

if __name__ == "__main__":

    S = Solution()

    nums = [1,2,3,1]

    print(f"output: {S.checkdup(nums)}")
    print(f"output: {S.checkdup_HashSet(nums)}")

        