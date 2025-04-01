from rich import print

if __name__ == "__main__":
    numbers = input("input 3 numbers: ").split()
    numbers = list(map(int, numbers))
    targets = [numbers[0], numbers[0] + numbers[1] * numbers[2], numbers[1]]
    for i in range(targets[0], targets[1], targets[2]):
        print(i)
