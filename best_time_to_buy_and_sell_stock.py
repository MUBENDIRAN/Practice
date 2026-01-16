def buy_sell(prices):
    min_val = float('inf')
    max_val = 0

    for price in prices:
        if price < min_val:
            min_val = price
        else:
            profit = price - min_val
            max_val = max(max_val,profit)

    return max_val

prices = list(map(int,input("Enter the stock values : ").split()))
print("Profit gained :",buy_sell(prices))