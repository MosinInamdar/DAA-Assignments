# Structure for an item which stores weight and value
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

# Main greedy function to solve fractional knapsack problem
def fractionalKnapsack(W, arr):
    # Sort items based on the profit-to-weight ratio in descending order
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)

    # Result (total value in the Knapsack)
    final_value = 0.0

    # Loop through all items
    for item in arr:
        # If adding the item won't overflow, add it completely
        if item.weight <= W:
            W -= item.weight
            final_value += item.profit
        # If we can't add the full item, add fractional part of it
        else:
            final_value += item.profit * W / item.weight
            break
    
    # Returning final value
    return final_value

# Driver Code
if __name__ == "__main__":
    # Taking user input for knapsack capacity
    W = int(input("Enter the maximum weight of the knapsack: "))

    # Taking user input for number of items
    n = int(input("Enter the number of items: "))

    # Creating an empty list to store items
    arr = []
    for i in range(n):
        profit = float(input(f"Enter profit for item {i+1}: "))
        weight = float(input(f"Enter weight for item {i+1}: "))
        arr.append(Item(profit, weight))

    # Function call
    max_val = fractionalKnapsack(W, arr)
    print(f"Maximum value in the knapsack: {max_val}")
