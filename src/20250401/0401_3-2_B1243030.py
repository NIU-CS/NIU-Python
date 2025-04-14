from rich import print

if __name__ == "__main__":
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j % 2 == 0:
                print(f"{i} * {j} = {i * j}", end="\t")
            else:
                print(f"         ", end="\t")
        print()
