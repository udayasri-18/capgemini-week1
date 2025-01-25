balance=20000

def checkBalance():
    return f"Your total balance is {balance}"

def depositMoney(deposit):
    global balance
    balance+=deposit
    print(f'You have deposited {deposit} into your account')
    return checkBalance()
    

def withdrawMoney(withdrawmoney):
    global balance
    if balance > withdrawmoney:
        balance=balance-withdrawmoney
        print(f"You've withdrawn {withdrawmoney}")

    else:
        print(f"Insufficient balance for withdrawal")

    return checkBalance()
def exit():
    return "End"

print(depositMoney(1000))
print(withdrawMoney(10000))
print(checkBalance())
print(exit())