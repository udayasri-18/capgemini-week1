
total_marks=0
name=input("Enter your name :")
for i in range(1,6):
    marks=int(input(f"Enter marks for subject {i} for 100 :"))
    total_marks+=marks

percentage=(total_marks/500)*100

if percentage>90:
    grade='A'
elif percentage>80 and percentage<=90:
    grade='B'
elif percentage>70 and percentage<=80:
    grade='C'
elif percentage>70 and percentage<=80:
    grade='D'
elif percentage>60 and percentage<=70:
    grade='E'
else:
    grade='F'

print(f"Total marks scored by {name}are ",total_marks)
print(f"Percentage of {name} is ",percentage)
print(f"Grade acquired by {name}is",grade)