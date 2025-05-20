from rich import print

if __name__ == "__main__":
    # 1. First letter uppercase, rest lowercase
    name = input("Enter a English name: ")
    formatted_name = name.capitalize()
    print("Formatted: ", formatted_name)

    # 2. Convert to uppercase and lowercase
    text = input("Input a sentence: ")
    print("All uppercase: ", text.upper())
    print("All lowercase: ", text.lower())

    # 3. Check format: islower, isupper, istitle
    sentence = input("Input a sentence: ")
    print("All char are lowercase? ", sentence.islower())
    print("All char are uppercase? ", sentence.isupper())
    print("Is title? ", sentence.istitle())