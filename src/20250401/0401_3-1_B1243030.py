from rich import print

if __name__ == "__main__":
    for i in range(1, 10):
        for j in range(1, 10):
            if i >= j:
                print(f"{i} * {j} = {i * j}", end="\t")
        print()