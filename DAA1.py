# Non recursive function for fibonacci series.

def fibonacci_non_recursive(n):
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a,b = 0,1
    for _ in range(2, n+1):
        a,b = b, a+b
    return b

# Test
n = 10
print(f"Fibonacci number at position {n} is: {fibonacci_non_recursive(n)}")

# Recursive function for fibonacci numbers

def fibonacci_recursive(n):
    # Time Complexity: O(2^n)
    # Space Complexity: O(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    
    
# Test
n = 10
print(f"Fibonacci number at position {n} is: {fibonacci_recursive(n)}")
