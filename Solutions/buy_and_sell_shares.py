# Say you have an array for which the ith element is the price of a given stock on day i.


def maxProfit(prices):
    max_v = min_v = prices[0]
    max_profit=0
    profit=[0]*3
    l=len(prices)

    for i in range(1,l):
        if prices[i]>max_v:
            max_v=prices[i]
            profit=[min_v,max_v,max_v-min_v]
        if min_v>prices[i]:
            min_v=max_v=prices[i]

        max_profit = max(max_profit, profit[2])
    print(max_profit)


#N=[3,2,3,1,2]
N=[1,2,3,4,5,4,3,2,1]
maxProfit(prices=N)
