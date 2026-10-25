text = input("Enter a string: ")
i = int(input("Enter the character position to remove: "))

result = text[:i] + text[i + 1:]

print("String after removing character:", result)
