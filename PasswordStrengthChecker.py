str1=input("Enter password: ")
digit=0
lower=0
upper=0
special=0
for i in str1:
    if i.isdigit():
        digit+=1
    elif i>='a' and i<='z':
        lower+=1
    elif i>='A' and i<='Z':
        upper+=1
    else:
        special+=1
if len(str1)>7 and digit>0 and lower>0 and upper>0 and special>0:
    print("Strong Password")
else:
    print("Weak Password")