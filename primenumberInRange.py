num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

def isprime(n):
    flag=0
    if n<=1:
        return True
    else:
        for i in range(2,int(n)):
            if n%i==0:
                flag=1
                break
    if(flag==1):
        return False
    else:
        return True
print(f"Prime numbers between {num1} and {num2}")
for i in range(num1,num2):
    if isprime(i):
        print(f"{i}")
    