bill_amount=int(input("Enter bill amount: "))
people=int(input("Enter number of people: "))
tip=int(input("Enter tip percentage: "))

tip_amount=(bill_amount*tip)/100

amount=(bill_amount+tip_amount)/people

print("Amount o be paid by each person",amount)
