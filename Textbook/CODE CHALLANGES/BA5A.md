# Find the Minimum Number of Coins Needed to Make Change
## Problem
The Change Problem
Find the minimum number of coins needed to make change.

Given: An integer money and an array Coins of positive integers.

Return: The minimum number of coins with denominations Coins that changes money.


```python
def DPChange(money, coins):
    MinNumCoins = [0]
    for i in range(1,money+1):
        MinNumCoins.append(1e9)
        for coin in coins:
            if i >= coin and MinNumCoins[i-coin]+1 < MinNumCoins[i]: MinNumCoins[i] = MinNumCoins[i-coin]+1
    
    return MinNumCoins[money]

N, coins = input().split()
coins = list(map(int,coins.split(',')))

print(DPChange(int(N),coins))
```

    19891 9,5,3,1
    2211



```python

```
