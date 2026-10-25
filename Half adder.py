a = int(input("Enter A (0 or 1): "))
b = int(input("Enter B (0 or 1): "))

sum_bit = a ^ b
carry = a & b

print("Sum =", sum_bit)
print("Carry =", carry)
