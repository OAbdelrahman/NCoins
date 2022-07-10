from time import time
import numpy as np

# Algorithm 1: Divide-and-Conquer
def DACcoins(coins, amount):
    if amount == 0: # The base case
        return 0
    
    else: # The recursive case
        minCoins = float("inf")
        for currentCoin in coins: # Check all coins
        # If we can give change
            if (amount - currentCoin) >= 0:
            # Calculate the optimal for currentCoin
                currentMin = DACcoins(coins, amount-currentCoin) + 1
            # Keep the best
                minCoins = min(minCoins, currentMin) 
        return minCoins

# Algorithm 2: Dynamic Programming with Traceback
def DPcoins(coins, amount):
# Create the initial tables and filling base case
    change = [0]*(amount+1)
    winner = [0]*(amount+1)
# Fill in the rest of the table
    for i in range(1, amount+1):
        minimum = float("inf")
        for coin in coins:
            if (i- coin) >= 0:
                minimum = np.minimum(minimum, change[i-coin])
                change[i] = minimum+1
                if change[i-coin] == minimum: 
                    winner[i]= coin
    
    # Perform the traceback to print result
    k = int(change[-1])
    m=i
    while k !=0:
        print(winner[m])
        m = m-winner[m]  
        k-=1

    return int(change[i]) # return optimal number of coins

def main():    
    C = [1,5,10,12,25] # coin denominations (must include a penny)
    A = int(input('Enter desired amount of change: ')) 
    assert A>=0
    print("DAC:") 
    t1 = time()
    numCoins = DACcoins(C,A) 
    t2 = time()
    print("optimal:",numCoins," in time: ",round((t2-t1)*1000,1),"ms")
    print() 
    print("DP:") 
    t1 = time()
    numCoins = DPcoins(C,A) 
    t2 = time()
    print("optimal:",numCoins," in time: ",round((t2-t1)*1000,1),"ms")



if __name__ == "__main__":
    main()

