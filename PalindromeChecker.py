t=int(input("Enter number of values: "))
for i in range(t):
    n1=input("Enter string: ")
    n2=n1[::-1]
    if n1==n2:
        print("string is palindrome")
    else:
        print("String is not a palindrome")