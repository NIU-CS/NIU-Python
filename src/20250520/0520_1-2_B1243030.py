from rich import print

if __name__ == "__main__":
    # 1. Split the input text into words and align each word left and right (column width: 10 characters)
    text = input("Enter a sentence: ")
    words = text.split()

    print("\nLeft and right aligned (10 characters per column):")
    for word in words:
        print(word.ljust(10), word.rjust(10))

    # 2. Center align each word (total width: 30 characters)
    print("\nCenter aligned (width 30):")
    for word in words:
        print(word.center(30, '-'))

    # 3. Use partition() to split the sentence into three parts and print them separately
    partition_input = input("\nEnter a sentence to partition (will split at the first space): ")
    part1, sep, part2 = partition_input.partition(" ")

    print("\nFirst part: ", part1)
    print("Separator : ", sep)
    print("Second part:", part2)