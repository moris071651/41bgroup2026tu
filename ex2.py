import math

r = float(input("r = "))

if r <= 0:
    print("invalid input")
    exit(1)

print(f"P = {2 * math.pi * r: .3f}")
print(f"S = {math.pi * r * r: .3f}")

