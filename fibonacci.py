def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        while len(fib) < n:
            next_num = fib[-1] + fib[-2]
            fib.append(next_num)
        return fib

# Get the number of Fibonacci numbers to calculate from the user
try:
    n = int(input("Enter the number of Fibonacci numbers to calculate: "))
    if n < 0:
        print("Please enter a non-negative number.")
    else:
        result = fibonacci(n)
        print(f"The first {n} Fibonacci numbers are: {result}")
except ValueError:
    print("Please enter a valid number.")