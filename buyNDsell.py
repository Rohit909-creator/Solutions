import matplotlib.pyplot as plt



class Solution:

    def maxProfit(self, prices:list):

        l,r = 0,1
        maxp = 0

        while r < len(prices):

            if prices[l] < prices[r]:

                profit = prices[r] - prices[l]
                maxp = max(profit, maxp)
                
            else:
                l = r
            
            r+=1

        return maxp
    
if __name__ == "__main__":

    S = Solution()
    prices = [5,6,7,9,2,10,20]

    maxp = S.maxProfit(prices)
    print(f"Max profit: {maxp}")
    plt.plot([_ for _ in range(1, len(prices)+1)], prices)
    plt.show()