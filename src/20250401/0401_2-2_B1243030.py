from rich import print

if __name__ == "__main__":
    fib = [1, 1]
    target = int(input("input a number: "))
    for i in range(2, target):
        fib.append(fib[i - 1] + fib[i - 2])

    for i in range(target):
        print(f"number {i + 1}: {fib[i]}")