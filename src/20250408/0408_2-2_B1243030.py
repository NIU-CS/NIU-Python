from rich import print
import random

if __name__ == "__main__":
    runner1 = 0
    runner2 = 0
    steps = 0
    while runner1 < 100 and runner2 < 100:
        steps += 1
        runner1 += random.randint(1, 3)
        runner2 += random.randint(1, 3)

    print(f"Total steps: {steps}")
    print(f"Runner 1: {runner1}, Runner 2: {runner2}")
