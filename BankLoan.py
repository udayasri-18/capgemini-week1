salary=int(input("Enter your salary per annum "))
age=int(input("Enter your age "))
creditscore=int(input("Enter your credit score "))

loanamount=int(input("\nEnter loan amount required "))

if loanamount>(2*salary):
    print(f"Loan rejected due to less salary income")
elif age<21:
     print(f"Loan rejected age is less than 21")
elif creditscore<1000:
    print(f"Loan rejected creditscore is less than 10000")
else:
    print("Loan Approved")