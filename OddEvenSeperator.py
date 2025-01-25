list1=list(input("Enter list of numbers: ").split(' '))

evenlist=[]
oddlist=[]

for i in list1:
    if int(i)%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print("The even list is",evenlist)
print("The oddlist is",oddlist)