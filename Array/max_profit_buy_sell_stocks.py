"""
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
"""

#Solution 1 

def max_profit(prices):
    buy_pointer =   0
    sell_pointer    =   0
    l = len(prices)-1
    total_profit = 0
    if prices and l > 0:
        sell_pointer+=1
        while(sell_pointer<=l):
            if sell_pointer ==  l :
                if prices[buy_pointer]<prices[sell_pointer]:
                    total_profit += prices[sell_pointer] - prices[buy_pointer] 
                    return total_profit
                else:
                    return total_profit
            if prices[buy_pointer]<=prices[sell_pointer] :
                if prices[sell_pointer] > prices[sell_pointer+1]:
                    total_profit += prices[sell_pointer] - prices[buy_pointer] 
                    buy_pointer =   sell_pointer+1
                    sell_pointer += 2
                else:
                    sell_pointer += 1
            elif prices[buy_pointer]>prices[sell_pointer]:
                buy_pointer =   sell_pointer
                sell_pointer+=1
        return total_profit
    return 0

print(max_profit(prices=[1,7,4,2]))

