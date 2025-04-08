from rich import print

if __name__ == "__main__":
    n = int(input("input n: "))
    sum = 0.0
    i = 1
    while i <= n:
        sum += 1 / (2 ** i)
        i += 1

    print(f"Sum of the first {n} terms of the series is {sum}")
