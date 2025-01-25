n=int(input("Enter no. of rows: "))
choice=input("Enter reverse to print pattern in reverse else no: ")
if choice=='reverse':
    for i in range(1,n+1):
        print('*'*(n-i+1))
else:
    for i in range(1,n+1):
        print('*'*i)

