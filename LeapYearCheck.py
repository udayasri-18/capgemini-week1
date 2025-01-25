t=int(input("Enter number of testcases: "))
for i in range(t):
    n=int(input("Enter the year: "))
    if n%4==0:
        print(f"Year {n} is a leap year")
    else:
        print(f"Year {n} is not a leap year")