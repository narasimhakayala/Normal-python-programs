text = input("Enter a string: ")

text = text.replace(",", "#")
text = text.replace(".", ",")
text = text.replace("#", ".")

print("Result:", text)
