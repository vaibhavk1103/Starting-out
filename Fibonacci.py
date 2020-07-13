# Fibonacci series using while loop in python.
def fibo(n):
    x0 = 0
    x1 = 1
    c = 0
    print(x0)           # Printing the first number of the series.
    while (c < n-1):
        xs = x0 + x1
        print(xs)
        c += 1
        x0 = x1
        x1 = xs


n = int(input("Enter the number upto which you want the Fibonacci series to be printed:"))
fibo(n);
