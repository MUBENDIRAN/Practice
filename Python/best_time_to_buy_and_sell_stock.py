# this function holds the operation of getting min and max values of the stock and profit earned 
def buy_sell(prices):
    min_val = float('inf') # initial edge case handling min value 
    max_val = 0 # initial edge case handling max value 

    for price in prices:
        if price < min_val: # if the current stock value is lesser than past new min value is added by replacing the old
            min_val = price
        else:
            profit = price - min_val # else its gets subtracted and profit value is obtained 
            max_val = max(max_val,profit) # it is compared with previous max value if its maximum than previous max value is replaced with current

    return max_val
# custom input 
prices = list(map(int,input("Enter the stock values : ").split()))
print("Profit gained :",buy_sell(prices))