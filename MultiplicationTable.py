num1=int(input("Enter the number to generate multiplication table: "))
num2=int(input("Enter the range: "))

for i in range(1,num2+1):
    res=num1*i
    print(f"{num1} x {i} = {res}")