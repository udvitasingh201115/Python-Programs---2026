a=int(input("enter a number"))
n=2
while n <= a-1:
    if a%n == 0:
        print(f"{a} is divided by {n}.")
        print(f"{a} is not a PRIME NUMBER")
        break
    n = n+1
else:
    print(f"{a} is a PRIME NUMBER")