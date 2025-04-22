from rich import print
import random

if __name__ == "__main__":
    # guess odd number
    ans = random.randint(0, 9) * 2 + 1
    guess_count = 1
    while True:
        guess = int(input("guess odd number: "))
        if guess == ans:
            print("[green]correct![/green]")
            print(f"[green]guess count: {guess_count}[/green]")
            break
        elif guess % 2 == 0:
            print("[red]even number![/red]")
            continue
        elif guess == -1:
            print("[red]exit![/red]")
            break
        else:
            print("[red]wrong![/red]")
            guess_count += 1
            continue
