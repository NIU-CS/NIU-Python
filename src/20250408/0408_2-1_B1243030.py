from rich import print
import random

if __name__ == "__main__":
    # random walk
    pos = [0, 0]
    total_steps = 0
    target_pos_x = int(input("Enter target position x: "))
    target_pos_y = int(input("Enter target position y: "))
    while pos != [target_pos_x, target_pos_y]:
        choices = [0, 1], [0, -1], [1, 0], [-1, 0]
        step = random.choice(choices)
        pos[0] += step[0]
        pos[1] += step[1]
        print(f"Position: {pos}, Total Steps: {total_steps}")

        total_steps += 1

    print(f"Total steps: {total_steps}")
    print(f"Final position: {pos}")
