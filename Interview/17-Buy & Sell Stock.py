# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Using element comparison

    def maxProfit(self, prices):

        low = float('inf') # set initial low price to be infinite 
        profit = 0 # set profit to be 0 
        for price in prices:
            if price < low:  # detect current price are lower than low
                low = price 
            else:  # detect current price are higher
                profit = max(price-low, profit) # compare the current difference and previous max profit
        return profit

Dynamic programming

    def maxProfit(self, prices):
    
        fb, fs = float('inf'), 0
        for price in prices:
            fb = min(fb, price) # keep minimal
            fs = max(fs, price-fb) # compute max difference
        return fs