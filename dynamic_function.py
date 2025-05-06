def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    prev = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev[i] = coin

    result = {}
    curr = amount
    while curr > 0:
        coin = prev[curr]
        result[coin] = result.get(coin, 0) + 1
        curr -= coin

    return result

if __name__ == "__main__":
    print(find_min_coins(113))
