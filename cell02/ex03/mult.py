n1 = int(input("Enter the first number:\n"))
n2 = int(input("Enter the second number:\n"))
r = n1*n2
if r == 0:
    t = "The result is both positive and negative."
elif r < 0:
    t = "The result is negative."
else:
    t = "The result is positive."
print(f"{n1} x {n2} = {r}\n{t}")
