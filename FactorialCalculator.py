n=int(input("Enter a number :"))
ans=1
if n<0:
    print("Negative number")
elif n==0:
    print("Factorail of 0 is 1")
else:
    for i in range(1,n+1):
        ans*=i
    print(f"Factorial of {n} is",ans)