a = float(input("a = "))
b = float(input("b = "))
h = float(input("h = "))

if not all((a > 0, b > 0, h > 0)):
    print("invalid input")
    exit(1)

print(f"area = {(a + b) * h / 2: .2f}")

