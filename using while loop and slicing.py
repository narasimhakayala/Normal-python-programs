n = int(input("Enter the value of n: "))

numbers = list(range(1, n + 1))
odd_numbers = numbers[::2]

while odd_numbers:
    print(odd_numbers[0])
    odd_numbers = odd_numbers[1:]
