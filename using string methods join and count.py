n = int(input("Enter the value of n: "))

numbers = " ".join(str(i) for i in range(1, n + 1, 2))

print(numbers)
print("Count of odd numbers =", numbers.count(" ") + 1 if numbers else 0)
