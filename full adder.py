a = int(input("Enter A (0 or 1): "))
b = int(input("Enter B (0 or 1): "))
cin = int(input("Enter Carry-in (0 or 1): "))

sum_bit = a ^ b ^ cin
carry_out = (a & b) | (b & cin) | (a & cin)

print("Sum =", sum_bit)
print("Carry-out =", carry_out)
