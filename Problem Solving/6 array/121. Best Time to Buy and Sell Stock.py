prices = [7,1,5,3,6,4]
n = len(prices)
min_element = prices[0]
profit = 0
for i in range(1,n):
    cost = prices[i] - min_element
    min_element = min(min_element,prices[i])
    profit = max(profit,cost)
print(profit)

