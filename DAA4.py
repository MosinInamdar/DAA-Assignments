# Memoization approach for 0/1 Knapsack in Python
def knapsack(wt, val, W, n, t):
    # Base conditions
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]

    # Choice diagram code
    if wt[n-1] <= W:
        t[n][W] = max(
            val[n-1] + knapsack(wt, val, W - wt[n-1], n - 1, t),
            knapsack(wt, val, W, n - 1, t)
        )
    else:
        t[n][W] = knapsack(wt, val, W, n - 1, t)

    return t[n][W]

# Driver code
if __name__ == '__main__':
    # Taking user input for number of items
    n = int(input("Enter the number of items: "))

    # Taking user input for profits and weights
    profit = []
    weight = []
    for i in range(n):
        p = int(input(f"Enter profit for item {i+1}: "))
        w = int(input(f"Enter weight for item {i+1}: "))
        profit.append(p)
        weight.append(w)

    # Taking user input for knapsack capacity
    W = int(input("Enter the maximum weight of the knapsack: "))

    # Initialize the memoization matrix with -1
    t = [[-1 for i in range(W + 1)] for j in range(n + 1)]

    # Function call
    max_profit = knapsack(weight, profit, W, n, t)
    print(f"Maximum profit in the knapsack: {max_profit}")
