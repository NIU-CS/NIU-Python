from rich import print

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq.pop()

if __name__ == "__main__":
    n = int(input("How many Fibonacci numbers do you want to generate: "))
    i = 0
    while(i < n):
        print(f"fibonacci({i}) = {fibonacci(i)}")
        i += 1
