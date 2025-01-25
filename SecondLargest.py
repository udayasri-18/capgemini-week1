list1=list(map(int,input("Enter a list: ").split(" ")))
max=0
secondmax=0
for i in list1:
    if i>max:
        secondmax,max=max,i
    elif i>secondmax and i!=max:
        secondmax=i
print(f"Second Largest numer is {secondmax}")