ask="y"

while ask=="y":
    m=int(input("enter a number: "))
    if m % 2==0:
        print(f"{m} is even")
    else:
        print(f"{m} is odd")
    
    ask=input("Do you want to continue? (y/n): ")

