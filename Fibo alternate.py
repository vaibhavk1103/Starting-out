# Fibonacci series using for loop in python.
def fibo(n):
    x0 = 0                    # Initializing the series.
    x1 = 1                    # Initializing the series.
    c = 0
    print(x0)                 # Printing the first number in the series.
    for c in range(0, n - 1):
        xs = x0 + x1          # Formula for next term.
        print(xs)
        c += 1
        x0 = x1
        x1 = xs


n = int(input("Enter the number upto which you want the Fibonacci series to be printed:"))
fibo(n)
