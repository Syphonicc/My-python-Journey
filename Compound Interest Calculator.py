# Python compound interest calculator
P =0
r = 0
t= 0

while P <= 0:
    P = float(input("Enter the principle amount:"))
    if P <= 0:
        print("Principle can't be less than or equal to zero")

while r <= 0:
    r = float(input("Enter the rate amount:"))
    if r <= 0:
        print("Rate can't be less than or equal to zero")
while t <= 0:
    t = float(input("Enter the time:"))
    if t <= 0:
        print("Time can't be less than or equal to zero")

total = P * pow((1 + r / 100), t)
print(f"Balance after {t} year/s: ${total:.2f}")