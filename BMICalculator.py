height=int(input("Enter your height in meters: "))
weight=int(input("Enter your weight in kilograms: "))

bmi=weight/(height**2)

if bmi<18:
    print("Underweight")
elif bmi<29.9 and bmi>25:
    print("Overweight")
elif bmi>30:
    print("Obesity")
else:
    print("Normal")