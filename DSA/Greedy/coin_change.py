def MinimumCoins(coins, amount):
        pointer = len(coins)-1
        count = 0
        while (amount > 0 and pointer >= 0):
            print(amount, coins[pointer], count)
            if(amount >= coins[pointer]):
                amount -= coins[pointer]
                count += 1
            else:
                pointer -= 1
        if amount == 0:
            print("Minimum coins required:", count)
        else:
            print("Not possible to make the amount with given coins")
            count = -1

MinimumCoins([1, 5, 10, 25], 63)
# Output: Minimum coins required: 6     
# Explanation: 63 = 25 + 25 + 10 + 1 + 1 + 1
# The minimum number of coins required to make 63 is 6.
