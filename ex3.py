import math

hours = int(input("hours = "))
pay = float(input("pay = "))

if not all([hours > 0, pay > 0]):
    print("invalid input")
    exit(1)

print(f"salary = { math.floor(pay * hours * 100) / 100 : .2f}")

